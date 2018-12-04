'''
Created on 2013-5-9
@author: wally
'''
from AUT.RedPulse.pages import LoginPage, ListingPage, HomePage
from selenium_framework.web_browser import delete_all_cookies
from selenium_framework.reporting import reporting
from selenium_framework.utils import BaseAction


class LandingHome(BaseAction):

    @staticmethod
    def landing_home(driver):
        homepage_obj = HomePage()
        pass_creteria = homepage_obj.mp4_background.if_exist(driver) and homepage_obj.btn_signin.if_exist(driver)
        reporting(pass_creteria_bool=pass_creteria,
                  expectation_txt='Check background video and sign in button')

    @staticmethod
    def nagivate_to_login(driver):
        homepage_obj = HomePage()
        homepage_obj.btn_signin.click(driver)

        login_page_obj = LoginPage()
        pass_creteria = login_page_obj.btn_login.if_exist(driver)
        reporting(pass_creteria,
                  'Login button should exist')


class Login(BaseAction):

    def login(self, driver, username, password):

        delete_all_cookies(driver)

        self._login(driver, username, password)

        listing_page_obj = ListingPage()

        pass_creteria = listing_page_obj.txt_report_titles.if_exist(driver, None, 5)
        reporting(pass_creteria_bool=pass_creteria,
                  expectation_txt='Should navigate to Listing page')

    @staticmethod
    def _login(driver, user_name, psw):
        login_page_obj = LoginPage()
        login_page_obj.txt_user_name.set_txt(driver, user_name)
        login_page_obj.txt_password.set_txt(driver, psw)
        login_page_obj.chk_remember_me.uncheck(driver)
        login_page_obj.btn_login.click(driver)



