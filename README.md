SeleniumFramework
=================

### Backgrounds

Well, when i looked into my previous codes, I found 6 years back (Dec.2012) when I just joined Autodesk, I wrote a Selenium Framework which was used by several teams within Autodesk.

Now 6 years passed and I already left Autodesk, maybe it's time to share to Github, lol.

This framework provides a way to code Selenium Automation with Layers instead of writing un-resuable and un-readable codes. 
Suggested layers are:
 - Pages: define elements and pages
 - Actions: define test actions using web elements defined in "pages"
 - Test Cases: combination of actions
 
I made some tests these days and prooved these codes can be executed from Mac using Python 3.6.

If I have time, i will work on the follwoing:
 - HTML reports
 - make it more compatible with Firefox on Windows or Linux
 - test headless

Don't laugh at me if codes looks ugly for you, i wrote it 6 years ago, lol

### Usage

###### 1. Install this package:
```
pip install pyselenium-framework
```
###### 2. Create a folder under your application to store Chrome/Firefox binary files, let's say folder called:

```
driver_binary_files
```
###### 3. Download binary files and put them there.
 - Example: Chrome driver can be downloaded from: http://chromedriver.chromium.org/downloads
 ###### 4. Start to build your awesome project simply by:

```
import selenium_framework
```


### Sample Code and Structures
TBD later, but in the meantime, please refer to:
https://github.com/wally-yu/selenium-framework/tree/master/AUT/RedPulse