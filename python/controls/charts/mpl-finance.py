import matplotlib
import mplfinance as mpf
import pandas as pd

import flet
from flet import Page
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: Page):

    daily = pd.read_csv(
        ".\\playground\\data\\SP500_NOV2019_Hist.csv", index_col=0, parse_dates=True
    )
    daily.index.name = "Date"
    daily.shape
    daily.head(3)
    daily.tail(3)

    fig, axlist = mpf.plot(daily, type="candle", mav=(3, 6, 9), returnfig=True)

    page.add(MatplotlibChart(fig, expand=True))


flet.app(target=main)
