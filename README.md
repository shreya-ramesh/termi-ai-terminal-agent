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
##  Project Structure
<pre>
Termi/
├── config/
│   └── env.py                # Loads .env and Groq API key
│
├── core/                     # Core agent logic
│   ├── agent.py              # Handles prompt parsing and mode logic
│   ├── error_explainer.py    # LLM-based error explanation
│   ├── executor.py           # Runs shell commands
│   ├── explainer.py          # Command explanation module
│   ├── intent.py             # Maps intent to command
│   ├── memory.py             # Persistent memory manager
│   └── settings.py           # settings logic
│
├── db/
│   └── history.json          # Persistent prompt-command history
│
├── README.md                
├── main.py                   # Main terminal assistant logic
├── requirements.txt
└── settings.json             # mode setup
</pre>

## Quick Setup

Clone the repository:
```bash
git clone https://github.com/your-username/Termi.git
cd Termi
```
Set up your environment:
```bash
cp .env.example .env
```
Then open .env and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
Launch the assistant:
```bash
python3 main.py
```
---
## Contact
For queries or collaborations: shreya.ramesh22@gmail.com

