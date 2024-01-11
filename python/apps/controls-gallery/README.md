# Flet Controls Gallery app

Flet Controls Gallery app showcases examples of Flet controls usage.

# How to contribute

Contributions are welcome!

Fork this repo.

## To add new example to an existing Control:
1. Create file named `XX_example_name.py`, where XX would be order of example displayed for this control, starting with 01, for example "01_expansiontile_example.py", with the following contents:
```
import flet as ft

name = "<Example name>"


def example():
    return ft.Column()
```
2. Replace ft.Column with the control you want to display.

## To add new Control to an existing Control Group:
1. Create a new folder within the Control Group folder with the name of the Control
2. Create index.py file with the following contents:
```
name = "<Control name>"
description = """<Control description>"""
```

## To add new Control Group:

Submit Pull Request (PR) with your changes.

When the contribution is tested by Flet team/community a new Flet Controls Gallery release will be published.
