import os
import matplotlib
import mplfinance as mpf
import pandas as pd

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: ft.Page):

    csv_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "assets/SP500_NOV2019_Hist.csv"
    )
    print(csv_path)
    daily = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    daily.index.name = "Date"
    daily.shape
    daily.head(3)
    daily.tail(3)

    fig, axlist = mpf.plot(daily, type="candle", mav=(3, 6, 9), returnfig=True)

    page.add(MatplotlibChart(figure=fig, expand=True))


ft.run(target=main)
