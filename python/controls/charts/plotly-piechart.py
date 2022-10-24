import plotly.graph_objects as go

import flet
from flet import Page
from flet.plotly_chart import PlotlyChart


def main(page: Page):

    labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    page.add(PlotlyChart(fig, expand=True))


flet.app(target=main)
