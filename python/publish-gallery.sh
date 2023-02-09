pip install flet --pre
flet --version
flet publish python/apps/todo/todo.py --distpath python/dist/todo --base-url todo --pre --app-name "Flet To-Do" --app-description "A classic To-Do app inspired by TodoMVC project."
flet publish python/apps/icons-browser/main.py --distpath python/dist/icons-browser --base-url icons-browser --pre --app-name "Flet Icons Browser" --app-description "Quickly search through icons collection to use in your app."
flet publish python/tutorials/calc/calc.py --distpath python/dist/calculator --base-url calculator --pre --app-name "Calculator" --app-description "A simple calculator app written in Flet."
flet publish python/tutorials/solitaire/solitaire-final-part1/main.py --distpath python/dist/solitaire --base-url solitaire --assets assets --pre --app-name "Solitaire" --app-description "Learn how to handle gestures and position controls on a page."
flet publish python/apps/trolli/src/main.py --distpath python/dist/trolli --base-url trolli --assets ../assets --pre --app-name "Trolli" --app-description "A clone of Trello."