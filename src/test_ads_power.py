import time
import pandas as pd
from adspower import AdsPower
from selenium.webdriver.common.by import By


def read_fil(file_name: str = 'browser_data.xlsx'):
    data = pd.read_excel(file_name)
    browser_ids = data['browser_ids'].dropna().values
    urls = data['links'].dropna().values

    return browser_ids, urls


def make_action(driver):
    print(driver.title)
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(5)
    driver.execute_script('window.scrollBy(0, 500);')
    time.sleep(5)
    driver.find_element(By.TAG_NAME, 'body')


def imit_action_on_sits():
    browser_ids, urls = read_fil()

    for browser_id in browser_ids:
        ads_power = AdsPower(browser_id)

        with ads_power as driver:
            for url in urls:
                driver.execute_script(f"window.open('https://www.avito.ru/');")
                time.sleep(5)
                make_action(driver)
                # driver.execute_script(f"window.open('{urls}');")
                # time.sleep(15)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(10)


def by_cript():
    pass


if __name__ == '__main__':
    imit_action_on_sits()
    # print(f'[0] Имитация работы с сайтами\n'
    #       f'[1] Авто-покупка крипты')
    #
    # event = input('Выберите действие: ')
    #
    # if event == '0':
    #     print('Имитация работы с сайтами')
    # elif event == '1':
    #     print('Авто-покупка крипты')
