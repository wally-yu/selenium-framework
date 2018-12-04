'''
Created on 2012-12-28

@author: wally
'''

from selenium_framework.common import prt


def maxmize(driver):
    prt(3, 'Maxmize Browser')
    driver.maximize_window()


def set_window_position(x, y, driver):
    driver.set_window_position(x, y)
    prt(3, 'Set Window Position to: X - %s; Y - %s' % (x, y))


def set_window_size (width, height, driver):
    driver.set_window_size(width, height)
    prt(3, 'Set Window Size to: Width - %s; Height - %s' % (width, height))


def switch_to_window(driver, window_name):
    driver.switch_to_window(window_name)
    prt(3, 'Switch to Window: %s' % window_name)


def switch_to_frane(driver, frameName):
    driver.switch_to_frame(frameName)


def switch_current_window_to_front(driver):
    driver.switch_to_window(driver.current_window_handle)


def swith_to_alert(driver):
    driver.browser.switch_to_alert()
    prt(3, 'Switch to Alert on Browser')


def get_page_source(driver):
    prt(3, 'Get Page Source')
    return driver.page_source


def get_current_url(driver):
    prt(2, 'Get Current URL')
    return driver.current_url()


def refresh(driver):
    prt(3, 'Refresh Current Page')
    driver.refresh()


def delete_all_cookies(driver):
    prt(3, 'Delete All Cookies')
    driver.delete_all_cookies()


def save_screen_shot_as_base64(driver):
    return driver.get_screenshot_as_base64()


def save_screen_shot_as_file(driver, file_path):
    driver.get_screenshot_as_file(file_path)

