import flet as ft


def main(page: ft.Page):
    file_picker = ft.FilePicker()
    page.services.append(file_picker)

    # Pick files dialog
    async def open_pick_files_dialog(e):
        files = await file_picker.pick_files_async(allow_multiple=True)
        selected_files.value = (
            ", ".join(map(lambda f: f.name, files)) if files else "Cancelled!"
        )

    # Save file dialog
    async def open_save_file_dialog(e):
        save_file_path.value = await file_picker.save_file_async()

    # Open directory dialog
    async def open_get_directory_dialog(e):
        directory_path.value = await file_picker.get_directory_path_async()

    page.add(
        ft.Row(
            [
                ft.Button(
                    "Pick files",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=open_pick_files_dialog,
                ),
                selected_files := ft.Text(),
            ]
        ),
        ft.Row(
            [
                ft.Button(
                    "Save file",
                    icon=ft.Icons.SAVE,
                    on_click=open_save_file_dialog,
                    disabled=page.web,
                ),
                save_file_path := ft.Text(),
            ]
        ),
        ft.Row(
            [
                ft.Button(
                    "Open directory",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=open_get_directory_dialog,
                    disabled=page.web,
                ),
                directory_path := ft.Text(),
            ]
        ),
    )


ft.run(main)
