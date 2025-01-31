#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:32:14 2025

@author: peter
"""

import FuncationFile #Export of Results to file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def driverTesting(username,password,Testurl2):
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Drivers Login information"))
    
    try :
        
        # My Inspections link        
        a="My Inspections Summary"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li/a').click()
        FuncationFile.linkClickTest(Testurl, "myInspections", a)
        FuncationFile.writeFile("PASSED: " + a)                 
        
    except Exception as e:
        FuncationFile.writeFile("****FAILED: " + a + " " + repr(e))
        print("FAILED "+a+" ", repr(e))   

