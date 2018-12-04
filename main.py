from selenium_framework.common import prt, getFormatedCurrentTime
from AUT.RedPulse.test_cases import SmokeTest

prt(0, 'Testing Starts on %s' % getFormatedCurrentTime())

url = 'https://www.redpulse.com/'

# Testing Start ----------------------------------
SmokeTest(url)

# Testing End ------------------------------------
prt(0, 'Testing Finished on %s' % getFormatedCurrentTime())