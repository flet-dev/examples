import plotly.express as px

import flet
from flet import Page
from flet.plotly_chart import PlotlyChart


def main(page: Page):

    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color="country")

    page.add(PlotlyChart(fig, expand=True))


flet.app(target=main)
