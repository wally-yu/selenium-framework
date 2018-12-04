import time
import uuid
import shutil
import os
from platform import platform
from selenium import webdriver
from selenium_framework.common import prt
import settings

_tmp_folder = '/tmp/{}'.format(uuid.uuid4())


class BasePage():
    def __init__(self):
        self.__page_name = self.__class__.__name__
        prt(3, '## Page: %s ##' % self.__page_name)


class BaseAction():
    """ Base Action is just to print some stuffs"""
    def __init__(self):
        self.__action_name = self.__class__.__name__
        prt(2, 'Current Action: %s' % self.__action_name, True)


def start_browser(URL, browserType='chrome', brower_driver_location=settings.DRIVER_PATH_CHROME_MAC):
    prt(0, 'Stated to Open Browser %s' % browserType.upper())
    if browserType.upper() == 'FIREFOX':
        driver = webdriver.Firefox()
    elif browserType.upper() == 'CHROME':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = settings.DRIVER_PATH_CHROME

        if not os.path.exists(_tmp_folder):
            os.makedirs(_tmp_folder)

        if not os.path.exists(_tmp_folder + '/user-data'):
            os.makedirs(_tmp_folder + '/user-data')

        if not os.path.exists(_tmp_folder + '/data-path'):
            os.makedirs(_tmp_folder + '/data-path')

        if not os.path.exists(_tmp_folder + '/cache-dir'):
            os.makedirs(_tmp_folder + '/cache-dir')

        if 'Darwin' in platform():
            chrome_driver_location = settings.DRIVER_PATH_CHROME_MAC
            driver = webdriver.Chrome(chrome_driver_location)
        elif 'Linux' in platform():
            # Designed for headless like aws lambda
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1280x1696')
            chrome_options.add_argument('--user-data-dir={}'.format(_tmp_folder + '/user-data'))
            chrome_options.add_argument('--hide-scrollbars')
            chrome_options.add_argument('--enable-logging')
            chrome_options.add_argument('--log-level=0')
            chrome_options.add_argument('--v=99')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument('--data-path={}'.format(_tmp_folder + '/data-path'))
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--homedir={}'.format(_tmp_folder))
            chrome_options.add_argument('--disk-cache-dir={}'.format(_tmp_folder + '/cache-dir'))
            chrome_options.add_argument(
                'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
            driver = webdriver.Chrome(chrome_options=chrome_options)
        else:
            raise Exception('which environment is it?')
    else:
        raise RuntimeError('Browser Type is not correct!')
    driver.implicitly_wait(30)
    if URL != "":
        driver.get(URL)
    time.sleep(settings.T_MINI)
    return driver


def close_browser(driver):
    prt(0, 'Close Browser, Test End')
    # Close webdriver connection
    driver.quit()

    # Remove specific tmp dir of this "run"
    try:
        shutil.rmtree(_tmp_folder)
    except:
        # silent pass
        pass

    # Remove possible core dumps
    folder = '/tmp'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if 'core.headless-chromi' in file_path and os.path.exists(file_path) and os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)