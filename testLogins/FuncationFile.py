#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:28:13 2025

@author: peter
"""

import datetime
import FuncationFile #Export of Results to file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


# Funcation to write / append to a file 
def writeFile(text):
    x= datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open("Results.txt","a") as resultsFile:
        resultsFile.write(x+" --> " +text+" \n")    
        

def linkClickTest (Testurl,location, Test):
    
    try:
        
        time.sleep(3)
        
        loc = Testurl.current_url
        if (loc.find(location)>0):
            FuncationFile.writeFile("PASSED:  "+ Test)

        else:
            FuncationFile.writeFile("FAILED: Link did not work : "+Test)
            
            
    except Exception as e: 
        print("FAILED ", repr(e))
        FuncationFile.writeFile("****FAILED: Clicking on link caused error :"+ location + repr(e))

    