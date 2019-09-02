from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from collections import OrderedDict
import time
import pandas as pd
import xlsxwriter

start = input('Please enter a start date of the form (dd month yyyy):\n').split()
day, month, year = start

url = 'https://www.dsebd.org/data_archive.php'

driver = webdriver.Firefox()
driver.get(url)

df = pd.read_excel(r'C:\Users\alovy\Python\Python37-32\Projects\Maslin Capital\TRADECODE.xlsx','Sheet1')
tradecodes = df['TRADECODE'].values.tolist()
companies = tradecodes

dictionary = {}

for n in companies:
    if n == 'AL-HAJTEX':
        n = 'AL_HAJTEX'
    dictionary[n] = {}

for ticker in companies:

    Select(driver.find_element_by_id('ClosePDate_month')).select_by_visible_text(month)
    Select(driver.find_element_by_id('ClosePDate_day')).select_by_value(day)
    Select(driver.find_element_by_id('ClosePDate_year')).select_by_visible_text(year)

    Select(driver.find_element_by_id('ClosePDate1_month')).select_by_visible_text('January')
    Select(driver.find_element_by_id('ClosePDate1_day')).select_by_value('31')
    Select(driver.find_element_by_id('ClosePDate1_year')).select_by_visible_text('2019')
    
    tickers = driver.find_elements_by_id('Symbol')
    Select(tickers[2]).select_by_visible_text(ticker)

    driver.find_element_by_name('ViewClosePArchive').click()
    prices_html = driver.page_source

    soup = BeautifulSoup(prices_html,'html.parser')

    counter = 0
    list_prices = []
    list_dates = []
    if ticker == 'AL-HAJTEX':
        ticker = 'AL_HAJTEX'

    for number in soup.find_all('font', attrs = {'face':"Arial", 'size':"2"}):
        counter += 1
        if (counter + 3) % 5 == 0:
            list_dates.append(number.text)
        if (counter + 1) % 5 == 0:
            if number.text == '0':
                continue
            else:
                list_prices.append(number.text)
            
    for n in range(len(list_prices)):
        dictionary[ticker].update({list_dates[n]:list_prices[n]})

    driver.back()

masterlist = []

Select(driver.find_element_by_id('DayEndSumDate1_day')).select_by_value(day)
Select(driver.find_element_by_id('DayEndSumDate1_month')).select_by_visible_text(month)
Select(driver.find_element_by_id('DayEndSumDate1_year')).select_by_visible_text(year)
    
tickers = driver.find_elements_by_id('Symbol')
Select(tickers[0]).select_by_visible_text('GP')

driver.find_element_by_name('ViewDayEndArchive').click()
prices_html = driver.page_source

soup = BeautifulSoup(prices_html,'html.parser')

counter = 0
masterlist = []

for number in soup.find_all('font', attrs = {'face':"Arial", 'style':"size:11px;"}):
    counter += 1
    if (counter + 10) % 12 == 0:
        masterlist.append(number.text)
        

for k in companies:
    if k == 'AL-HAJTEX':
        k = 'AL_HAJTEX'
    for date in masterlist:
        if date in dictionary[k].keys():
            continue
        else:
            dictionary[k].update({date : 0})
    dictionary[k] = OrderedDict(dictionary[k])
    

workbook = xlsxwriter.Workbook('Close prices.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 1
    
for i in range(len(companies)):
    if companies[i] == 'AL-HAJTEX':
        companies[i] = 'AL_HAJTEX'
    for n in range(len(dictionary[companies[i]])):
        worksheet.write(row, col, 'Date')
        worksheet.write(row + 1 + n, 0, masterlist[n])
        worksheet.write(row, col, companies[i])
        worksheet.write(row + 1 + n, col, list(dictionary[companies[i]].values())[n])
    row = 0
    col += 1

workbook.close()
