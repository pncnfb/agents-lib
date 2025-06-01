# 🧠 AGENTS-LIB

**AGENTS-LIB** is a personal playground and evolving Python library to test and integrate various tools developed by startups, and to experiment with LLMs from multiple providers.
This project is currently **a work in progress**.

## 📁 Project Structure
- `agents/` → Custom agents (e.g., weather, search)
- `controller/` → (Planned) Logic to coordinate agents and LLMs
- `llms/` → Interfaces for LLM providers (like Google, Anthropic)
  - `creds/` → API keys and credential files
- `models/` → Core logic and helper functions

## 🧪 Setup Instructions

This project uses [uv](https://github.com/astral-sh/uv) for Python environment and dependency management.

### 1. Install `uv`

```bash
brew install uv
```

### 2. Create a virtual environment with Python 3.12
```bash
uv venv --python=3.12
```

### 3. Install dependencies in editable mode
```bash
uv pip install -e .
```

### 4. Activate the virtual environment
```bash
source .venv/bin/activate
```

### 5. Configure credentials and settings
Copy the example config file and set your own credentials and parameters:
```bash
cp config.ini.example config.ini
```

## 🛠️ Features (WIP)
* Modular agents (e.g., weather, search)
* LLM integration (Google, Anthropic, and others)
* Extensible controller architecture
* Easily pluggable for new experiments

## 📌 Notes
This repo is not production-ready.

It serves as an experimental sandbox for learning and integrating new tools.