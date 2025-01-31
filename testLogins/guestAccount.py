#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:57:38 2025

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
import time

from selenium.webdriver.support import expected_conditions as EC
 





def testing(username,password,Testurl2):
    #print("reached here "+Testurl)
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Guest Login information"))
    
    if(Testurl.find("#/fleetTracking")>0):
            print("PASS: Found URL")
            FuncationFile.writeFile(("PASS: URL correct "))
    else:
            print("FAIL: URL not found")
        #    writeToFile("FAIL: URL not found")
    

    try:

    # Map Options button there       
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[12]/div[2]/button')
        FuncationFile.writeFile("PASS: Map Button found")
        
    # Drivers Link
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[1]')
        FuncationFile.writeFile("PASS: Drivers Link, Top left")
        
    # Vehicles Link
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[2]')
        FuncationFile.writeFile("PASS: Vehicles Link, Top left")
    # Trailers Link
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[3]')
        FuncationFile.writeFile("PASS: Trailers Link, Top left")
    # Bookmark Link
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[7]/div/div/div/a/h4')
        FuncationFile.writeFile("PASS: Bookmark found")
        
        
                                            
                                                   
                                                   
    except Exception as e: 
        print("FAILED ", repr(e))
        Testurl2.save_screenshot('selenium-save-screenshot.png')
        FuncationFile.writeFile("****FAILED: "+ repr(e))

 
    