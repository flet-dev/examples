from groq import Groq
import flet as ft

# Initialize Groq client with API key
client = Groq(
    api_key='your_groq_api_key_here',
)

class Message:
    def __init__(self, user: str, text: str, response_text: str):
        self.user = user
        self.text = text
        self.response_text = response_text

def main(page: ft.Page):
    chat = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)
    new_message = ft.TextField(expand=True, hint_text="Type your message here...")

    def on_message(message: Message):
        chat.controls.append(ft.Text(f"User: {message.text}"))
        chat.controls.append(ft.Text(f"Bot: {message.response_text}"))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        user_message = new_message.value
        if user_message:
            new_message.value = ""
            processing_text = ft.Text("Processing answer...", color="blue")
            chat.controls.append(processing_text)
            page.update()
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_message,
                    }
                ],
                model="llama-3.1-70b-versatile",
            )
            response_text = chat_completion.choices[0].message.content
            message = Message(user=page.session_id, text=user_message, response_text=response_text)
            page.pubsub.send_all(message)
            new_message.value = ""
            page.update()

    page.add(
        ft.Container(
            content=ft.Column([
                chat,
                ft.Row([new_message, ft.ElevatedButton("Send", on_click=send_click)])
            ]),
            expand=True,
            padding=10
        )
    )

ft.app(target=main)
