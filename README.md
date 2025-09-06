# ⚽ Football Match Data Web Scraper

A Python script to automatically scrape football match data and save it to a CSV file.

---

## 📖 Overview

This project contains a Python script that automates the process of scraping football match data from the detailed statistics page on [adamchoi.co.uk](http://www.adamchoi.co.uk/).

The script performs the following:

- Navigates to the website.
- Clicks the **"All matches"** button to load the full match dataset.
- Extracts match details including **Date**, **Home Team**, **Score**, and **Away Team**.
- Saves the structured data to a CSV file for further analysis.

---

## ✨ Features

- 🤖 **Automated Browsing**: Uses Selenium to control a Chrome browser instance.
- ⏳ **Dynamic Content Handling**: Waits for JavaScript content to load before interacting.
- 📊 **Data Extraction**: Extracts and parses match details from an HTML table.
- 📄 **Structured Output**: Outputs clean data into a `match_data.csv` file.
- ⚙️ **Automatic Driver Management**: Utilizes Selenium Manager to handle ChromeDriver installation and versioning.

---

## 🛠️ Technology Stack

- **Language**: Python 3
- **Library**: Selenium

---

## 🚀 Getting Started

Follow these instructions to set up and run the scraper on your local machine.

### ✅ Prerequisites

- Python 3.x installed on your system.
- Google Chrome browser installed.

### 📦 Installation & Setup

1. **Clone the repository** (or download `main.py` directly).

2. **Install the required Python package**:

   ```bash
   pip install selenium


## ▶️ Running the Scraper

1. Navigate to the project directory:

   ```bash
   cd path/to/your/project
   ```

2. Run the script:

   ```bash
   python main.py
   ```

The script will open a Chrome browser window, perform the scraping, and print progress messages to your terminal.

---

## 📄 Output

After successful execution, a CSV file named `match_data.csv` will be generated in your project directory.

### 🧾 Example Output:

```csv
Date,Home Team,Score,Away Team
13-08-2023,Brentford,2 - 2,Tottenham
12-08-2023,Bournemouth,1 - 1,West Ham
...
```

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---


## 💬 Acknowledgments

Thanks to [adamchoi.co.uk](http://www.adamchoi.co.uk/) for providing the football match data used in this project.

```

---

Let me know if you'd like a version with GitHub-style badges, Docker support, or more advanced setup instructions.
```
