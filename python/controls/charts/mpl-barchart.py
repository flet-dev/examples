import matplotlib
import matplotlib.pyplot as plt

import flet
from flet import Page
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: Page):

    fig, ax = plt.subplots()

    fruits = ["apple", "blueberry", "cherry", "orange"]
    counts = [40, 100, 30, 55]
    bar_labels = ["red", "blue", "_red", "orange"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel("fruit supply")
    ax.set_title("Fruit supply by kind and color")
    ax.legend(title="Fruit color")

    page.add(MatplotlibChart(fig, expand=True))


flet.app(target=main)
