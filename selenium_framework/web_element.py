'''
Created on Dec 21, 2012

@author: wally.yu@autodesk.com
'''
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_framework.common import prt, formatedStrNumber
import settings
import time
from selenium.webdriver.common.by import By


class Identifier():
    """ Define identifier, created singleton instance which can be used among projects """
    id = By.ID
    name = By.NAME
    xpath = By.XPATH
    class_name = By.CLASS_NAME
    css = By.CSS_SELECTOR
    link_text = By.LINK_TEXT
    part_link_text = By.PARTIAL_LINK_TEXT,
    tag = By.TAG_NAME


# Singleton identifer instance can be used by projects
identifier = Identifier()


class _BaseElement():
    '''This is Base Class of Web Element and its Methods'''
    def __init__(self, identifier_type, identifier_value, nick_name=''):
        """ Web Element Identifier """
        self.sID = identifier_type  # identifier type, which should be a "identifier" object method
        self.sIDV = identifier_value  # identifier value
        self.sNN = nick_name  # identifier nick name
        
    def _highlight(self, driver, index=None):
        locator = driver.find_elements(by=self.sID,
                                       value=self.sIDV)[index] if index else driver.find_element(by=self.sID,
                                                                                                 value=self.sIDV)
        for i in range(3):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  locator,
                                  "color: red; border: 2px solid red;")
            time.sleep(0.2)
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  locator,
                                  "")
            time.sleep(0.2)

    def click(self, driver,  elementsClickByIndex_indexNumber = None):
        if elementsClickByIndex_indexNumber == None:
            '''Click a Web Element'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver)
                WebDriverWait(driver,settings.T_SHORT).until(lambda x: x.find_element(by=self.sID, value=self.sIDV).is_displayed())
                driver.find_element(by=self.sID, value=self.sIDV).click()
                time.sleep(settings.T_SHORT)
                prt(3, 'Click %s Button' % self.sNN)
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
        else:
            '''Click A Element from Lots of Matching Elements by IndexNumber'''
            if self._if_exist(driver): # Check Existence
                try:
                    if settings.DEMO:
                        self._highlight(driver, elementsClickByIndex_indexNumber - 1)
                    driver.find_elements(by=self.sID, value=self.sIDV)[elementsClickByIndex_indexNumber - 1].click()
                    prt(3, 'Click the %s Element from "%s"' % (formatedStrNumber(elementsClickByIndex_indexNumber), self.sNN))
                    time.sleep(settings.T_SHORT)
                except Exception as e:
                    prt(3, str(e))
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
        
    def db_click(self, driver):
        '''Double Click a Web Element'''
        if self._if_exist(driver):  # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            driver.find_element(by=self.sID, value=self.sIDV).double_click()
            prt(3, 'Double Click %s Button' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            
    def if_exist(self, driver, elementsExistByText_textValue = None, waitTime = settings.T_LONG):
        ''' Check the Existence of a Web Element / Lots of Matching Web Elements'''
        if elementsExistByText_textValue == None:
            '''Check the Existence of a Web Element'''
            try:
                WebDriverWait(driver,waitTime).until(lambda x: x.find_element(by=self.sID, value=self.sIDV))
                if settings.DEMO:
                    self._highlight(driver)
                prt(3, 'Check Existence of %s: Existed!' % self.sNN)
                return True
            except:
                prt(3, 'Check Existence of %s: NOT Existed!' % self.sNN)
                return False
        else:
            '''Find if an Element is Existed in Lots of Matching Elemets'''
            prt(3, 'Check Existence of Text Value "%s" in Elemets "%s"' % (elementsExistByText_textValue, self.sNN))
            if self._if_exist(driver): # Check Existence
                index = 1 # initiate looping value
                for locator in driver.find_elements(self.sID, value=self.sIDV):
                    if locator.text == elementsExistByText_textValue:
                        if settings.DEMO:
                            self._highlight(driver, index - 1)
                        return index
                    else:
                        index += 1
                return 0
            else:
                return 0
            
           
    def _if_exist(self, driver):
        '''Check Web Element Existence, Private Use Only! '''
        try:
            WebDriverWait(driver, settings.T_LONG).until(lambda x: x.find_element(by=self.sID, value=self.sIDV))
            return True
        except:
            return False
        
    def is_enabled(self, driver):
        '''Click if the Web Element is enabled'''
        if self._if_exist(driver):  # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Check if Element %s is enabled' % self.sNN)
            if self.__is_visible(driver):
                return driver.find_element(by=self.sID, value=self.sIDV).is_enabled()
            else:
                return False    
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
    
    def is_visible(self, driver):
        '''Click if a Web Element is visible'''
        if self._if_exist(driver):  # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Check if Element %s is visible' % self.sNN)
            return driver.find_element(by=self.sID, value=self.sIDV).is_displayed()
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
    
    def __is_visible(self, driver):
        '''Click if a Web Element is visible'''
        if self._if_exist(driver):  # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            return driver.find_element(by=self.sID, value=self.sIDV).is_displayed()
        else:
            return False
    
    def get_text(self, driver, elementsGetTextByIndex_IndexNumber = None):
        import datetime
        if not elementsGetTextByIndex_IndexNumber:
            '''Get the Text Value From a Web Element'''
            if self._if_exist(driver) == True: # Check Existence
                if settings.DEMO:
                    self._highlight(driver)
                prt(3, 'Get Text Value from Element: %s @ %s' % (self.sNN, datetime.datetime.now().strftime("%m-%d %H:%M:%S.%f")))
                return driver.find_element(by=self.sID, value=self.sIDV).text
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
                return ''
        else:
            '''Get the Text Value FromFrom Matching Elements'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver, elementsGetTextByIndex_IndexNumber - 1)
                prt(3, 'Get the %s Text Value from: %s' % (formatedStrNumber(elementsGetTextByIndex_IndexNumber), self.sNN))
                return driver.find_elements(self.sID, value=self.sIDV)[elementsGetTextByIndex_IndexNumber + 1].text
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
                return ''
            
    def _get_text(self, driver, elementsGetTextByIndex_IndexNumber=None):
        if not elementsGetTextByIndex_IndexNumber:
            '''Get the Text Value From a Web Element'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver)
                return driver.find_element(by=self.sID, value=self.sIDV).text
            else:
                return ''
        else:
            '''Get the Text Value FromFrom Matching Elements'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver, elementsGetTextByIndex_IndexNumber - 1)
                return driver.find_elements(self.sID, value=self.sIDV)[elementsGetTextByIndex_IndexNumber + 1].text
            else:
                return ''
              
    def get_texts(self, driver):
        '''
        Note: This is only used for elemets not for single element
        '''
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                    self._highlight(driver)
            prt(3, 'Get All Texts From %s' % self.sNN)
            ret = []
            for element in driver.find_elements(self.sID, value=self.sIDV):
                ret.append(element.text)
            return ret
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return ''
        
    def get_value(self, driver, attribute, elementsGetTextByIndex_IndexNumber = None):
        if not elementsGetTextByIndex_IndexNumber:
            '''Get the Text Value From a Web Element'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver)
                prt(3, "Get Text's %s from Element: %s" % (attribute, self.sNN))
                return driver.find_element(by=self.sID, value=self.sIDV).get_attribute(attribute)
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
                return ''
        else:
            '''Get the Text Value FromFrom Matching Elements'''
            if self._if_exist(driver): # Check Existence
                if settings.DEMO:
                    self._highlight(driver, elementsGetTextByIndex_IndexNumber - 1)
                prt(3, "Get the %s Text's %s from: %s" % (formatedStrNumber(elementsGetTextByIndex_IndexNumber), attribute, self.sNN))
                return driver.find_element(by=self.sID, value=self.sIDV)[elementsGetTextByIndex_IndexNumber + 1].get_attribute(attribute)
            else:
                prt(3, 'Element %s is NOT found!' % self.sNN)
                return ''
    
    def get_values(self, driver, attribute):

        '''Get the Text Value From a Web Element'''
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            ret = []
            for elem in driver.find_elements(by=self.sID,value=self.sIDV):
                ret.append(elem.get_attribute(attribute))
            prt(3, "Get All Value from: %s" % (self.sNN))
            return ret
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return ''

    def get_elements(self, driver):
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            return driver.find_elements(by=self.sID,value=self.sIDV)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return ''
           
    def wait_until_text_present(self, driver, textWait, waitTime=settings.T_LONG):
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Wait for Text "%s" to be Present in %s' % (textWait, self.sNN))
            
            for i in range(waitTime):
                if self._get_text(driver).find(textWait) >= 0:
                    return True
                else:
                    time.sleep(1)
            return False
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False

    def wait_until_value_present(self, driver, attribute, textWait, waitTime=settings.T_LONG):
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Wait for Text "%s" to be Present in %s' % (textWait, self.sNN))
            
            for i in range(waitTime / 4):
                if self.get_value(driver, attribute).find(textWait) >= 0:
                    return True
                else:
                    time.sleep(15)
                    
            return False
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
        
    def mouse_over(self, driver):
        if self._if_exist(driver):  # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Mouse over on: %s' % (self.sNN))
            
            elemToHover = driver.find_element(by=self.sID, value=self.sIDV)
            hover = ActionChains(driver).move_to_element(elemToHover)
            hover.perform()
            
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
        
    def send_ESC_key(self, driver):
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Send Keys to: %s' % (self.sNN))
            
            elemToSend = driver.find_element(by=self.sID, value=self.sIDV)
            key = ActionChains(driver).send_keys_to_element(elemToSend, u'\ue00c')
            key.perform()
            
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
 
    def send_key(self, driver, key):
        
        if self._if_exist(driver): # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Send Keys to: %s' % (self.sNN))
            
            elemToSend = driver.find_element(by=self.sID, value=self.sIDV)
            key = ActionChains(driver).send_keys_to_element(elemToSend, key)
            key.perform()
            
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False

class WebCheckbox(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
    
    def is_checked(self, driver):
        '''Check if the Checkbox is checked'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            prt(3, 'Check if Element %s is checked' % self.sNN)
            return driver.find_element(by=self.sID, value=self.sIDV).is_selected()
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return False
    
    def check(self, driver):
        '''Set "ON" to a Checkbox'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            if driver.find_element(by=self.sID, value=self.sIDV).is_selected() == True:
                pass
            else:
                driver.find_element(by=self.sID, value=self.sIDV).click()
            prt(3, 'Set Checkbox %s to "ON" (checked)' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
    
    def check_all(self,driver):
        '''Set "ON" to a Checkbox'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            matchItems = driver.find_elements(by=self.sID, value=self.sIDV)
            if len(matchItems) > 0:
                for item in matchItems:
                    if item.is_selected() == True:
                        pass
                    else:
                        item.click()
            prt(3, 'Set Checkbox %s to "ON" (checked)' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)        
    
    def uncheck(self, driver):
        '''Set "OFF" to a Checkbox'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            if driver.find_element(by=self.sID, value=self.sIDV).is_selected() == True:
                driver.find_element(by=self.sID, value=self.sIDV).click()
            else:
                pass
            prt(3, 'Set Checkbox %s to "OFF" (unchecked)' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
        
    def uncheck_all(self, driver):
        '''Set "OFF" to a Checkbox'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
                
            matchItems = driver.find_elements(by=self.sID, value=self.sIDV)
            if len(matchItems) > 0:
                for item in matchItems:
                    if item.is_selected() == True:
                        item.click()
                    else:
                        pass
            prt(3, 'Set Checkbox %s to "OFF" (unchecked)' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
    
class WebEdit(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
        
    def set_txt(self, driver, text):
        ''' Set Text to a Editbox '''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)

            driver.find_element(by=self.sID, value=self.sIDV).clear()
            driver.find_element(by=self.sID, value=self.sIDV).send_keys(text)
#            if self.sID == 'id':
#                driver.find_element_by_id(self.sIDV).clear()
#                driver.find_element_by_id(self.sIDV).send_keys(text)
#            elif self.sID == 'name':
#                driver.find_element_by_name(self.sIDV).clear()
#                driver.find_element_by_name(self.sIDV).send_keys(text)
            prt(3, 'Set %s as: %s' % (self.sNN, text))
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)    

