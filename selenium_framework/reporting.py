'''
Created on 2013-4-22

@author: wally
'''

from selenium_framework import common

def initReport():
    # todo: tbd...
    pass


def reporting(pass_creteria_bool, expectation_txt):
    # todo: tbd...
    if pass_creteria_bool:
        common.prt(3, ' -- Check: ' + expectation_txt + ' <== passed')
    else:
        common.prt(3, ' -- Check: ' + expectation_txt + ' <== failed')


def endReport(testcase_name):
    # todo: tbd...
    pass


def getOSInfo():
    import platform
    if platform.system() == 'Windows':
        osinfo = {'os_type':platform.system(),
                  'os_version':platform.win32_ver()[0],
                  "os_language":"",
                  "os_build_num":platform.win32_ver()[1],
                  "os_sp":platform.win32_ver()[2],
                  'os_arch':platform.architecture()[0]
                }

    elif platform.system() == 'Darwin':
        osinfo = {'os_type':platform.system(),
                  'os_version':platform.mac_ver()[0],
                  "os_language":"",
                  "os_build_num":platform.version(),
                  "os_sp":'',
                  'os_arch':platform.architecture()[0]
                }
    return osinfo # Dic
