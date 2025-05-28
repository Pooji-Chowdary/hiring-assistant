# 🤖 TalentScout Hiring Assistant

An intelligent, offline technical interview assistant that generates relevant interview questions based on a candidate’s tech stack and experience level — all powered by a local `flan-t5-large` model with no need for API keys or internet access.

---

## 🧩 Overview

TalentScout is a Streamlit web app that acts as an AI hiring assistant. It takes candidate inputs such as name, contact info, tech stack, and experience level, then uses a locally loaded transformer model to generate targeted technical interview questions.

This project avoids reliance on cloud APIs like OpenAI or Hugging Face Inference by running `google/flan-t5-large` directly on your machine using the `transformers` library.

---

## 🛠 Installation

Ensure you have **Python 3.8+** installed. Then run:

```bash
pip install streamlit torch transformers sentencepiece
```

> Note: `flan-t5-large` requires ~2.5GB of memory. For smoother performance, use a machine with at least 16 GB RAM.

---

## ▶️ How to Run

Launch the app with:

```bash
streamlit run app.py
```

This will open a browser window where you can:

1. Fill in candidate details
2. Choose a tech stack (e.g., Python, React, MySQL)
3. Select experience level (Beginner / Intermediate / Advanced)
4. Generate tailored interview questions instantly

---

## 💬 Prompt Design Explanation

The model prompt is crafted to simulate a **technical interviewer** generating questions based on:

- The **technologies listed**
- The **experience level** selected

### Example Prompt Sent to Model:

> *"You are an expert technical interviewer. For a Beginner candidate, generate 3 relevant and practical technical interview questions for each technology in this list: Python, Django. The questions should assess skill level appropriate to Beginner. Return a clearly numbered list grouped by technology."*

This approach gives the model clear context and formatting expectations, leading to high-quality, organized output.

---

## 🧱 Libraries & Architecture

| Library       | Purpose                                  |
|---------------|------------------------------------------|
| `streamlit`   | Web UI for collecting user input         |
| `transformers`| Load and run `flan-t5-large` locally     |
| `torch`       | Backend tensor engine for model execution|
| `sentencepiece`| Tokenizer support for T5 models         |

### Architecture Flow:
```
[User Input via Streamlit Form]
        ↓
[Prompt Construction Based on Inputs]
        ↓
[flan-t5-large model generates questions]
        ↓
[Streamlit displays numbered Q&A list]
```

---

## 🧠 Challenges & Solutions

| Challenge                                 | Solution |
|------------------------------------------|----------|
| Hugging Face models returning 404 errors | Switched to running models locally |
| Poor generation relevance                | Improved prompt phrasing and added beam search |
| Slow loading                             | Cached the model using `@st.cache_resource` |
| Streamlit runtime error from PyTorch     | Suppressed harmless warning using `warnings` module |

---

## ✅ Future Improvements

- Add export to PDF/CSV
- Support for resume parsing
- Customize difficulty and question types
- Switch to quantized versions for low-RAM systems

---

## 📦 Credits

- Model: [google/flan-t5-large](https://huggingface.co/google/flan-t5-large)
- UI: [Streamlit](https://streamlit.io/)
- Transformers: [Hugging Face](https://huggingface.co/transformers/)
