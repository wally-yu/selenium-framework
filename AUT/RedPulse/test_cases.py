'''
Created on 2013-5-9

@author: wally
'''
import time
import settings
from AUT.RedPulse.actions import LandingHome, Login
from selenium_framework.utils import start_browser, close_browser
from selenium_framework.web_browser import set_window_position, switch_current_window_to_front


def SmokeTest(url):

    # Start Browser
    driver = start_browser(url)
    time.sleep(settings.T_MINI)

    # Actions
    landing_action_obj = LandingHome()
    landing_action_obj.landing_home(driver)
    landing_action_obj.nagivate_to_login(driver)

    Login().login(driver, 'testing@redpulse.com', '<somepassword>')

    # Close Browser
    close_browser(driver)


def MultiUserInteractionDemo(url):
    # Start Browser and Login with Normal User
    driver_normal_user = start_browser(URL=url,
                                       brower_driver_location=settings.DRIVER_PATH_CHROME_MAC)
    time.sleep(settings.T_MINI)
    set_window_position(0, 0, driver_normal_user)
    landing_action_obj = LandingHome()
    landing_action_obj.landing_home(driver_normal_user)

    # Start Browser and Login with supervisor
    driver_supervisor = start_browser(URL=url,
                                       brower_driver_location=settings.DRIVER_PATH_CHROME_MAC)
    time.sleep(settings.T_MINI)
    set_window_position(200, 200, driver_supervisor)
    landing_action_obj.landing_home(driver_supervisor)

    # Normal user login
    switch_current_window_to_front(driver_normal_user)
    landing_action_obj.nagivate_to_login(driver_normal_user)
    Login().login(driver_normal_user, 'testing@redpulse.com', '<somepassword>')

    # supervisor login
    switch_current_window_to_front(driver_supervisor)
    landing_action_obj.nagivate_to_login(driver_supervisor)
    Login().login(driver_supervisor, 'test@red-pulse.com', '<somepassword>')

    # Close Browser
    close_browser(driver_normal_user)
    close_browser(driver_supervisor)