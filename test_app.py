from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def test_title():
    options = Options()
    options.add_argument("--headless=new")   # important
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 👇 use system chromedriver (GitHub provides it)
    service = Service()

    driver = webdriver.Chrome(service=service, options=options)

    # 👇 works both locally + GitHub
    file_path = os.path.abspath("index.html")
    driver.get("file://" + file_path)

    assert "DevOps" in driver.page_source

    driver.quit()