'''
Created on 2013-5-9

@author: wally
'''
from selenium_framework import web_element
from selenium_framework.web_element import identifier
from selenium_framework.utils import BasePage


class LoginPage(BasePage):

    txt_user_name = web_element.WebEdit(identifier.xpath, "//input[@placeholder='Email']", 'email address')
    txt_password = web_element.WebEdit(identifier.name, "password", 'password')
    chk_remember_me = web_element.WebCheckbox(identifier.id, 'checkbox1', 'remember me')
    btn_login = web_element.WebButton(identifier.xpath, "//button[@type='submit']", 'Login' )


class HomePage(BasePage):

    btn_signin = web_element.WebButton('css', '.landing-header__signin__btn', 'Sign In Button')
    mp4_background = web_element.WebPicture('css', 'video', 'Background video')


class ListingPage(BasePage):

    txt_report_titles = web_element.WebGeneral('css', '.report-title', 'Report Titles')