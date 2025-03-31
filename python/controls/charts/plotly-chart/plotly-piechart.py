import plotly.graph_objects as go

import flet as ft
from flet.plotly_chart import PlotlyChart


def main(page: ft.Page):

    labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    page.add(PlotlyChart(fig, expand=True))


ft.app(main)
