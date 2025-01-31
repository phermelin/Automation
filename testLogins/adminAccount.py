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




def adminTesting(username,password,Testurl2):
    
    Testurl = Testurl2.current_url
    FuncationFile.writeFile(("### Validating Administration Login information"))


    try :
        
        # Geozone/Locations link        
        a="Geozone Location link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li[1]/a')
        FuncationFile.writeFile("PASS: " + a)
        
        # Users link        
        a="Users link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li[2]/a')
        FuncationFile.writeFile("PASS: " + a)        
        
        # Vehicles link        
        a="Vehciles link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li[3]/a')
        FuncationFile.writeFile("PASS: " + a)        
        
        # Cameras link        
        a="Cameras link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[1]/a')
        FuncationFile.writeFile("PASS: " + a)         
        
        # Tablets link        
        a="Tablets link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[2]/div/div/ul/li[2]/a')
        FuncationFile.writeFile("PASS: " + a)         
        
        # Notifications link        
        a="Notifications link"
        driversVehicalLink = Testurl2.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[3]/div/div/ul/li/a')
        FuncationFile.writeFile("PASS: " + a)         
        
        
        
    except Exception as e: 
        FuncationFile.writeFile("****FAILED: " + a + " " + repr(e))
        print("FAILED "+a+" ", repr(e))        