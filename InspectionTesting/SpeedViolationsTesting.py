#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:40:54 2025

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
from selenium.webdriver.support.select import Select
import requests
import datetime
import csv
import time
import os

resultFile ="SpeedViolationResults.txt"


### removing Results.txt file, if it exists
if os.path.exists(resultFile):
  os.remove(resultFile)

### opening loginInput file
if not os.path.exists("SpeedViolationVariables.txt"):
    FuncationFile.writeFile("Unable to find SpeedViolationVariables.txt")
    SystemExit(0) ### Kill the run


### getting URL, user and password
with open ('SpeedViolationVariables.txt','r') as file:
    for line in file:
        varb = line.split(',')
file.close()
# parsing out varibles        
testURL = varb[0]
userName = varb[1]
passWord = varb[2]
        
        
### Loggin into navisteam
try:
    # Setting up chrome browser
    options = Options()
    #options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(testURL)
except Exception as fail:
    ## FAILURE TO LAUNCH URL
    FuncationFile.writeFile("FAILED to load URL") 
    SystemExit() # STOP THE TESTING
    
### Logging in
inputElement = driver.find_element(By.XPATH,'//*[@class="MuiInputBase-input MuiInput-input"]')
inputElement.send_keys(userName)
inputElement2 = driver.find_element(By.XPATH,'//*[@class="MuiInputBase-input MuiInput-input MuiInputBase-inputAdornedEnd"]')
inputElement2.send_keys(passWord)
                                                 
element2 = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[1]/div/div/div/div/div/div[3]/button[2]/span[1]').click()
time.sleep(3) # Wating for the page to load

### Going to the Reports Category
# Clicking on Reports
element2 = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppHeader > div.AppTabs > button:nth-child(2)').click()
element2 = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div.RouteFrame.RouteFrame--basic.reports > div > div:nth-child(4) > div > div > ul > li > a').click()
time.sleep(5) # let page load

### Query check
element2 = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--queryPanel.ExpansionPanel--collapsed.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiButtonBase-root.MuiAccordionSummary-root.ExpansionPanel__summary > div.MuiButtonBase-root.MuiIconButton-root.MuiAccordionSummary-expandIcon.MuiIconButton-edgeEnd').click()
                                                
#### Check Organization
time.sleep(3) # let page load                                                 #main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--queryPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--ouMode > div > div
element2 = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--queryPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--ouMode > div > div').click()
#element2 = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--queryPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--ouMode > div > div').click()
checkDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.SelectInput__menuItem.Mui-selected.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button.Mui-selected')
time.sleep(2)

if checkDrop.text == 'Selected organization':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDrop.text,resultFile)
    
checkDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(2)')
if checkDrop.text == 'All organizations':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDrop.text,resultFile)

checkDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(3)')
if checkDrop.text == 'Custom selection':
   FuncationFile.writeFile("PASSED: Found drop list item "+ checkDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDrop.text,resultFile)
        
# Check to see if any other values in the dropdown    
checkDrop = driver.find_elements(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(4)')
if len(checkDrop) > 0:
    FuncationFile.writeFile("#### FAILED: Found wrong drop list item "+ checkDrop.text,resultFile)

checkDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.SelectInput__menuItem.Mui-selected.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button.Mui-selected').click()

### Check Date Range
# opening the dropdown
checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--queryPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--dateRangeMode > div > div').click()
time.sleep(3)
checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.SelectInput__menuItem.Mui-selected.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button.Mui-selected')

if checkDateDrop.text == 'Today':
   FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
   FuncationFile.writeFile("### FAILED: did not find drop list item Today",resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(1)')
if checkDateDrop.text == 'Custom range':
   FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
   FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(3)')
if checkDateDrop.text == 'Yesterday':
   FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
   FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(4)')
if checkDateDrop.text == 'This week':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(5)')
if checkDateDrop.text == 'Last week':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(6)')
if checkDateDrop.text == 'Last 7 days':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)
    
checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(7)')
if checkDateDrop.text == 'Last 14 days':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(8)')
if checkDateDrop.text == 'This month':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(9)')
if checkDateDrop.text == 'Last month':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)

checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(10)')
if checkDateDrop.text == 'Last 30 days':
    FuncationFile.writeFile("PASSED: Found drop list item "+ checkDateDrop.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item "+ checkDateDrop.text,resultFile)    

checkDateDrop = driver.find_elements(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li:nth-child(11)')
if len(checkDateDrop)>0 :
    FuncationFile.writeFile("### FAILED: To many items in dropdown list",resultFile)
# Stop looking at Date Range     
checkDateDrop = driver.find_element(By.CSS_SELECTOR,'#menu- > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.SelectInput__menuItem.Mui-selected.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button.Mui-selected').click()
time.sleep(3)

### Looking at Violation Filters
ViolationCheck = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--filtersPanel.ExpansionPanel--collapsed.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiButtonBase-root.MuiAccordionSummary-root.ExpansionPanel__summary > div.MuiButtonBase-root.MuiIconButton-root.MuiAccordionSummary-expandIcon.MuiIconButton-edgeEnd').click()
time.sleep(3)
# Check drivers
ViolationCheck = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--filtersPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--driverNames > label')
if ViolationCheck.text == 'Drivers':
    FuncationFile.writeFile("PASSED: Found drop list item "+ ViolationCheck.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item DRIVERS",resultFile)
    
# Check Vehicles
ViolationCheck = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--filtersPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--vehicleNames > label')
if ViolationCheck.text == 'Vehicles':
    FuncationFile.writeFile("PASSED: Found drop list item "+ ViolationCheck.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item Vehicles",resultFile)
# Check Geozone
ViolationCheck = driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div.MuiPaper-root.MuiAccordion-root.ExpansionPanel.ReportControl--filtersPanel.ExpansionPanel--expanded.Mui-expanded.MuiAccordion-rounded.MuiPaper-elevation1.MuiPaper-rounded > div.MuiCollapse-root.MuiCollapse-entered > div > div > div > div > div.MuiFormControl-root.SelectInput.ReportControl--geozoneNames > label')
if ViolationCheck.text == 'Geozone':
    FuncationFile.writeFile("PASSED: Found drop list item "+ ViolationCheck.text,resultFile)
else:
    FuncationFile.writeFile("### FAILED: did not find drop list item Geozone",resultFile)


# Check possible Data Table column values
dTable =driver.find_element(By.CSS_SELECTOR,'#main > div > div.AppRoot__Content > div:nth-child(3) > div > div:nth-child(5) > div.MuiButtonBase-root.MuiAccordionSummary-root.ExpansionPanel__summary > div.MuiAccordionSummary-content > div.ExpansionPanel__summary__end > button').click()
dTable =driver.find_element(By.CSS_SELECTOR,'body > div.MuiPopover-root.Menu__popover > div.MuiPaper-root.MuiMenu-paper.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > ul > li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.Menu__item--selectColumns.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button').click()
                                               
dTable = driver.find_elements(By.CLASS_NAME,'ToggleTree__item__label')

ColTables=["Information","Start Date","Start Time","Duration","Driver Name","Vehicle","Speed","Average Speed","Maximum Speed","Speed Limit","Grace Period","Location","Speed Violation Map","Geozone"]
      #      Information	Start Date	Start Time	Duration	 Driver Name	 ehicle	Speed	Average Speed	Maximum Speed	Speed Limit	Grace Period	Location	Speed Violation Map
#for ee in range (len(dTable)):
#    testSplit = dTable[ee].text.split('\n')
print (dTable)
for ss in range (len(dTable)):
     time.sleep(1)   
     if dTable[ss].text == ColTables[ss]:
         FuncationFile.writeFile("PASSED: Column Heading found: "+ColTables[ss]+" ",resultFile)
#    if testSplit[ss].lstrip() == colNames[ss]:
#        print (colNames[ss]+"------->"+testSplit[ss])
#        FuncationFile.writeFile("PASSED: Column "+ testSplit[ss]+" for Inspections Summary Report Data Table",resultFile)
#    else:
#        FuncationFile.writeFile("FAILED: NO Column "+ testSplit[ss]+" for Inspections Summary Report in Data Table",resultFile)
      


    


print("here")



    
    
driver.close()