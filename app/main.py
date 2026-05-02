from config import MODEL_PROVIDER
from gemini_client import ask_gemini
from openai_client import ask_openai


def ask_llm(user_input: str) -> str:
    if MODEL_PROVIDER == "gemini":
        return ask_gemini(user_input)
    elif MODEL_PROVIDER == "openai":
        return ask_openai(user_input)
    else:
        return f"Error: Unsupported provider: {MODEL_PROVIDER}"


def main() -> None:
    print("🤖 Multi-Model Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("Your Query: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            reply = ask_llm(user_input)
            print("\nAI:", reply, "\n")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
