from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

os.makedirs("screenshots", exist_ok=True)

def test_scenario_a_search(driver):    # ← driver fixture
    driver.get("https://www.wikipedia.org")
    time.sleep(3)
    search = driver.find_element(By.ID, "searchInput")
    search.send_keys("Python programming language")
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    heading = driver.find_element(By.ID, "firstHeading").text
    print("Article Heading:", heading)
    driver.save_screenshot("screenshots/wikipedia_python_article.png")
    assert "python" in heading.lower()

def test_scenario_b_homepage(driver):  # ← driver fixture
    driver.get("https://www.wikipedia.org")
    time.sleep(3)
    title = driver.title
    print("Page Title:", title)
    driver.save_screenshot("screenshots/wikipedia_homepage.png")
    assert "wikipedia" in title.lower()

def test_scenario_c_selenium_article(driver):  # ← driver fixture
    driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")
    time.sleep(3)
    paragraphs = driver.find_elements(By.CSS_SELECTOR, ".mw-parser-output > p")
    first_para = ""
    for para in paragraphs:
        if para.text.strip():
            first_para = para.text.strip()
            break
    print("First Paragraph Preview:")
    print(first_para[:150])
    driver.save_screenshot("screenshots/wikipedia_selenium_article.png")
    assert "selenium" in first_para.lower()