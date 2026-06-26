# 🍞 Share-a-Naan Automation Bot

A Selenium-based automation bot that can automatically follow and unfollow users on the Share-a-Naan platform. This project is built using the Page Object Model (POM) design pattern and includes logging, explicit waits, and modular page objects.

## Features

* 🔐 Automated login
* 👥 Follow followers of target accounts
* ❌ Unfollow followed users
* 📜 Detailed logging to file and console
* 🏗️ Page Object Model architecture
* ⏳ Explicit waits with `WebDriverWait`
* 📸 Automatic screenshots on failures

## Project Structure

```text
Day 52/
│
├── config.py
├── driver_setup.py
├── main.py
├── logs/
│   └── naan_bot.log
└── pages/
    ├── base_page.py
    ├── login_page.py
    └── home_page.py
```

## Technologies Used

* Python 3.12
* Selenium
* webdriver-manager
* Logging Module

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/share-a-naan-bot.git
cd share-a-naan-bot
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the bot:

```bash
python main.py
```

The program will ask:

```text
Would you like to follow(y) or unfollow(n)?
```

Choose:

* `y` → Follow users
* `n` → Unfollow users

## Configuration

Edit `config.py`:

```python
SIMILAR_ACCOUNTS = [
    "account1",
    "account2",
    "account3",
]
```

## Future Improvements

* Store credentials in environment variables
* Add configuration file support
* Add retry mechanisms
* Add headless mode
* Add unit tests with pytest
* Add GitHub Actions CI/CD

## Disclaimer

This project was built for educational purposes to practice Selenium automation and the Page Object Model design pattern.
