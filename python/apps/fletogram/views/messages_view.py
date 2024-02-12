import flet as ft


class MessagesView(ft.View):
    def __init__(self, chat):
        super().__init__()
        self.route = "/chat"
        self.chat = chat
        self.appbar = ft.AppBar(
            title=ft.Text(self.chat.display_name),
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        self.generate_messages_view()

    def generate_messages_view(self):
        messages_view = ft.ListView(spacing=5)
        for message in self.chat.messages:
            if message.is_logged_user:
                alignment = ft.MainAxisAlignment.END
            else:
                alignment = ft.MainAxisAlignment.START
            messages_view.controls.append(
                ft.Row(
                    [message],
                    alignment=alignment,
                )
            )
            print(message.body)
        self.controls = [messages_view]
