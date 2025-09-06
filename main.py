import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Configuration ---
WEBSITE_URL = "https://www.adamchoi.co.uk/teamgoals/detailed"
OUTPUT_FILE = "match_data.csv"


def run_scraper():
    """
    Initializes the web driver, scrapes the data, and handles cleanup.
    """
    # Let Selenium Manager handle the driver. No more manual paths or Service objects.
    # This automatically solves version mismatch and timeout issues.
    print("Initializing WebDriver...")
    driver = webdriver.Chrome()

    try:
        print(f"Navigating to {WEBSITE_URL}...")
        driver.get(WEBSITE_URL)

        # Use WebDriverWait to reliably wait for elements to be ready.
        # This is better than time.sleep() as it waits only as long as needed.
        wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds

        print("Waiting for the 'All matches' button and clicking it...")
        all_matches_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//label[@analytics-event="All matches"]'))
        )
        all_matches_button.click()

        # Wait for the table to update after the click
        time.sleep(1)  # A small static wait can be useful here for the table to re-render

        print("Scraping the match data from the table...")
        # Select all table rows 'tr' within the 'tbody' to exclude the header
        match_rows = driver.find_elements(By.CSS_SELECTOR, "table.table-bordered tbody tr")

        scraped_data = []
        for row in match_rows:
            # Get all cells 'td' in the current row
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) > 3:  # Make sure it's a row with match data
                date = cells[0].text
                home_team = cells[1].text
                score = cells[2].text
                away_team = cells[3].text

                # Store data in a dictionary for clarity
                match_info = {
                    "Date": date,
                    "Home Team": home_team,
                    "Score": score,
                    "Away Team": away_team
                }
                scraped_data.append(match_info)
                print(f"  - Scraped: {home_team} vs {away_team}")

        # Save the scraped data to a CSV file
        if scraped_data:
            with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=scraped_data[0].keys())
                writer.writeheader()
                writer.writerows(scraped_data)
            print(f"\nSuccess! Saved {len(scraped_data)} matches to '{OUTPUT_FILE}'.")
        else:
            print("Could not find any match data to scrape.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        # Crucial: Always close the browser to free up resources.
        print("Closing the browser.")
        driver.quit()


# Run the scraper
if __name__ == "__main__":
    run_scraper()

