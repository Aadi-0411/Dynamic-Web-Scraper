from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.adamchoi.co.uk/teamgoals/detailed"
# The path to your chromedriver executable
path = '/Users/aadityapatil/Downloads/chromedriver-mac-arm64/chromedriver'

# Create a Service object with the executable path
service = Service(executable_path=path)

# Pass the service object to the Chrome driver
driver = webdriver.Chrome(service=service)

driver.get(website)

# Remember to quit the driver when you're done
driver.quit()