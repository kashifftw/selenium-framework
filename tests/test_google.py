from selenium import webdriver
import time

# Open Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait 5 seconds
time.sleep(5)

# Close browser
driver.quit()