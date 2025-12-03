"""Main Reflex-GPT application."""

import reflex as rx
import os
from dotenv import load_dotenv
import openai
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatMessage(rx.Base):
    """Chat message model."""
    id: str
    user: str
    content: str
    timestamp: str
    is_bot: bool = False


class State(rx.State):
    """The app state."""
    chat_history: list[ChatMessage] = []
    current_input: str = ""
    is_loading: bool = False
    error_message: str = ""

    def send_message(self):
        """Send a message to the AI and get a response."""
        if not self.current_input.strip():
            self.error_message = "Please enter a message"
            return

        # Add user message
        user_msg = ChatMessage(
            id=f"user_{len(self.chat_history)}",
            user="You",
            content=self.current_input,
            timestamp=datetime.now().isoformat(),
            is_bot=False,
        )
        self.chat_history.append(user_msg)
        
        self.is_loading = True
        self.current_input = ""

    async def get_ai_response(self):
        """Get response from OpenAI API."""
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": self.chat_history[-1].content}
                ],
                temperature=0.7,
                max_tokens=500,
            )
            
            bot_response = response["choices"][0]["message"]["content"]
            
            bot_msg = ChatMessage(
                id=f"bot_{len(self.chat_history)}",
                user="Assistant",
                content=bot_response,
                timestamp=datetime.now().isoformat(),
                is_bot=True,
            )
            self.chat_history.append(bot_msg)
            self.error_message = ""
            
        except Exception as e:
            self.error_message = f"Error: {str(e)}"
        finally:
            self.is_loading = False

    def clear_chat(self):
        """Clear chat history."""
        self.chat_history = []
        self.current_input = ""
        self.error_message = ""


def message_bubble(msg: ChatMessage) -> rx.Component:
    """Render a message bubble."""
    return rx.box(
        rx.text(
            msg.content,
            font_size="14px",
            padding="12px",
            border_radius="8px",
            background_color=rx.cond(
                msg.is_bot,
                "#e3f2fd",
                "#c8e6c9",
            ),
            color="black",
        ),
        width="100%",
        padding="8px 0",
        margin_bottom="8px",
    )


def index() -> rx.Component:
    """The main page."""
    return rx.container(
        rx.heading(
            "Reflex-GPT Chat",
            font_size="2xl",
            margin_bottom="20px",
            text_align="center",
        ),
        rx.box(
            rx.foreach(State.chat_history, message_bubble),
            height="400px",
            overflow_y="auto",
            border="1px solid #ccc",
            padding="16px",
            border_radius="8px",
            margin_bottom="20px",
            background_color="#f5f5f5",
        ),
        rx.cond(
            State.error_message != "",
            rx.text(
                State.error_message,
                color="red",
                margin_bottom="10px",
            ),
        ),
        rx.hstack(
            rx.input(
                value=State.current_input,
                placeholder="Type your message...",
                on_change=State.set_current_input,
                on_blur=lambda: State.send_message(),
                width="100%",
                padding="10px",
                border_radius="4px",
            ),
            rx.button(
                "Send",
                on_click=State.send_message,
                is_loading=State.is_loading,
            ),
            width="100%",
            margin_bottom="10px",
        ),
        rx.button(
            "Clear Chat",
            on_click=State.clear_chat,
            color_scheme="red",
            width="100%",
        ),
        max_width="600px",
        margin="0 auto",
        padding="20px",
    )


app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.compile()
