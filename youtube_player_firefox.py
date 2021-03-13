import os
import csv
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

## Function randomTimeGenerator()
##   randomise play time between minTime to maxTime               ##
##   if play time <= minTime then randomTime = actual play time   ##
##   if play time >= maxTime then play time = maxTime             ##
def randomTimeGenerator( play_time ):
    import re
    import random
    num = re.findall('[0-9]+', play_time)
    length = len(num)
    time = 0    # convert play time into seconds
    if length==3:
        time = int(num[0])*60*60 + int(num[1])*60 + int(num[2])
    if length==2:
        time = int(num[0])*60 + int(num[1])
    if length==1:
        time = int(num[0])

    minTime = 5
    maxTime = 20

    if time <= minTime:
        randomTime = time
    elif time <= maxTime:
        randomTime = random.randint(minTime,time)
    else:
        randomTime = random.randint(minTime,maxTime)

    return randomTime


##########################
####                  ####
####   Main Program   ####
####                  ####
##########################

####  headless geckodriver  ##
options = Options()
options.add_argument('-headless') 

driver = webdriver.Firefox(options=options, service_log_path=os.devnull)

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")

## original df before randomise           ##
## read in an output.csv of scraped links ##
df = pd.read_csv('output.csv', index_col=None)
titles = df['Titles']
url = df['URL']
playtime = df['Time']
numberOfTitles = len(df)
print("Youtube titles before randomise")
for i in range(0, numberOfTitles):
    print(titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i] )

try:
    while True:
        ## df after randomised                    ##        
        ## randomise rows of Titles and URL links ##
        df = df.sample(frac=1).reset_index(drop=True)
        titles = df['Titles']
        url = df['URL']   
        playtime = df['Time']
           
        ## print titles, links, time and random play video in the df list ##
        playtimeRandom=[]
        print("\nYoutube titles after randomised")
        for i in range(0, numberOfTitles):
            playtimeRandom.append( randomTimeGenerator( playtime[i] ) )
            print(titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i], playtimeRandom[i])

        ## play video from random url and with random play time ##

        for i in range(0, numberOfTitles):
            print("\nTitle:", titles[i])
            print("URL:", url[i])
            print("Playtime:", playtime[i] )
            print("Random playtime:", playtimeRandom[i],"secs")
            driver.get(url[i])
            #time.sleep(1)
            #driver.save_screenshot('./image'+str(i)+'.png')
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.ytp-mute-button')))
            #print(driver.find_element_by_css_selector('.ytp-mute-button').get_attribute('aria-label'))
            if driver.find_element_by_css_selector('.ytp-mute-button').get_attribute('aria.label')=='Mute (m)':
                #print("Original mute")
                driver.find_element_by_css_selector('.ytp-mute-button').click()
            else:
                #print("Now mute")
                pass
            #video = driver.find_element_by_id('movie_player')
            #video.send_keys(Keys.SPACE) #hits space
            #video.click()               #mouse click
            time.sleep(playtimeRandom[i])
except KeyboardInterrupt:
    pass

except TimeoutException:
    print("Loading took too long....")

except Exception as e:
    print("Encounter error:", e)

driver.quit()                   #quit browser

print("\nThank you for using video-bot. Bye !!")

