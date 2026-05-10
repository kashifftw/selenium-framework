from selenium.webdriver.common.by import By
import time
import os

os.makedirs("screenshots", exist_ok=True)

def test_github_search(driver):        # ← driver fixture
    driver.get("https://github.com/search?q=python&type=repositories")
    time.sleep(5)

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

    results = driver.find_elements(By.CSS_SELECTOR, '[data-testid="results-list"] > div')
    print("Results Found:", len(results))

    driver.save_screenshot("screenshots/github_results.png")
    print("Screenshot Saved")

    assert "python" in driver.current_url.lower()