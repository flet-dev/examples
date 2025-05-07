import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    def handle_action_click(e):
        page.add(ft.Text(f"Action clicked: {e.control.content}"))
        page.pop_dialog()

    cupertino_actions: list[ft.Control] = [
        ft.CupertinoDialogAction(
            content="Yes",
            destructive=True,
            on_click=handle_action_click,
        ),
        ft.CupertinoDialogAction(
            content="No",
            default=False,
            on_click=handle_action_click,
        ),
    ]

    material_actions: list[ft.Control] = [
        ft.TextButton(content="Yes", on_click=handle_action_click),
        ft.TextButton(content="No", on_click=handle_action_click),
    ]

    page.add(
        ft.FilledButton(
            content="Open Material Dialog",
            on_click=lambda e: page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Material Alert Dialog"),
                    content=ft.Text("Do you want to delete this file?"),
                    actions=material_actions,
                )
            ),
        ),
        ft.CupertinoFilledButton(
            content="Open Cupertino Dialog",
            on_click=lambda e: page.show_dialog(
                ft.CupertinoAlertDialog(
                    title=ft.Text("Cupertino Alert Dialog"),
                    content=ft.Text("Do you want to delete this file?"),
                    actions=cupertino_actions,
                )
            ),
        ),
        ft.FilledButton(
            content="Open Adaptive Dialog",
            adaptive=True,
            bgcolor=ft.Colors.BLUE_ACCENT,
            on_click=lambda e: page.show_dialog(
                ft.AlertDialog(
                    adaptive=True,
                    title=ft.Text("Adaptive Alert Dialog"),
                    content=ft.Text("Do you want to delete this file?"),
                    actions=(
                        cupertino_actions
                        if page.platform in [ft.PagePlatform.IOS, ft.PagePlatform.MACOS]
                        else material_actions
                    ),
                )
            ),
        ),
    )


ft.app(main)
