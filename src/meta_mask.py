import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

base_url = 'http://local.adspower.net:50325/'


def open_browser(browser_id):
    endpoint = 'api/v1/browser/start'

    params = {
        'user_id': browser_id,
    }

    response = requests.get(
        base_url + endpoint,
        params=params
    )
    if response.status_code == 200:
        return response.json()
    else:
        print('error')
        return False


def close_browser(browser_id):
    endpoint = 'api/v1/browser/stop'

    params = {
        'user_id': browser_id,
    }

    response = requests.get(
        base_url + endpoint,
        params=params
    )
    if response.status_code == 200:
        return response.json()
    else:
        print('error')
        return False


def get_driver(browser_id: str) -> webdriver.Chrome:
    data = open_browser(browser_id)

    print(data)

    debug_address_selenium = data['data']['ws']['selenium']
    debug_address_puppeteer = data['data']['ws']['puppeteer']
    driver_pass = data['data']['webdriver']

    options = webdriver.ChromeOptions()
    options.add_extension('MetaMask_Chrome.crx')
    options.add_experimental_option('debuggerAddress', debug_address_selenium)
    service = Service(executable_path=driver_pass)

    driver = webdriver.Chrome(service=service, options=options)

    return driver


javascript = """
var buttons = document.getElementsByTagName('button');
var inputElement  = document.getElementById('password');

inputElement.value = '123;

for (var i = 0; i < buttons.length; i++) {
    if (buttons[i].textContent == 'Разблокировать') {
        buttons[i].click();
        break;
    }

}
"""


def main(b_id='jd6u9gy'):
    driver = get_driver(b_id)

    while True:
        time.sleep(10)

        print(driver.window_handles)

        driver.switch_to.window(driver.window_handles[-1])
        print(driver.page_source)
        print('<' * 10 + str(driver.title) + '>' * 10)
        try:
            print('=' * 10)
            password_field = driver.find_element(By.ID, 'password')
            password_field.send_keys('123')
            btn = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button')
            btn.click()
        except Exception as e:
            print(e)

    # close_browser(b_id)


# https://www.youtube.com/watch?v=BEqc2wEX3iY

if __name__ == '__main__':
    main()
