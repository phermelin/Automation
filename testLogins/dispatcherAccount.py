#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:17:51 2025

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

def dispatcherTesting(username,password,Testurl2):
    
    
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Dispatcher Login information"))
    
    try :
 # Click on Fleet Tracking link at the top of the page
        a="Click on FLeet Tracking" 
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[1]').click()
        FuncationFile.writeFile("CLICKED: Clicked on Fleet Tracking")            
        time.sleep(3) # waiting for page to load properly        
        
        
    # Map Options button there       
        a="Map Option button"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[12]/div[2]/button')
       # driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[12]/div[2]/button')
        FuncationFile.writeFile("PASS: Map Button found")
        
    # Drivers Link
        a="Drivers link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[1]')
        FuncationFile.writeFile("PASS: Drivers Link, Top left")
        
    # Vehicles Link
        a="Vehicle link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[2]')
        FuncationFile.writeFile("PASS: Vehicles Link, Top left")
    # Trailers Link
        a="Trails link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[3]')
        FuncationFile.writeFile("PASS: Trailers Link, Top left")
    # Bookmark Link
        a="Bookmark link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[7]/div/div/div/a/h4')
        FuncationFile.writeFile("PASS: Bookmark found")
        
    # Click Hide Inactive 
        a="Hide Inactive Click"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/div[2]/div[4]/span[1]').click()
        #FuncationFile.writeFile("PASS: Bookmark found")
        time.sleep(3) # waiting for page to load properly

    # Click on the first driver
        a="Clicking on first driver"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]').click()
    
    # Check in the info panel on the driver loads.
        a="info panel for driver"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[13]/div[2]/div/div/a/h4')
        FuncationFile.writeFile("PASS: Able to bring up the info panel for a driver")
                                                   
# Click on Reports link at the top of the page
        a="Click on Reports Link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[2]').click()
        FuncationFile.writeFile("CLICKED: Reports")
        time.sleep(3) # waiting for page to load properly

# Inspections Summary link
        a="Inspections Summary Link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li/a')
        FuncationFile.writeFile("PASSED: Inspection Summary link found")


 # Hours of Service Summary link
        a="Hours of Service Summary link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[1]/a')
        FuncationFile.writeFile("PASSED: Hours of Service Summary link found")                 

 # Unidentified Driving Summary  link
        a="Unidentified Driving link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[2]/a')
        FuncationFile.writeFile("PASSED: Unidentified Driving Summary link found")        
      
 # Exception Summary link
        a="Exception Summary link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[5]/div/div/ul/li/a')
        FuncationFile.writeFile("PASSED: Exception Summary link found")    
  
  # Shift Summary Link
        a="Shift Summary link"
        # driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[3]/div/div/ul/li[2]/a')
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[3]/div/div/ul/li/a')
        FuncationFile.writeFile("PASSED: Shift Summary link found") 
   
  # Schedule Link
        a="Schedule link"
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[5]/div/div/ul/li/a')
        FuncationFile.writeFile("PASSED: Schedule link found")                                                     
                                                   
                                                   
    except Exception as e: 
        FuncationFile.writeFile("*** FAILED: " + a + " " + repr(e))
        Testurl2.save_screenshot('selenium-save-' + "1" +'screenshot.png')
        print("FAILED "+a+" ", repr(e))
        
        