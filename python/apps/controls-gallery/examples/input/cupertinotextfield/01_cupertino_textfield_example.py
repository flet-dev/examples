import flet as ft

name = "CupertinoTextField example"


def example():

    tf1 = ft.TextField(
        label="Material",
    )
    tf2 = ft.CupertinoTextField(
        placeholder_text="Cupertino",
    )
    tf3 = ft.TextField(
        adaptive=True,
        label="Adaptive",
    )

    return ft.Column(controls=[tf1, tf2, tf3])
