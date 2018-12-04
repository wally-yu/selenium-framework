'''
Created on Dec 20, 2012

@author: wally.yu@autodesk.com
'''

import os
import settings
import shutil
import stat
from xml.etree import ElementTree as etree

def deleteFile(fileLocation):
    if os.path.exists(fileLocation):
        os.remove(fileLocation)

def getCurrentFolder():
    return os.getcwd()

def getCurrentFileAbsLoc():
    return os.path.abspath('.')

def createFolder(folderPath):
    os.mkdir(folderPath)

def createFile(fileLocation):
    f = open(fileLocation, 'w')
    f.close()

def fileExist(fileLocation):
    return os.path.exists (fileLocation)

def getFormatedCurrentTime():
    import time
    return time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time()))

def fileWriteAppend (fileLocation, txt):
    file_handler = open(fileLocation, 'a+')
    file_handler.write (txt + '\n')
    file_handler.close()

def fileWriteChange (fileLocation, txt):
    file_handler = open(fileLocation, 'w+')
    file_handler.write (txt + '\n')
    file_handler.close()

def fileWriteLinesChange (fileLocation, txt):
    file_handler = open(fileLocation, 'w+')
    file_handler.writelines(txt)
    file_handler.close()
    
def fileReadAll (fileLocation):
    try:
        file_handler = open(fileLocation, 'r')
        file_handler.close()
        return file_handler.readlines ()
    except:
        li = []
        return li

def fileLineCount (fileLocation):
    file_handler = open(fileLocation, 'r')
    file_handler.close()
    ret = file_handler.readlines()
    return len(ret)

def fileReadLastLine (fileLocation):
    file_handler = open(fileLocation, 'r')
    ret = file_handler.readlines()
    file_handler.close()
    return ret[-1]

def fileReadLastLines (fileLocation, lineNumbers):
    file_handler = open(fileLocation, 'r')
    ret = file_handler.readlines()
    return ret[lineNumbers*(-1):]


def fileReadline (fileLocation, lineNumbers):
    file_handler = open(fileLocation, 'r')
    ret = file_handler.readlines()
    file_handler.close()
    return ret[lineNumbers-1]

def fileReadLines (fileLocation, lineStart, lineEnd):
    file_handler = open(fileLocation, 'r')
    ret = file_handler.readlines()
    file_handler.close()
    return ret[(lineStart-1):lineEnd]
    
def prt(offset, value, newLine = False):
    if newLine == True:
        print('\r')
    ret = ''
    for i in range(offset*4):
        ret = ret + ' '
    value = value.replace('<','&lt;').replace('>','&gt;')
    settings.steps = (ret + value) if (settings.steps == '') else (settings.steps + '<br>\n' + ret + value)
    print(ret + value)


def formatedStrNumber(number):
    if str(number)[-1] == '1':
        return str(number) + 'st'
    elif str(number)[-1] == '2':
        return str(number) + 'nd'
    elif str(number)[-1] == '3':
        return str(number) + 'rd'
    else:
        return str(number) + 'th'
    
def getOSType():
    import platform
    if platform.system() == 'Windows':
        return 'Windows'
    elif platform.system() == 'Linux':
        return 'Linux'
    else:
        return 'Mac'

def openFolder(folderPath):
    import platform

    if platform.system() == 'Windows':
        os.startfile(folderPath)
    elif platform.system() == 'Linux':
        os.system('xdg-open "%s"' % folderPath)
    else: #Mac
        os.system('open "%s"' % folderPath)
#def openFolder(folderPath):
#    if getOSType == 'Mac':
#        print "open %s" % folderPath
#        os.system('open "%s"' % folderPath)
#    elif getOSType == 'Windows':
#        os.startfile(folderPath)
#    elif getOSType == 'Linux':
#        os.system('xdg-open "%s"' % folderPath)
        
def executeSikuliScript(scriptPath):
    import platform
    if platform.system() == 'Windows':
        currentFolder = getCurrentFolder()
        temp = os.path.join(os.path.dirname(__file__),'ThirdParty')
        temp = os.path.join(temp,'Sikuli')
        temp = os.path.join(temp,'sikuli-script.jar ')
        cmd = 'java -jar %s -r %s' % (temp,scriptPath)
        os.popen(cmd)
    else:
        os.system('open %s' % scriptPath)

def delSpecialItem(li):
    ret = []
    for elem in li:
        continueFlag = True
        for i in range(len(elem)):
            if 48<=ord(elem[i])<=57 or 65<=ord(elem[i])<=90 or 97<=ord(elem[i])<=122:
                pass
            else:
                continueFlag = False
                break
        if continueFlag == True:
            ret.append(elem.lower())
    return ret

def getFirstDayFromWeekNumber(year,weekNumber):
    import datetime
    #currentYear = datetime.date.today().year
    vDay = datetime.date(year,1,1)
    weekday = vDay.weekday()
    firstDayOfYear = vDay - datetime.timedelta(weekday)
    return firstDayOfYear + datetime.timedelta(7*weekNumber - 7)

