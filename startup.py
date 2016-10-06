# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get('http://finder.startupnationcentral.org/startups')

try:
	#element = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "intercom-container"))
    #)
    for pages in range(1,30):
    	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    	time.sleep(1)
    element = WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script("return jQuery.active == 0")
    )
#wait.until(lambda driver: driver.execute_script("return jQuery.active == 0"))

finally:
	html = driver.page_source
	soup = BeautifulSoup(html,'lxml')

	for lvl1 in soup.find_all("div", class_="filter-search-results"):
		for lvl2 in lvl1.find_all("div", class_="companies-view "):
			for company in lvl2.find_all("a", class_="company-card__info"):
				print 'http://finder.startupnationcentral.org/startups'+company.attrs['href']
			#for descr in lvl2.find_all("p", class_="company-card_desription"):
			#	print descr.text
	print 'Done'	


	
