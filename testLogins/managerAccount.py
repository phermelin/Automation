#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:29:45 2025

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

"""
        for x in testAuto:
            try:
                t =Testurl2.find_element(By.PARTIAL_LINK_TEXT,x)
                FuncationFile.writeFile("PASSED: found map options, "+ x)
            except NoSuchElementException as z:
                FuncationFile.writeFile("****FAILED: "+ x +" type of execption->"+ repr(z))


"""



def managerTesting(username,password,Testurl2):
    
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Manager Login information"))


  # Validate Fleet Tracking Tab. 
    try:
 # Click on Fleet Tracking link at the top of the page
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[1]').click()
        FuncationFile.writeFile("CLICKED: Clicked on Fleet Tracking")            
        time.sleep(3) # waiting for page to load properly
         
            
    # Map Options button there
        a="Map options button"       
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[12]/div[2]/button')
        
        FuncationFile.writeFile("PASS: Map Button found")
        
    # Drivers Link
        a="Drivers Link"       
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[1]')
        FuncationFile.writeFile("PASS: Drivers Link, Top left")
        
    # Vehicles Link
        a="Vehicles Link"       
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[2]')
        FuncationFile.writeFile("PASS: Vehicles Link, Top left")
        
    # Trailers Link
        a="Trailers Link"           
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[6]/div/div/div/div/div/div/ul/li[3]')
        FuncationFile.writeFile("PASS: Trailers Link, Top left")
    # Bookmark Link
        a="Bookmark Link"       
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div[3]/div[7]/div/div/div/a/h4')
        FuncationFile.writeFile("PASS: Bookmark area found")

## Navigating to the Reports 
  # Click on Reports link at the top of the page
        a="Reports Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[2]').click()
        FuncationFile.writeFile("CLICKED: Reports")
        time.sleep(3) # waiting for page to load properly

  # Inspections Summary link
        a="inspectionsSummary"
        driversVehicalLink=Testurl2.find_element(By.PARTIAL_LINK_TEXT,'Inspections Summary')
        FuncationFile.writeFile("PASSED: Inspection Summary link found")

  # Speed Violations link
        a="Speed Violations link"       
        #FuncationFile.linkClickTest(Testurl2, "#/reports/speedViolations/default", "Speed Violation")
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[4]/div/div/ul/li/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Speed Violations link found")        
        
  # Cycle Summary link
        a="Cycle Summary Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[4]/div/div/ul/li/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Cycle Summary link found")        

  # Trip Summary link
        a="Trip Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[7]/div/div/ul/li[2]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Trip Summary link found")                 
        
   # Hours of Service Summary link
        a="Hours of Service Summary"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[1]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Hours of Service Summary link found")                 
  
   # Unidentified Driving Summary  link
        a="Unidentified Driving Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[2]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Unidentified Driving Summary link found")        
        
   # Exception Summary link
        a="Exection Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[5]/div/div/ul/li/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Exception Summary link found")    
   
    # Geozone Summary Link
        a="Geozone Summary Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[8]/div/div/ul/li/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Geozone Summary link found")    
 
    # Performance Summary Link
        a="Performace Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[3]/div/div/ul/li[1]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Performance Summary link found") 
    
    # Shift Summary Link
        a="Shift Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[3]/div/div/ul/li[2]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Shift Summary link found") 
        
    # Fuel Tax Summary Link
        a="Fuel Tax Summary Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[6]/div/div/ul/li[1]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Fuel Tax Summary link found")     
 
    # Consumption Summary Link
        a="Consuptions Summary Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[6]/div/div/ul/li[2]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Consuption Summary link found") 
        
    # Fueling Summary Link
        a="Fueling Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[6]/div/div/ul/li[3]/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Fueling Summary link found")     
    
    # Schedule Link
        a="Schedule Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[5]/div/div/ul/li/a').click()
        time.sleep(3)
        Testurl2.back()
        FuncationFile.writeFile("PASSED: Schedule link found")  
    
    except Exception as e: 
        print("FAILED "+a+" ", repr(e))
        FuncationFile.writeFile("****FAILED: "+a+" " + repr(e))


  