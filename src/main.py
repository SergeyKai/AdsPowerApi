import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'http://local.adspower.net:50325/'


def open_browser(browser_id='jd6u9gy'):
    endpoint = 'api/v1/browser/start'

    api_key = 'c2e4b7646046674561f4f975757cccc0'

    params = {
        'user_id': browser_id,
    }

    response = requests.get(
        url + endpoint,
        params=params
    )
    if response.status_code == 200:
        return response.json()
    else:
        print('error')
        return False


def close_browser(browser_id='jd6u9gy'):
    endpoint = 'api/v1/browser/stop'

    params = {
        'user_id': browser_id,
    }

    response = requests.get(
        url + endpoint,
        params=params
    )
    if response.status_code == 200:
        return response.json()
    else:
        print('error')
        return False


def create_request(driver, url):
    driver.get(url)


def main(browser_id: str = None):
    data = open_browser(browser_id)

    print(data)

    debug_address_selenium = data['data']['ws']['selenium']
    debug_address_puppeteer = data['data']['ws']['puppeteer']
    driver_pass = data['data']['webdriver']

    options = webdriver.ChromeOptions()
    options.add_experimental_option('debuggerAddress', debug_address_selenium)
    service = Service(executable_path=driver_pass)

    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')

    time.sleep(10)

    close_browser(browser_id)


if __name__ == '__main__':
    main('jd6u9gy')
