# 🤖 Termi

Termi is a terminal-based AI assistant that converts natural language into executable shell commands using the Groq API (LLaMA3). It offers a smart, interactive CLI experience.

---

## Features

- Converts natural language into shell commands
- Supports command history, editing, retry, and autorun
- Explains shell commands and errors using LLM
- Enhanced terminal UI with Rich library
- Beginner-friendly, safe, and extensible

---

## Platform Support

- Linux (Ubuntu recommended)
- Works on Windows **only via WSL (Windows Subsystem for Linux)**
- Not supported on native Windows or macOS (yet)

---

## Quick Setup

```bash
git clone https://github.com/your-username/Termi.git
cd Termi
pip install -r requirements.txt
cp .env.example .env   # Add your Groq API key to this file
python3 main.py
