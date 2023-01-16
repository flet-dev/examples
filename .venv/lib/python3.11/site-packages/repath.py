import re

import six
from six.moves.urllib import parse as urllib

REGEXP_TYPE = type(re.compile(''))


# Match escaped characters that would otherwise appear in future matches.
# This allows the user to escape special characters that won't transform.
#
# Match Express-style parameters and un-named parameters with a prefix
# and optional suffixes. Matches appear as:
#
#  Path         | prefix | name   | capture | group | suffix | asterisk
# --------------+--------+--------+---------+-------+--------+----------
#  /:test(\d+)? | "/"    | "test" | "\d+"   | None  | "?"    | None
#  /route(\d+)  | None   | None   | None    | "\d+" | None   | None
#  /*           | "/"    | None   | None    | None  | None   | "*"

PATH_REGEXP = re.compile(r'''
    (?P<escaped>\\.)
    |
    (?P<prefix>[/.])?
    (?:
        (?:
            \:
            (?P<name>\w+)
            (?:
                \(
                (?P<capture>
                    (?:
                        \\.
                        |
                        [^()]
                    )+
                )
                \)
            )?
            |
            \(
            (?P<group>
                (?:
                    \\.
                    |
                    [^()]
                )
            +)
            \)
        )
        (?P<suffix>[+*?])?
        |
        (?P<asterisk>\*)
    )
''', re.X)

PATTERNS = dict(
    REPEAT='(?:{prefix}{capture})*',
    OPTIONAL='(?:{prefix}({name}{capture}))?',
    REQUIRED='{prefix}({name}{capture})'
)


def escape_string(string):
    """
    Escape URL-acceptable regex special-characters.

    """
    return re.sub('([.+*?=^!:${}()[\\]|])', r'\\\1', string)


def escape_group(group):
    return re.sub('([=!:$()])', r'\\\1', group)


def parse(string):
    """
    Parse a string for the raw tokens.

    :param path: express-style path string
    :return: list of path tokens used by :func:`tokens_to_pattern`

    """
    tokens = []
    key = 0
    index = 0
    path = ''

    for match in PATH_REGEXP.finditer(string):
        parts = match.groupdict()
        offset = match.start(0)
        path += string[index:offset]
        index = offset + len(match.group(0))

        if parts['escaped']:
            path += parts['escaped'][1]
            continue

        if path:
            tokens.append(path)
            path = ''

        delimiter = parts['prefix'] or '/'
        token_pattern = (
            parts['capture'] or
            parts['group'] or
            ('.*' if parts['asterisk'] else '[^%s]+?' % delimiter)
        )

        if not parts['name']:
            parts['name'] = key
            key += 1

        token = {
            'name': str(parts['name']),
            'prefix': parts['prefix'] or '',
            'delimiter': delimiter,
            'optional': parts['suffix'] in ('?', '*'),
            'repeat': parts['suffix'] in ('+', '*'),
            'pattern': escape_group(token_pattern),
        }

        tokens.append(token)

    if index < len(string):
        path += string[index:]

    if path:
        tokens.append(path)

    return tokens


def tokens_to_template(tokens):
    """
    Generate a function for templating tokens into a path string.

    """
    def template_function(obj):
        path = ''
        obj = obj or {}

        for token in tokens:
            if isinstance(token, six.string_types):
                path += token
                continue

            regexp = re.compile('^%s$' % token['pattern'])

            value = obj.get(token['name'])
            if value is None:
                if token["optional"]:
                    continue
                else:
                    raise KeyError(
                        'Expected "{name}" to be defined'.format(**token)
                    )

            if isinstance(value, list):
                if not token['repeat']:
                    raise TypeError(
                        'Expected "{name}" to not repeat'.format(**token)
                    )

                if len(value) == 0:
                    if token['optional']:
                        continue
                    else:
                        raise ValueError(
                            'Expected "{name}" to not be empty'.format(**token)
                        )

                for i, val in enumerate(value):
                    val = six.text_type(val)
                    if not regexp.search(val):
                        raise ValueError(
                            'Expected all "{name}" to match "{pattern}"'.format(**token)
                        )

                    path += token['prefix'] if i == 0 else token['delimiter']
                    path += urllib.quote(val, '')

                continue

            value = six.text_type(value)
            if not regexp.search(value):
                raise ValueError(
                    'Expected "{name}" to match "{pattern}"'.format(**token)
                )

            path += token['prefix'] + urllib.quote(value.encode('utf8'), '-_.!~*\'()')

        return path
    return template_function


def tokens_to_pattern(tokens, end=True, strict=False):
    """
    Generate a pattern for the given list of tokens.

    """
    route = ''
    last = tokens[-1]
    trailing_slash = isinstance(last, six.string_types) and last.endswith('/')

    for token in tokens:
        if isinstance(token, six.string_types):
            route += escape_string(token)
            continue

        parts = {
            'prefix': escape_string(token['prefix']),
            'capture': token['pattern'],
            'name': ''
        }

        if token['name'] and re.search('[a-zA-Z]', token['name']):
            parts['name'] = '?P<%s>' % re.escape(token['name'])

        if token['repeat']:
            parts['capture'] += PATTERNS['REPEAT'].format(**parts)

        segment_necessity = 'OPTIONAL' if token['optional'] else 'REQUIRED'
        segment_template = PATTERNS[segment_necessity]
        route += segment_template.format(**parts)

    if not strict:
        route = route[:-1] if trailing_slash else route
        route += '(?:/(?=$))?'

    if end:
        route += '$'
    else:
        route += '' if strict and trailing_slash else '(?=/|$)'

    return '^%s' % route


def compile(path, flags=0, **options):
    """
    Create a comiled regular expresion from the given path.

    :param path: express-style path string
    :param flags: (optional) regex flags as defined in :mod:`re`
    :param options: (optional) dictionary of options accepted by :func:`pattern`
    :return: A :mod:`re` compiled regular expression object.

    """
    return re.compile(pattern(path, **options), flags)


def match(path, string, flags=0, **options):
    """
    Match a string against a path.

    :param path: express-style path string
    :param string: a string to match against the generated regular expression
    :param flags: (optional) regex flags as defined in :mod:`re`
    :param options: (optional) dictionary of options accepted by :func:`pattern`
    :return: A :class:`_sre.SRE_Match` or ``None``

    """
    return compile(path, flags=0, **options).match(string)


def pattern(path, **options):
    """
    Generate a pattern from any kind of path value.

    This function selects the appropriate function array/regex/string paths,
    and calls it with the provided values.

    :param path: express-style path string, or list of paths, or compiled regex
    :param end: Make *path* match to the end of strings (default ``True``)
    :param strict: Enforce trailing slash in matched strins (default ``False``)
    :return: A regular expression pattern string

    """
    if isinstance(path, REGEXP_TYPE):
        return path.pattern
    if isinstance(path, list):
        parts = [pattern(p, **options) for p in path]
        return '(?:%s)' % '|'.join(parts)

    return tokens_to_pattern(parse(path), **options)


def template(path):
    """
    Compile a string to a template function for the path.

    :param path: express-style path string
    :return: A template funcion for generating paths from given field values

    """
    return tokens_to_template(parse(path))
