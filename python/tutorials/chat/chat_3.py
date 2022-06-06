import flet
from flet import AlertDialog, Column, ElevatedButton, Page, Row, Text, TextField

pub_sub = {}


def broadcast(user, message):
    for session_id, handler in pub_sub.items():
        handler(user, message)


def main(page: Page):

    messages = Column()
    message = TextField()

    def on_message(user, message):
        messages.controls.append(Text(f"{user}: {message}"))
        page.update()

    pub_sub[page.session_id] = on_message

    def send_click(e):
        broadcast(page.user, message.value)
        message.value = ""
        page.update()

    user_name = TextField(label="Enter your name")

    page.user = page.session_id

    def join_click(e):
        if not user_name.value:
            user_name.error_message = "Name cannot be blank!"
            user_name.update()
        else:
            page.user = user_name.value
            dlg.open = False
            page.update()

    dlg = AlertDialog(
        open=True,
        modal=True,
        title=Text("Welcome!"),
        content=Column([user_name], tight=True),
        actions=[ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )

    send = ElevatedButton("Send", on_click=send_click)
    form = Row([message, send])
    page.add(messages, form, dlg)


flet.app(target=main, view=flet.WEB_BROWSER)
