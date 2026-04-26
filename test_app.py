from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def test_title():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # 👇 get correct path dynamically
    file_path = os.path.abspath("index.html")
    driver.get("file://" + file_path)

    assert "DevOps" in driver.page_source

    driver.quit()