def getWeekNumberFromToday():
    import datetime
    today = datetime.date.today()
    vDay = datetime.date(today.year, 1,1)
    weekday = vDay.weekday()
    firstDayOfYear = vDay - datetime.timedelta(weekday)
    days = today - firstDayOfYear
    weeks = int(str(days.days)) / 7
    if int(str(days.days)) % 7 > 0:
        weeks = weeks +1
    return weeks

class pharseExcel():
    
    def __init__(self, fileLoc):
        self.fileLoc = fileLoc
        
    def __getRowCount(self,li): # Start from 0
        ret = 0
        for elem in li:
            if elem[0][0] > ret:
                ret = elem[0][0]
        return ret

    def __getRow(self,li, rowNo):
        ret = []
        for elem in li:
            if elem[0][0] == rowNo:
                ret.append(elem)
        return ret
    
    def __getCellData(self,li,x,y):
        ret = ''
        for elem in li:
            if elem[0][0] == x and elem[0][1] == y:
                ret = elem[1]
                break
        return ret

    def __getParaActionByColumnNo(self,li,coNo):
        action = self.__getRow(li,0)
        para = self.__getRow(li,1)
        # Get Action
        actionName = ''
        actionColumnList = []
        for elem in action:
            actionColumnList.append(elem[0][1])
        if coNo in actionColumnList:
            actionName = self.__getCellData(li,0,coNo)
        else:
            tempCo = actionColumnList[0]
            for elem in actionColumnList:
                if elem > coNo:
                    break
                else:
                    tempCo = elem
            actionName = self.__getCellData(li,0,tempCo)
        # Get Para
        paraName = self.__getCellData(li,1,coNo)
        return paraName, actionName
    
    def pharseExcel(self):
        from ThirdParty import pyExcelerator
        
        fileContents = pyExcelerator.parse_xls(self.fileLoc)
        
        ret = {}
        for fileContent in fileContents:
            if fileContent[0].upper() == 'CONFIG':
                ret['CONFIG'] = {}
                sortedLi = sorted(fileContent[1].items(),key=lambda d:d[0])
                tempRowContents = self.__getRow(sortedLi, 1)
                tempRowTitles = self.__getRow(sortedLi, 0)
                config = {}
                for tempRowTitle in tempRowTitles:
                    coNo = tempRowTitle[0][1]
                    try:
                        ret['CONFIG'][tempRowTitle[1]] = self.__getCellData(sortedLi, 1, coNo)
                    except:
                        ret['CONFIG'][tempRowTitle[1]] = ''
                ret['CONFIG']
            else:
                ret[fileContent[0]] = []
                sortedLi = sorted(fileContent[1].items(),key=lambda d:d[0])
    #             action = self.__getRow(sortedLi, 0)
    #             para = self.__getRow(sortedLi, 1)
                rowNo = self.__getRowCount(sortedLi)
                
                for i in range(2,rowNo+1):
                    tempRowContents = self.__getRow(sortedLi, i)
                    tempCase = {}
                    for tempRowContent in tempRowContents:
                        coNo = tempRowContent[0][1]
                        tempData = tempRowContent[1]
                        paraName, actionName = self.__getParaActionByColumnNo(sortedLi, coNo)
                        try:
                            tempCase[actionName][paraName] = tempData
                        except:
                            tempCase[actionName] = {}
                            tempCase[actionName][paraName] = tempData
                    ret[fileContent[0]].append(tempCase)
        return ret
    
def restCall(uri, path, method, body):
    import httplib2 as http
    import json
    
    try:
        from urlparse import urlparse
    except ImportError:
        from urllib.parse import urlparse
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    
    target = urlparse(uri+path)
    body = body
    
    h = http.Http(cache=None)

    response, content = h.request(
            target.geturl(),
            method,
            body,
            headers)
    
    # assume that content is a json reply
    # parse content with the json module
    return response, content

def internetFileExist(uri):
    import urllib2
    f = urllib2.urlopen(uri)
    if f.code == 200:
        return True
    else:
        return False
    
def sendmail(from_who, to, subject, content):
    import smtplib
    #gmail_user = 'autodeskdlsautomation@gmail.com'
    #from_who = 'macking.liu@autodesk.com'
    #gmail_pwd = 'Autotest18'
    smtpserver = smtplib.SMTP("mail.autodesk.com")
    #smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    #smtpserver = smtplib.SMTP("10.148.252.94",25)
    #smtpserver.ehlo()
    #smtpserver.starttls()
    #smtpserver.ehlo
    #smtpserver.login(gmail_user, gmail_pwd)
    header = 'To: ' + to + '\n' + 'From: ' + from_who + '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + content + '\n\n'
    smtpserver.sendmail(from_who, to.split(","), msg)
    #smtpserver.close()
    smtpserver.quit()

    
def getSystemVarialable(definename):
    val = os.getenv(definename)
    print(val)
    return val
