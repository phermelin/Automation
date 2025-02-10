#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:58:13 2025

@author: peter

This will test that a Guest Account has the proper access
Parameters will be taken from file 'guestTest.txt' Located un the 'GuestAccount' folder:
    1. Web Site Address
    2. Username
    3. Password
    
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
import requests
import datetime
import csv
import time
import os


### removing Results.txt file, if it exists
if os.path.exists("Results.txt"):
  os.remove("Results.txt")
  
### Creating a new file for results
FuncationFile.writeFile("Testing of Logins")
FuncationFile.writeFile("Testing")
# Stop if results file does not get created
if not os.path.exists("Results.txt"):    
    FuncationFile.writeFile("Unable to find Result.txt")
    exit(0)
    
### opening loginInput file
if not os.path.exists("loginInput.txt"):
    FuncationFile.writeFile("Unable to find loginInput.txt")
    exit(0)



            

# Read in test URL 
url=""
with open("testURL.txt", "r") as file:
    for line in file:
        url=line.strip()


#driver.get(url)
## check to see if the url worked


# Reading in the first to be tested
# SUser - Support User information
with open ('loginInput.txt','r') as file:
    import driverAccout       # Testing of drivers account
    import guestAccount       # Testing of guest account    
    import managerAccount     # Testing of manager account
    import dispatcherAccount  # Testing the dispatder account
    import adminAccount       # Testing of the Administator accountadmin_testeradmin_testeradmin_testeradmin_testeradmin_testeradmin_tester
    import mechanicAccount    # Testing of the mechanicAccount
    
    for line in file:
        SUser = line.split(',')
        
        # Setting up chrome browser
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)


# Logging in
        inputElement = driver.find_element(By.XPATH,'//*[@class="MuiInputBase-input MuiInput-input"]')
        inputElement.send_keys(SUser[1])
        inputElement2 = driver.find_element(By.XPATH,'//*[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd"]')
        inputElement2.send_keys(SUser[2])
                                                  
        element2 = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div/div[3]/button[2]/span[1]').click()
        time.sleep(3) # Wating for the page to load


        match SUser[0]:
            case "Driver":
                driverAccout.driverTesting(driver)          
                print ("Driver")                
            case "Guest":
                print ("Guest")
                guestAccount.testing(driver)          
                driver.close()
            case "Manager":
                managerAccount.managerTesting(SUser[1],SUser[2],driver)
                print("Manager")
                driver.close()
            case "Dispatcher":
                dispatcherAccount.dispatcherTesting(SUser[1],SUser[2],driver)
                print("Dispatcher")
                driver.close()
            case "Super Administrator":
                print("superAdmin")
            case "Administrator":                
                adminAccount.adminTesting(SUser[1],SUser[2],driver)
                print ("Administrator")
                driver.close()
              
            case "Mechanic":
                print("Mechanic")
                mechanicAccount.mechTesting(SUser[1],SUser[2],driver)
                driver.close()
            case _:
                print("None of the above")
                driver.close()    
#driver.close()

        