from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_title():
    driver = webdriver.Chrome()

    driver.get("file:///C:/Users/LAXMI SUNAGAR/Desktop/devops-project/index.html")

    time.sleep(5)

    # 👇 wait until alert appears
    try:
        wait = WebDriverWait(driver, 5)
        alert = wait.until(EC.alert_is_present())

        print("Alert found:", alert.text)
        alert.accept()

    except:
        print("No alert found")

    time.sleep(1)

    assert "DevOps" in driver.page_source

    driver.quit()