class WebButton(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
    
    def submit(self, driver):
        ''' Submit a Web Form'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            driver.find_element(by=self.sID, value=self.sIDV).submit()
            prt(3, 'Click %s Button' % self.sNN)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)

class WebList(_BaseElement):
    
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
    
    def select_by_index(self, driver, indexNumber):
        '''Select an Item from List by Index Number'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            selectObj = Select(driver.find_element(by=self.sID, value=self.sIDV))
            selectorSize = selectObj.size()
            if indexNumber > selectorSize:
                pass
            else:
                selectObj.select_by_index(self, indexNumber)
            prt(3, 'Select %s to by index number: %d' % self.sNN, indexNumber)
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
        
    def select_by_text(self, driver, text):
        '''Select an Item from List by Text'''
        if self._if_exist(driver) == True: # Check Existence
            if settings.DEMO:
                self._highlight(driver)
            selectObj = Select(driver.find_element(by=self.sID, value=self.sIDV))
            selectObj.select_by_visible_text(text)
            prt(3, 'Select %s to by visible text: %s' % (self.sNN, text))
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
    
    def get_current_selection(self, driver):
        '''Get Current Selection from a List'''
        if self._if_exist(driver) == True: # Check Existence
            try:
                selectObj = Select(driver.find_element(by=self.sID, value=self.sIDV))
                prt(3, "Get Selector %s's Current Selected Option" % self.sNN)
                if settings.DEMO:
                    self._highlight(driver)
                return selectObj.first_selected_option().getText()
            except:
                prt(3, "Get Selector %s's Current Selected Option, But No Item Seleted" % self.sNN)
                return ''
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
        
    def get_all_options(self, driver):
        '''Get all options from a List, return value is a Python List'''
        if self._if_exist(driver) == True: # Check Existence
            prt(3, "Get Selector %s's Current Selected Option" % self.sNN)
            selectObj = Select(driver.find_element(by=self.sID, value=self.sIDV))
            if settings.DEMO:
                self._highlight(driver)
            return selectObj.options()
                
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)
            return []
    
class WebLabel(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)

class WebLink(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)

class WebTable(_BaseElement):
    '''
    To By Done!!!
    '''
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)  
        
class WebItem(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
        
class WebGeneral(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
        
class WebIframe(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
        
class WebPicture(_BaseElement):
    def __init__(self, identityMethod, identityValue, nickName):
        _BaseElement.__init__(self, identityMethod, identityValue, nickName)
        
    def get_pic_url(self, driver):
        if self._if_exist(driver) == True: # Check Existence
            prt(3, "Get URL of Picture: %s" % self.sNN)
            try:
                if settings.DEMO:
                    self._highlight(driver)
                selectObj = driver.find_element(by=self.sID, value=self.sIDV).get_attribute('src')
                return selectObj
            except:
                return ''
        else:
            prt(3, 'Element %s is NOT found!' % self.sNN)