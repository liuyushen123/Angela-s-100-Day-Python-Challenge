# 🏠 Zillow Web Scraping & Google Forms Automation

A Python automation project that scrapes rental property listings from a Zillow clone website using **BeautifulSoup** and automatically submits each listing into a **Google Form** using **Selenium WebDriver**.

The project demonstrates a complete data collection pipeline: **Web Scraping → Data Cleaning → Browser Automation → Google Sheets**.

---

## ✨ Features

- Scrape all rental listings from the App Brewery Zillow Clone
- Extract
  - Property Address
  - Rental Price
  - Listing URL
- Clean scraped data
  - Remove `$`, commas, `/mo`, `+`, `1 bd`, etc.
  - Format addresses by removing unnecessary separators and whitespace
- Automatically fill out a Google Form
- Submit every property as a separate response
- Store all responses inside Google Sheets

---

## 🛠 Technologies

- Python 3
- Requests
- BeautifulSoup4
- Selenium
- ChromeDriver
- Google Forms

---

## 📁 Project Structure

```text
Day53/
│
├── driver_setup.py
├── config.py
├── main.py
│
├── pages/
│   ├── zillow_page.py
│   └── form_page.py
│
└── README.md
```

---

## 🚀 How It Works

### Step 1

Scrape rental listings from the Zillow Clone website.

```text
https://appbrewery.github.io/Zillow-Clone/
```

---

### Step 2

Extract the following information from every listing:

- Address
- Price
- Listing URL

Example:

```python
{
    "address": "300 Buchanan St #202, San Francisco, CA",
    "price": "2975",
    "link": "https://www.zillow.com/..."
}
```

---

### Step 3

Clean the scraped data.

Example transformations:

| Raw | Clean |
|------|-------|
| `$2,975+/mo` | `2975` |
| `$2,809+ 1 bd` | `2809` |
| `300 Buchanan \| San Francisco` | `300 Buchanan San Francisco` |

---

### Step 4

Open a Google Form.

---

### Step 5

Automatically enter

- Address
- Price
- Link

using Selenium.

---

### Step 6

Submit the form.

Repeat until every listing has been submitted.

---

## 📸 Example Output

| Address | Price | Link |
|----------|------:|------|
| 300 Buchanan St | 2975 | Zillow Link |
| SoMa Square | 2809 | Zillow Link |
| Palace Court Apartments | 1745 | Zillow Link |

Every submission is automatically recorded in Google Sheets.

---

## 🧠 Skills Demonstrated

- Object-Oriented Programming (OOP)
- Page Object Model (POM)
- Web Scraping
- HTTP Requests
- HTML Parsing
- Selenium Automation
- Explicit Waits
- Data Cleaning
- Project Organization

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/zillow-web-scraper.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 📚 What I Learned

This project combines multiple Python libraries to build an end-to-end automation workflow.

Key takeaways include:

- Building reusable Page Objects
- Cleaning inconsistent scraped data
- Using BeautifulSoup for parsing HTML
- Automating Google Forms with Selenium
- Working with explicit waits instead of fixed delays
- Structuring a medium-sized Python project for maintainability

---

## 🙏 Credits

Project inspired by the **100 Days of Code: Python Bootcamp** by **Dr. Angela Yu**.

The Zillow website used in this project is a practice clone provided for educational purposes.