# Day 51 - Internet Speed Twitter Complaint Bot 🚀

## Overview

This project is part of the **100 Days of Python Bootcamp**.

The program automatically:

1. Measures your internet download and upload speeds using **Speedtest.net**.
2. Logs into a social media website.
3. Compares your actual internet speed with your promised speed.
4. Creates a complaint message if your internet speed is lower than expected.

---

## Technologies Used

* Python 3
* Selenium WebDriver
* ChromeDriver
* Explicit Waits (`WebDriverWait`)
* Object-Oriented Programming (OOP)

---

## Features

* Automated browser interaction
* Speed testing with Speedtest.net
* Dynamic message generation
* Login automation
* Conditional logic based on internet speeds
* Web scraping and browser automation

---

## Project Structure

```text
InternetSpeedTwitterBot
│
├── get_internet_speed()
│   ├── Open Speedtest.net
│   ├── Run speed test
│   └── Store download/upload speeds
│
├── run_automation()
│   ├── Open website
│   ├── Login with credentials
│   └── Prepare for posting
│
└── tweet_at_provider()
    ├── Compare actual speed vs promised speed
    ├── Generate message
    └── Submit post
```

---

## Example Output

```text
Down: 845.62
Up: 912.41

Hey my internet provider, I'm seeing
845.62 down / 912.41 up,
but I pay for 1000/1000.
Can you help?
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/day-51-internet-speed-bot.git
cd day-51-internet-speed-bot
```

Install dependencies:

```bash
pip install selenium
```

Download and install:

* Google Chrome
* ChromeDriver compatible with your Chrome version

---

## Running the Project

```bash
python main.py
```

---

## What I Learned

* Using Selenium for browser automation
* Waiting for elements with `WebDriverWait`
* Working with dynamic websites
* Building automation scripts with OOP
* Using conditional logic to generate automated messages
* Handling exceptions in Selenium projects

---

## Challenges

* Dynamic websites frequently change their HTML structure.
* Login systems may include bot detection or CAPTCHA.
* Hardcoded selectors can break when websites update.

---

## Future Improvements

* Use environment variables for credentials.
* Replace `time.sleep()` with more explicit waits.
* Add screenshots for debugging.
* Add logging instead of print statements.
* Support multiple internet providers.
* Export speed test history to a CSV file.

---

## Disclaimer

This project was created for educational purposes as part of the **100 Days of Python Bootcamp**. Website structures and automation policies may change over time, causing parts of the script to stop working.

---

Made with ❤️ and Python.
