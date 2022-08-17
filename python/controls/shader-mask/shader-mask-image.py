import flet
from flet import (
    Image,
    LinearGradient,
    Page,
    RadialGradient,
    Row,
    ShaderMask,
    alignment,
    colors,
)


def main(page: Page):
    page.add(
        Row(
            [
                ShaderMask(
                    Image(
                        src="https://picsum.photos/200/300?1",
                        width=400,
                        height=400,
                        fit="fill",
                    ),
                    blend_mode="colorBurn",
                    shader=RadialGradient(
                        center=alignment.top_left,
                        radius=1.0,
                        colors=[colors.YELLOW, colors.DEEP_ORANGE_900],
                        tile_mode="clamp",
                    ),
                ),
                ShaderMask(
                    Image(src="https://picsum.photos/200/300?2"),
                    blend_mode="dstIn",
                    shader=LinearGradient(
                        begin=alignment.top_center,
                        end=alignment.bottom_center,
                        colors=[colors.BLACK, colors.TRANSPARENT],
                        stops=[0.5, 1.0],
                    ),
                ),
            ]
        )
    )


flet.app(target=main)
