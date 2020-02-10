from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(r'C:\ProgramData\chocolatey\bin\chromedriver.exe')

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
driver.get('http://www.youtube.com')
sleep(4)
search_box=driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys('Programmers song')
search_button=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
search_button.click()
sleep(3)
play=driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
play.click()
sleep(95)

driver.get('http://www.google.com')
g_search_box=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
g_search_box.send_keys('Thanks for watching')
sleep(2)
g_search_button=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
g_search_button.click()



