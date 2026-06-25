# 🔐 Password Checker CLI

A terminal-based password strength analyzer built with **Python**, **Typer**, and **Rich**.

This CLI tool analyzes password strength using **entropy-based calculations**, character diversity checks, and provides security recommendations with a beautiful colored terminal interface.

---

## ✨ Features

- 🔑 Password strength analysis
- 📊 Entropy score calculation
- 🔠 Character diversity breakdown
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Punctuation
  - Spaces
- 🎨 Rich terminal UI with:
  - Colored output
  - Tables
  - Progress bars
- ⚙️ YAML-based configuration for themes
- 💻 Installable CLI tool

---

## 🛠 Tech Stack

- Python 3.10+
- Typer — CLI framework
- Rich — Beautiful terminal UI
- PyYAML — Configuration management

---

## 📂 Project Structure

```bash
PasswordSecurity/
│
├── password_checker/
│   ├── __init__.py
│   ├── main.py
│   └── rich_config.yaml
│
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/password-checker-cli.git
cd password-checker-cli
```

---

### 2. Create virtual environment

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -e .
```

This installs the project in **editable mode**, so any changes to source files immediately reflect in the CLI.

---

## ▶️ Usage

### Run interactive mode

```bash
password-checker
```

You’ll be prompted to enter passwords repeatedly until you choose to exit.

---

### Run once

```bash
password-checker --once
```

This checks only one password and exits.

---

## 📸 Example Output

```bash
===== 🔑 Welcome to Password Strength Checker 🔑 =====

Enter your password:
Analyzing password... ████████████████████ 100%

┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Metric           ┃ Value    ┃
┣━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━┫
┃ Lowercase        ┃ 5        ┃
┃ Uppercase        ┃ 2        ┃
┃ Numbers          ┃ 3        ┃
┃ Punctuation      ┃ 1        ┃
┃ Spaces           ┃ 0        ┃
┃ Entropy Score    ┃ 74.32    ┃
┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━┛

Strong: Hard to guess, good password.
```

---

## 🧠 How Strength is Calculated

The tool estimates password strength using **entropy**:

```text
Entropy = Password Length × log₂(Character Set Size)
```

Character set size depends on which character categories are used:

- Lowercase letters → 26
- Uppercase letters → 26
- Digits → 10
- Punctuation → ~32
- Spaces → 1

Higher entropy generally means better resistance against brute-force attacks.

---

## 🎨 Configuration

Theme customization is stored in:

```bash
password_checker/rich_config.yaml
```

Example:

```yaml
theme:
  primary: bold blue
  success: green
  warning: yellow
  error: red
```

You can modify colors and styles easily.

---

## 🔮 Future Improvements

Planned features:

- Password generation mode
- Breach detection via HaveIBeenPwned API
- Export reports as JSON / CSV
- Better entropy estimation
- Unit tests
- Publish to PyPI

---

## 🤝 Contributing

Contributions are welcome.

Feel free to:
- Open issues
- Suggest features
- Submit pull requests

---

## 👨‍💻 Author

Built by **Dhrubajit Chakravarty**  
Computer Science Engineer | Backend Developer | Cybersecurity Enthusiast

GitHub: https://github.com/Dhrubajit-cmd

---

## 📜 License

MIT License