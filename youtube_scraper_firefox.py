###############################
####                       ####
####      Main Program     ####
####                       ####
###############################

import sys
import csv
import time
import string
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

## system argument                      ##
## allow the following                  ##
## search term : string without space   ##
## no. of webpage : int                 ##
arguments = len(sys.argv) - 1

## default ##
query = "cycling"
webpage = 1

if arguments>=1:
    print("Your request:")
    query = sys.argv[1]
    print("Query:", query)
    if arguments==2:
        if (sys.argv[2]).isnumeric():
            if int(sys.argv[2])>=1 and int(sys.argv[2])<=20: 
                webpage = int( sys.argv[2] )
                print("Number of webpage:", webpage)

##  headless geckodriver  ##
options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

page_url="https://www.youtube.com/results?search_query="+query

driver.get(page_url)
time.sleep(1)  

print("Scraping.....") 
for i in range(0,webpage):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    print("Webpage:",i+1 )
    time.sleep(5)

#block1 = driver.find_elements_by_xpath('//div[@id="title-wrapper"]//a[@id="video-title"]')
block1 = driver.find_elements_by_xpath('//a[@id="video-title"][@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
#block1 = driver.find_elements_by_css_selector('#video-title > a.yt-simple-endpoint.style-scope.ytd-video-renderer')
#block1 = driver.find_elements_by_css_selector('ytd-item-section-renderer.style-scope:nth-child(1) > div:nth-child(3) > ytd-video-renderer:nth-child(16) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)')
titles = []
links = []
for i in block1:
    titles.append(i.get_attribute('title'))
    links.append(i.get_attribute('href'))

#block2 = driver.find_elements_by_xpath('//*[@id="badges"]//span')
block2 = driver.find_elements_by_xpath('//*[@id="badges"]')
badges = []
for i in block2:
    badges.append(i.text)

#block3=driver.find_elements_by_css_selector("#overlays > ytd-thumbnail-overlay-time-status-renderer > span")   
#block3=driver.find_elements_by_xpath('//span[@class="style-scope.ytd-thumbnail-overlay-time-status-renderer"]')
block3=driver.find_elements_by_css_selector("#overlays > ytd-thumbnail-overlay-time-status-renderer > span")
playtime = []
for i in block3:
    playtime.append(i.get_attribute('aria-label'))
    #playtime.append(i.text)

#### debug purpose ##
##print(len(titles))
##print(len(links))
##print(len(playtime))
##print(len(badges))

## reassign arrays to remove blank data if any ##
## remove video that is LIVE                   ##
titles_actual = []
links_actual = []
length = len(titles)
for i in range(0,length):
    if badges[i].find("LIVE")>=0:
        pass
    else:
        titles_actual.append( titles[i] )
        links_actual.append( links[i] )
        
## use new arrays to form dictionary ##
dict = { 'Titles':titles_actual, 'URL':links_actual, 'Time':playtime }
df = pd.DataFrame(dict)

write_file = "output.csv"
with open(write_file, "w") as output:
    df.to_csv(output,na_rep="")
