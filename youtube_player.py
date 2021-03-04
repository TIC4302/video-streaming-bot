import csv
import pandas as pd

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

    minTime = 10
    maxTime = 300

    if time <= minTime:
        randomTime = time
    elif time <= maxTime:
        randomTime = random.randint(minTime,time)
    else:
        randomTime = random.randint(minTime,maxTime)

    return randomTime



######################
####                                    ####
####      Main Program        ####
####                                    ####
######################

#### Create a new testing file                ##
#### comment out if using existing output.csv ##
##titles=['80km Singapore Cycling Route','Casually Explained: Cycling','Epic Cycling on Ice']
##links=['https://www.youtube.com/watch?v=UHu7GW4_bOY','https://www.youtube.com/watch?v=5EE8m8mmq1k','https://www.youtube.com/watch?v=y_bwKW6V1lw']
##dict={ 'Titles':titles, 'URL':links}
##df = pd.DataFrame(dict)
##df.to_csv("output.csv", na_rep='', index=False)

## original df before randomise           ##
## read in an output.csv of scraped links ##
df = pd.read_csv('output5.csv', index_col=None)
titles = df['Titles']
url = df['URL']
time = df['Time']
numberOfTitles = len(df)
print("df before randomise")
for i in range(0, numberOfTitles):
    print(titles[i], url[i], time[i] )

## df after randomised                    ##
## randomise rows of Titles and URL links ##
df = df.sample(frac=1).reset_index(drop=True)
titles = df['Titles']
url = df['URL']
time = df['Time']
print("\ndf after randomised")


## print titles, links, time and random play video in the df list ##
playTime_random=[]
for i in range(0, numberOfTitles):
    playTime_random.append( randomTimeGenerator( time[i] ) )
    print(titles[i], url[i], time[i], playTime_random[i])


## play video from random url and with random play time ##
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()

for i in range(0, numberOfTitles):
    driver.get(url[i])
    time.sleep(2)
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE) #hits space
    time.sleep(1)
    video.click()               #mouse click
    ####need to find video runtime
    ##block = driver.find_element_by_xpath('//*[@id="overlays"] / ytd-thumbnail-overlay-time-status-renderer / span')
    ##run_time = block.get_attribute('aria-label')
    #time.sleep(playTime_random[i])    ## random play time

## to be deleted ##
##play_time = "1:9:30"
##randomTime = randomTimeGenerator( play_time )
##print("\nRandom play time generated :", randomTime, "seconds")




