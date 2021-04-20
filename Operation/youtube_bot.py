#################################
####                         ####
####      youtube-bot.py     ####
####                         ####
#################################

import os
import re
import random
import sys
import time
import string
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException

####################################
## Function randomTimeGenerator() ##
##################################################################
## randomise play time between minTime to maxTime               ##
## if play time <= minTime then randomTime = actual play time   ##
## if play time >= maxTime then play time = maxTime             ##
##################################################################
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

###############################
####                       ####
####    Scraper program    ####
####                       ####
#############################################
## Program arguments                       ##
## allow the following:                    ##
## search term    : string without space   ##
## no. of webpage : int                    ##
#############################################
arguments = len(sys.argv) - 1

## default values if no user input ##
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

driver = webdriver.Firefox(options=options, service_log_path=os.devnull)

profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")

page_url="https://www.youtube.com/results?search_query="+query

driver.get(page_url)
time.sleep(1)  

print("Scraping.....") 
for i in range(0,webpage):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    print("Webpage:",i+1 )
    time.sleep(5)


block1 = driver.find_elements_by_xpath('//a[@id="video-title"][@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
titles = []
links = []
for i in block1:
    titles.append(i.get_attribute('title'))
    links.append(i.get_attribute('href'))

block2 = driver.find_elements_by_xpath('//*[@id="badges"]')
badges = []
for i in block2:
    badges.append(i.text)

block3=driver.find_elements_by_css_selector("#overlays > ytd-thumbnail-overlay-time-status-renderer > span")
playtime = []
for i in block3:
    playtime.append(i.get_attribute('aria-label'))

#### debug purpose ##
##print(len(titles))
##print(len(links))
##print(len(playtime))
##print(len(badges))

## reassign arrays to remove blank data if any ##
## remove video that is LIVE                   ##
titles_actual = []
links_actual = []
#playtime_actual = []
length = len(titles)
for i in range(0,length):
    if badges[i].find("LIVE")>=0:
        pass
    else:
        titles_actual.append( titles[i] )
        links_actual.append( links[i] )
        #playtime_actual.append( playtime[i] )

while len(playtime) > len(titles):
    del playtime[-1];
    
if len(titles) != len(playtime):
    driver.quit()
    print("Bot experiencing trouble scrapping Youtube.")
    print("Please refine your query and try again.")
    print("Bot terminating.....\n")
    sys.exit()

## use new arrays to form dictionary ##
dict = { 'Titles':titles_actual, 'URL':links_actual, 'Time':playtime }
df = pd.DataFrame(dict)

############################
####                    ####
####   Player Program   ####
####                    ####
############################################
## Infinite loop to play list of videos,  ##
## randomisation after every end of loop. ##
## Crtl-C to end loop.                    ##
############################################

## List of videos before randomise  ##
#df = pd.read_csv('output.csv', index_col=None)
titles = df['Titles']
url = df['URL']
playtime = df['Time']
numberOfTitles = len(df)
print("Youtube titles before randomise")
for i in range(0, numberOfTitles):
    print(str(i+1)+".",titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i] )

try:
    while True:
        ## List of videos after randomised  ##  
        df = df.sample(frac=1).reset_index(drop=True)
        titles = df['Titles']
        url = df['URL']   
        playtime = df['Time']
           
        ## print titles, links, time and random play in the video list ##
        playtimeRandom=[]
        print("\nYoutube titles after randomised")
        for i in range(0, numberOfTitles):
            playtimeRandom.append( randomTimeGenerator( playtime[i] ) )
            print(str(i+1)+".", titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i], playtimeRandom[i])

        ## play video from random url and with random play time ##
        #numberOfTitles
        for i in range(0, numberOfTitles):
            print();
            print("No. "+str(i+1)+":");
            print("Title:", titles[i].encode('unicode-escape').decode('utf-8'))
            print("URL:", url[i])
            print("Playtime:", playtime[i] )
            print("Random playtime:", playtimeRandom[i],"secs")
            driver.get(url[i])
            if driver.find_element_by_css_selector('.ytp-play-button').get_attribute('aria-label')=="Play":
                driver.find_element_by_css_selector('.ytp-play-button').click()
            #video = driver.find_element_by_id('movie_player')
            #video.click()               #mouse click
            #time.sleep(1)
            #driver.save_screenshot('./image'+str(i)+'.png')
            #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.ytp-mute-button')))
            #print(driver.find_element_by_css_selector('.ytp-mute-button').get_attribute('aria-label'))
            if driver.find_element_by_css_selector('.ytp-mute-button').get_attribute('aria-label')=="Mute (m)":
                ##print("Original mute")
                driver.find_element_by_css_selector('.ytp-mute-button').click()
            else:
                ##print("Now mute")
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

print("\nThank you for using Youtube-bot. Bye !!")
