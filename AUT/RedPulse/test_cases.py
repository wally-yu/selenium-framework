'''
Created on 2013-5-9

@author: wally
'''
import time
import settings
from AUT.RedPulse.actions import LandingHome, Login
from selenium_framework.utils import start_browser, close_browser


def SmokeTest(url):

    # Start Browser
    driver = start_browser(url)
    time.sleep(settings.T_MINI)

    # Actions
    landing_action_obj = LandingHome()
    landing_action_obj.landing_home(driver)
    landing_action_obj.nagivate_to_login(driver)

    Login().login(driver, 'testing@redpulse.com', '123')

    # Close Browser
    close_browser(driver)