import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet
from flet import Page
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: Page):

    N = 45
    x, y = np.random.rand(2, N)
    c = np.random.randint(1, 5, size=N)
    s = np.random.randint(10, 220, size=N)

    fig, ax = plt.subplots()

    scatter = ax.scatter(x, y, c=c, s=s)

    # produce a legend with the unique colors from the scatter
    legend1 = ax.legend(*scatter.legend_elements(), loc="lower left", title="Classes")
    ax.add_artist(legend1)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
    legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

    page.add(MatplotlibChart(fig, expand=True))


flet.app(target=main)
