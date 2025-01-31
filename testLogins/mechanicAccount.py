#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:59:38 2025

@author: peter
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:05:13 2025

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




def mechTesting(username,password,Testurl2):
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Mechanic Login information"))


    try :
        
        # Click on the Fleet Tracking link
        a="Click on FLeet Tracking Link" 
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[1]/span[1]').click()
        FuncationFile.writeFile("CLICKED: Clicked on Fleet Tracking")            
        time.sleep(3) # waiting for page to load properly  
        
        # Check page / url
        Testurl = Testurl2.current_url
        a="URL pointing at Fleet Tracking"
        if(Testurl.find("#/fleetTracking")>0):
                print("PASS: Found URL")
                FuncationFile.writeFile("PASSED: url "+Testurl)
        else:
               raise Exception(a)
               
        # Click on the Fleet Tracking link
        a="Click Reports Link" 
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[2]').click()
        FuncationFile.writeFile("CLICKED: Clicked on Reports Tracking")            
        time.sleep(3) # waiting for page to load properly  
                  
        # Check page / url
        Testurl = Testurl2.current_url
        a="URL pointing at Reports "
        if(Testurl.find("#/reports")>0):
                print("PASS: Found URL")
                FuncationFile.writeFile("PASSED: url: "+Testurl)
        else:
               raise Exception("Wrong URL" +Testurl)
        #Inspections link
        a="Inspections Summary link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li/a')
        FuncationFile.writeFile("PASSED: " +a)
        
        #Schedule link
        a="Schedule Link"       
        driversVehicalLink=Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li/a)')
        FuncationFile.writeFile("PASSED: "+a)
        
        
    except Exception as e: 
           FuncationFile.writeFile("****FAILED: " + a + " " + repr(e))
           print("FAILED "+a+" ", repr(e))   
        
        