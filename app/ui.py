import gradio as gr

from config import MODEL_PROVIDER
from gemini_client import ask_gemini
from openai_client import ask_openai


def ask_llm(message: str) -> str:
    if not message.strip():
        return "Please enter a question."

    try:
        if MODEL_PROVIDER == "gemini":
            return ask_gemini(message)
        elif MODEL_PROVIDER == "openai":
            return ask_openai(message)
        else:
            return f"Unsupported provider: {MODEL_PROVIDER}"
    except Exception as e:
        return f"Error: {e}"


demo = gr.Interface(
    fn=ask_llm,
    inputs=gr.Textbox(
        label="Your question",
        placeholder="Ask anything, e.g. Explain what fever is in simple terms.",
        lines=4,
    ),
    outputs=gr.Textbox(label="AI response", lines=12),
    title="🤖 Multi-Model LLM Playground",
    description=(
        "An interactive AI chatbot UI using Gemini or OpenAI. "
        f"Current provider: {MODEL_PROVIDER}"
    ),
    examples=[
        ["Explain what fever is in simple terms."],
        ["Explain Retrieval-Augmented Generation in 3 bullet points."],
        ["請用簡單方式解釋什麼是機器學習。"],
    ],
)


if __name__ == "__main__":
    demo.launch()
