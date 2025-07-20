```markdown
# 📄 LLM-Powered Resume Optimizer (Local Version)

A local, privacy-focused resume optimization tool powered by a lightweight LLM (e.g. Phi-2 via `llama-cpp-python`). It analyzes and rewrites sections of your resume to better match a target job description — all offline, with no cloud APIs.

---

## ✨ Features

- 🔍 Resume-JD alignment via LLM rewriting
- 🧠 Local inference using `llama-cpp-python`
- 🖥️ Tkinter-based GUI (cross-platform)
- ⚡ Section-by-section live streaming output
- 🛡️ 100% offline & secure (no internet required)
- 📝 Smart segmentation of resume text (e.g., Experience, Skills, Education)

---

## 📁 Project Structure
```

resume_optimizer/
├── app.py # Main Tkinter GUI
├── core/
│ ├── rewriter.py # Resume segmentation + LLM logic
│ └── **init**.py
├── config.yaml # Path to your GGUF model
├── README.md

````

---

## ⚙️ Setup Instructions

### 1. Install Requirements

```bash
pip install llama-cpp-python pyyaml
````

> Optional (for faster local inference): Install `llama-cpp-python` with CUDA or Metal support.

---

### 2. Download a GGUF Model

Get a small LLM like [Phi-2](https://huggingface.co/TheBloke/phi-2-GGUF) or [Mistral-Instruct](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF).

Place the `.gguf` file somewhere locally and update `config.yaml`:

```yaml
llm_model_path: "models/phi-2.Q4_K_M.gguf"
```

---

### 3. Run the App

```bash
python app.py
```

---

## 🧠 How It Works

1. You paste your resume and a job description into the UI.
2. The app segments your resume into logical parts (Experience, Skills, etc.).
3. Each section is rewritten via the local LLM to better match the job.
4. Output is streamed live into the GUI, section-by-section.

---

## 🔗 Download Model

This app uses a local LLM: `Llama-3.2-3B-Instruct-Q4_0.gguf`.

Due to GitHub's 100MB file limit, you need to manually download the model:

## 🔒 Privacy Focused

This project is 100% local:

- No OpenAI, Anthropic, or any cloud API is used
- No internet connection required
- Your data stays on your device

---

## 📌 TODO / Improvements

- [ ] PDF/Docx import and export
- [ ] Manual section editing pre/post rewrite
- [ ] Scoring (ATS-style compatibility meter)
- [ ] Light/Dark mode toggle

---

## 🧑‍💻 Author

Ahmad | [XZOTECHX](https://github.com/xzotechx)

---

## 📜 License

MIT License

```

Would you like me to save this as a downloadable `.md` file now?
```
