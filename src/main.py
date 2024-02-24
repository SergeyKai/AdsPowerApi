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


def make_action(driver):
    print(driver.title)
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(5)
    driver.find_element(By.TAG_NAME, 'body')
    time.sleep(5)


def get_driver(browser_id: str) -> webdriver.Chrome:
    data = open_browser(browser_id)

    print(data)

    debug_address_selenium = data['data']['ws']['selenium']
    debug_address_puppeteer = data['data']['ws']['puppeteer']
    driver_pass = data['data']['webdriver']

    options = webdriver.ChromeOptions()
    options.add_experimental_option('debuggerAddress', debug_address_selenium)
    service = Service(executable_path=driver_pass)

    driver = webdriver.Chrome(service=service, options=options)

    return driver


def read_fil(file_name: str = 'browser_data.xlsx'):
    data = pd.read_excel(file_name)
    browser_ids = data['browser_ids'].dropna().values
    urls = data['links'].dropna().values

    return browser_ids, urls


def imit_action_on_sits():
    browser_ids, urls = read_fil()

    for browser_id in browser_ids:
        driver = get_driver(browser_id)
        for url in urls:
            driver.get(url)
            time.sleep(5)
            make_action(driver)
            driver.execute_script(f"window.open('', '_blank');")
            print(driver.title)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(5)

        win_met = filter(lambda win: win.title() == 'MetaMask Notification', driver.window_handles[-1])
        win_met.title()
        driver.close()
        close_browser(browser_id)


def bue_cript():
    browser_ids, urls = read_fil()

    for browser_id in browser_ids:
        driver = get_driver(browser_id)


def main():
    print(f'[0] Имитация работы с сайтами\n'
          f'[1] Авто-покупка крипты')

    event = input('Выберите действие: ')

    if event == '0':
        print('Имитация работы с сайтами')
        imit_action_on_sits()
    elif event == '1':
        print('Авто-покупка крипты')
        bue_cript()


if __name__ == '__main__':
    main()
