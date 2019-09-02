from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pandas as pd
import xlsxwriter


url = 'https://www.dsebd.org/data_archive.php'

driver = webdriver.Firefox()

driver.get('https://www.dsebd.org/data_archive.php')

dictionary = {}
df = pd.read_excel(r'C:\Users\alovy\Python\Python37-32\Projects\Maslin Capital\TRADECODE.xlsx','Sheet1')
companies = df['TRADECODE'].values.tolist()
#['AAMRANET', 'AAMRATECH']

for ticker in companies:
    day = Select(driver.find_element_by_id('ClosePDate_day'))
    day.select_by_value('03')

    month = Select(driver.find_element_by_id('ClosePDate_month'))
    month.select_by_visible_text('January')

    year = Select(driver.find_element_by_id('ClosePDate_year'))
    year.select_by_visible_text('2016')
    
    tickers = driver.find_elements_by_id('Symbol')
    Select(tickers[2]).select_by_visible_text(ticker)

    driver.find_element_by_name('ViewClosePArchive').click()
    prices_html = driver.page_source

    soup = BeautifulSoup(prices_html,'html.parser')

    n = 0
    counter = 0
    list_prices = []

    for number in soup.find_all('font', attrs = {'face':"Arial", 'size':"2"}):
        counter += 1
        if (counter + 1) % 5 == 0:
            list_prices.append(number.text)
            n += 1
            if ticker == 'AL-HAJTEX':
                ticker = 'AL_HAJTEX'
        dictionary[ticker] = list_prices

    driver.back()

workbook = xlsxwriter.Workbook('Close prices.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 1
    
for i in range(len(companies)):
    for n in range(len(dictionary[companies[i]])):
        worksheet.write(row, col, companies[i])
        worksheet.write(row + 1 + n, col, dictionary[companies[i]][n])
    row = 0
    col += 1

workbook.close()
