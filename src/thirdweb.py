from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    driver = webdriver.Chrome()

    url = 'https://zoraname.domains/?ref=0xcbF4e2115ab017cbDE3106Af6F47a94568687a19'

    driver.get(url)
    time.sleep(5)

    btn = driver.find_element(By.XPATH, '//*[@id="main_button"]')

    btn.click()

    time.sleep(5)

    window = driver.find_element(By.XPATH, '/html/body/w3m-modal//wui-flex/wui-card')

    print(window)


if __name__ == '__main__':
    main()
