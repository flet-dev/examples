# Llama 3.1 Chatbot with Flet 
A simple chatbot application using Llama 3.1 model from Groq, built with the Flet framework. This app provides a user interface for sending messages to the chatbot and receiving responses.
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/llama-chatbot.git
    cd llama-chatbot
    ```

2. Install the required Python packages:

    ```bash
    pip install flet groq
    ```

3. Set up your Groq API key. Follow the instructions below to obtain your API key.

## Getting the API Key from Groq

1. Visit the [Groq website](https://groq.com) and sign up for an account.
2. Navigate to the API section of your account settings.
3. Generate a new API key and copy it.

## Usage

1. Open the `chatbot.py` file in a text editor.
2. Replace the placeholder API key with your Groq API key:

    ```python
    client = Groq(
        api_key='your_groq_api_key_here',
    )
    ```

3. Save the file and run the application:

    ```bash
    python chatbot.py
    ```

4. The application will open a window with the chat interface. Type your message and press "Send" to interact with the chatbot.
