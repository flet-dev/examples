import plotly.express as px

import flet as ft
from flet.plotly_chart import PlotlyChart


def main(page: ft.Page):

    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.bar(
        df,
        x="year",
        y="pop",
        hover_data=["lifeExp", "gdpPercap"],
        color="country",
        labels={"pop": "population of Canada"},
        height=400,
    )

    page.add(PlotlyChart(fig, expand=True))


ft.app(main)
