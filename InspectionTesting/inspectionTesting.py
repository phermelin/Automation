#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:09:34 2025
Test the basic features of Inspections Summary
USER: will be a superAdmin
all other features outsdie Inspections are out of scope
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


### removing Results.txt file, if it exists
if os.path.exists("Results.txt"):
  os.remove("Results.txt")

### opening loginInput file
if not os.path.exists("inspectionVariables.txt"):
    FuncationFile.writeFile("Unable to find inspectionVariables.txt")
    SystemExit(0) ### Kill the run


### getting URL, user and password
with open ('inspectionVariables.txt','r') as file:
    for line in file:
        varb = line.split(',')
file.close()
print (varb )
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
    
     

### Navigate to Reports and then to Inspection Summary
# Clicking on the Reports Category
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div[2]/button[2]').click()
time.sleep(3) # Wating for the page to load

# Clicking on Inspection Summary link
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[2]/div/div[1]/div/div/ul/li/a').click()
time.sleep(4) # Wating for the page to load

### Query testing


### Checking the different mode "By Date Range" "Latest Vehicle" "Latest By Inspector" 
# clicking on element to show all in the list. Blue button Sample Carrier Name Erid
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[2]/div[1]/div[1]/div[2]/div[1]').click() 
#element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[2]/div[2]/div/div/div/div/div[6]/div').click()
time.sleep(3) # Wating for the page to load
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[2]/div[2]/div/div/div/div/div[6]/div/div').click()
time.sleep(2)

    
# There only 3 possible values: "By Date Range" "Latest By Vehicle" "Latest By Inspector" 
# any more or less is an error
ModeList=["By Date Range","Latest By Vehicle","Latest By Inspector" ]

test=driver.find_elements(By.XPATH,'//*[@data-value]')

for zz in range (len(test)):
    if test[zz].text in ModeList:
        FuncationFile.writeFile("PASSED: Found "+ test[zz].text +" in the mode menu")
    else:
        FuncationFile.writeFile("FAILED found "+test[zz].text+" NOT part of the mode menu")
# If there is a double        
if (len(test)>3):
    FuncationFile.writeFile("FAILED found Mode had duplicate value in the mode menu")

# unclicking Mode
test=driver.find_element(By.XPATH,'//*[@data-value]').click()
time.sleep(3)


### Checking Organization has only 2 values.. "Selected Organization" and "Custom Selection"
OrgList=["Selected organization","Custom selection" ]
switch=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div').click()
time.sleep(2)

test=driver.find_elements(By.XPATH,'//*[@data-value]')
for zz in range (len(test)):
    print(test[zz].text)
    if test[zz].text in OrgList:
        FuncationFile.writeFile("PASSED: Found "+ test[zz].text+" in the Organization menu")
    else:
        FuncationFile.writeFile("FAILED found "+test[zz].text+" NOT part of the dropdown")
# If there is a double        
if (len(test)>2):
    FuncationFile.writeFile("FAILED found Mode had duplicate value in the Organization menu")
# Unselecting the Organization    
test=driver.find_element(By.XPATH,'//*[@data-value]').click()

## # Checking Data Range values - 8 values
DateRangeList=["Custom range", "Today", "Yesterday", "This week", "Last week", "Last 7 days","This month","Last month"]
switch=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[2]/div[2]/div/div/div/div/div[3]/div/div').click()
time.sleep(2)

test=driver.find_elements(By.XPATH,'//*[@data-value]')
for zz in range (len(test)):
    print(test[zz].text)
    if test[zz].text in DateRangeList:
        FuncationFile.writeFile("PASSED: Found "+ test[zz].text+" in the Organization menu")
    else:
        FuncationFile.writeFile("FAILED found "+test[zz].text+" NOT part of the dropdown")
# If there is a double        
if (len(test)>8):
    FuncationFile.writeFile("FAILED found Mode had duplicate value in the Organization menu")
# Unselecting the Organization    
test=driver.find_element(By.XPATH,'//*[@data-value]').click()

#### Testing of Inspection Filters
# opening section
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[3]/div[1]/div[2]').click()
time.sleep(2)

InspectionsList=["Vehicles", "Vehicle Types", "Geozones", "Inspectors", "Has Defects?", "Has DTCs?"]


test=driver.find_elements(By.XPATH,'//*[@class="MuiFormLabel-root MuiInputLabel-root label MuiInputLabel-formControl MuiInputLabel-animated"]')
time.sleep(2)
for zz in range (len(test)):
    print(test[zz].text)
    if test[zz].text in InspectionsList:
        FuncationFile.writeFile("PASSED: Found "+ test[zz].text+" in the Inspection Filter ")
    else:
        FuncationFile.writeFile("FAILED found "+test[zz].text+" NOT part of the Inspection Filter")


#### Testing of Aggregates
# opening section
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[4]/div[1]/div[2]').click()
time.sleep(2)
tables=["Inspections", "Inspectors","Vehicles","Safe","Unsafe","Has DTC"]
test=driver.find_elements(By.XPATH,'//*[@class="Report__AggregatesCard__table"]')
time.sleep(2)
for xx in range (len(tables)):
    for yy in range (len(test)):

        if tables[xx] in test[yy].text:
            FuncationFile.writeFile("PASSED: Found "+ tables[xx]+" in the Aggregates")


### Checking Table headings
element2=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[3]/div[4]/div/div[5]/div[1]/div[1]/div[3]/button').click()
time.sleep(2)
element2=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/ul/li[2]').click()

#test=driver.find_elements(By.XPATH,'//*[@class="ag-header ag-pivot-off"]')
oneoff =driver.find_elements(By.XPATH,'//*[@class="MuiTreeView-root ToggleTree__tree"]')

print (len(oneoff))
for pp in range (len(oneoff)):
    print (oneoff[pp].text)



print("here")



driver.close()           