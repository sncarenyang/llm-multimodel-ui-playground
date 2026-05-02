# 🤖 LLM Multi-Model UI Playground

A simple **interactive AI chatbot UI** supporting Google Gemini and OpenAI.

This project demonstrates:
- LLM API integration
- Interactive web UI with Gradio
- Multi-model architecture
- Clean modular Python design

---

## 🚀 Features

- Web-based chatbot UI
- Supports Gemini and OpenAI
- Default model: gemini-2.5-flash
- Easy model switching
- Works in GitHub Codespaces / Colab / local Python environment

---

## 🏗️ Project Structure

```text
llm-multimodel-ui-playground/
├── README.md
├── requirements.txt
└── app/
    ├── ui.py
    ├── main.py
    ├── config.py
    ├── gemini_client.py
    └── openai_client.py
```
---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```
---

## 🔑 API Key Setup

### For Gemini

```bash
export GOOGLE_API_KEY=your_google_api_key
```
### For OpenAI

```bash
export OPENAI_API_KEY=your_openai_api_key
```
Gemini is the default provider in `app/config.py`.

---

## ▶️ Run CLI Version

```bash
python app/main.py
```
---

## 🖥️ Run Web UI

bash
python app/ui.py

If running in Codespaces, open the forwarded port shown by GitHub Codespaces.

---

## 🧠 How It Works

- ui.py creates the Gradio web interface
- main.py runs the command-line chatbot
- config.py controls the default provider and model names
- gemini_client.py handles Gemini API calls
- openai_client.py handles OpenAI API calls

---

## 📌 Portfolio Value

This project demonstrates practical AI engineering skills:

- Building interactive AI applications
- Connecting frontend UI with LLM backend logic
- Designing modular code for multiple model providers
- Handling real API integration and model configuration

---

## 📈 Future Improvements

- Add chat history memory
- Add streaming responses
- Add model selector in UI
- Add prompt templates
- Deploy to Hugging Face Spaces
