'''
Created on 2012-12-26

@author: wally.yu@autodesk.com
'''

import os

T_MINI = 2
T_SHORT = 5
T_MIDDLE = 10
T_LONG = 20

DEMO = True

# Below is driver's location

DRIVER_PATH_CHROME = os.path.join(os.getcwd(),
                                  'selenium_framework',
                                  'driver_binary_files',
                                  'chromedriver')
DRIVER_PATH_CHROME_HEADLESS = os.path.join(os.getcwd(),
                                           'selenium_framework',
                                           'driver_binary_files',
                                           'headless-chromium')

import os
os.environ["webdriver.chrome.driver"] = DRIVER_PATH_CHROME

# Global Variables
# import FrameworkSupport.Reporting as Rp
steps = ''
token = ''
reportaddress = ''

#record the times of failed
queryfailedtimes = 0
transFaileReason = ''
transDetailReason = []

productionmode = ''
EMBDownloadFailReason = ''