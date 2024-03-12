import flet as ft

name = "PieChart 1"


def example():
    normal_border = ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
    hovered_border = ft.BorderSide(6, ft.colors.WHITE)

    async def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            section.border_side = (
                hovered_border if idx == e.section_index else normal_border
            )
        await chart.update_async()

    chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                25,
                color=ft.colors.BLUE,
                radius=80,
                border_side=normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.colors.YELLOW,
                radius=65,
                border_side=normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.colors.PINK,
                radius=60,
                border_side=normal_border,
            ),
            ft.PieChartSection(
                25,
                color=ft.colors.GREEN,
                radius=70,
                border_side=normal_border,
            ),
        ],
        sections_space=1,
        center_space_radius=0,
        on_chart_event=on_chart_event,
        expand=True,
    )

    return chart
