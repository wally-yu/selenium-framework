'''
Created on 2012-12-28

@author: wally
'''

from selenium_framework.common import prt

def maxmize(driver):
    prt(3, 'Maxmize Browser')
    driver.maximize_window()
    
def setWindowPosition(x, y, driver):
    windowHandle = driver.current_window_handle()
    driver.set_window_position(x, y, windowHandle)
    prt(3, 'Set Window Position to: X - %s; Y - %s' % str(x), str(y))

def setWindowSize (width, height, driver):
    windowHandle = driver.current_window_handle()
    driver.set_window_size(width, height, windowHandle)
    prt(3, 'Set Window Size to: Width - %s; Height - %s' % str(width), str(height))
    
def swithToWindow(driver, windowName):
    driver.switch_to_window(windowName)
    prt(3, 'Switch to Window: %s' % str(windowName))

def switchToFrame(driver, frameName):
    driver.switch_to_frame(frameName)

def switchCurrentWindowToFront(driver):
    driver.switch_to_active_element()

def swithToAlert(driver):
    driver.browser.switch_to_alert()
    prt(3, 'Switch to Alert on Browser')
    
def getPageSource(driver):
    prt(3, 'Get Page Source')
    return driver.page_source

def getCurrentURL(driver):
    prt(2, 'Get Current URL')
    return driver.current_url()

def refresh(driver):
    prt(3, 'Refresh Current Page')
    driver.refresh()

def deleteAllCookies(driver):
    prt(3, 'Delete All Cookies')
    driver.delete_all_cookies()
    
def _saveScreenshotAsBase64(driver):
    return driver.get_screenshot_as_base64()

def _saveScreenshotAsFile(driver, filePath):
    driver.get_screenshot_as_file(filePath)

