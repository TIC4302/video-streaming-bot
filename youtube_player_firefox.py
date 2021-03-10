import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

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

## original df before randomise           ##
## read in an output.csv of scraped links ##
df = pd.read_csv('output.csv', index_col=None)
titles = df['Titles']
url = df['URL']
playtime = df['Time']
numberOfTitles = len(df)
print("df before randomise")
for i in range(0, numberOfTitles):
    print(titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i] )


## df after randomised                    ##
## randomise rows of Titles and URL links ##
df = df.sample(frac=1).reset_index(drop=True)
titles = df['Titles']
url = df['URL']
playtime = df['Time']

## print titles, links, time and random play video in the df list ##
playtimeRandom=[]
print("\ndf after randomised")
for i in range(0, numberOfTitles):
    playtimeRandom.append( randomTimeGenerator( playtime[i] ) )
    print(titles[i].encode('unicode-escape').decode('utf-8'), url[i], playtime[i], playtimeRandom[i])

####  headless geckodriver  ##
options = Options()
options.add_argument('--headless') 

driver = webdriver.Firefox(options=options)

## play video from random url and with random play time ##

for i in range(0, numberOfTitles):
    print("\nTitles:", titles[i])
    print("URL:", url[i])
    print("Playtime:", playtime[i] )
    print("Random playtime:", playtimeRandom[i])
    driver.get(url[i])
    time.sleep(1)
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) #hits space
    time.sleep(1)
    video.send_keys(Keys.SPACE) #hits space
    time.sleep(playtimeRandom[i])
    #time.sleep(1)
    video.click()               #mouse click
    #time.sleep(1)
    
driver.quit()                   #quit browser
