import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

#page_url="https://www.youtube.com/playlist?list=PL3D7BFF1DDBDAAFE5"
page_url="https://www.youtube.com/results?search_query=hacked"
driver = webdriver.Chrome()

driver.get(page_url)
time.sleep(2)  

for i in range(0,1):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5)

#block1 = driver.find_elements_by_xpath("//div[@id='dismissible'] | //*[@id='video-title']")
block1 = driver.find_elements_by_xpath('//*[@id="video-title"]')
titles = []
links = []
for i in block1:
    titles.append(i.get_attribute('title'))
    links.append(i.get_attribute('href'))

wait = WebDriverWait(driver, 10)
run_time = []
for i in links:
    driver.get(i)
    wait_for_loading = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration")))
    block2=driver.find_element_by_css_selector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration")
    #block2=driver.find_element_by_xpath('//*[@id="movie_player"]/div[27]/div[2]/div[1]/div[1]/span[3]')
    run_time.append(block2.text)

## reassign arrays to remove blank data if any ##
titles_actual = []
links_actual = []
run_time_actual = []
length = len(titles)
for i in range(0,length):
    if titles[i]=="" or links[i]=="" or run_time[i] =="":
        pass
    else:
        titles_actual.append( titles[i] )
        links_actual.append( links[i] )
        run_time_actual.append( run_time[i] )

## use new arrays to form dictionary ##
dict = { 'Titles':titles_actual, 'URL':links_actual, 'Time':run_time_actual  }
df = pd.DataFrame(dict)

write_file = "output.csv"
with open(write_file, "w") as output:
    df.to_csv(output,na_rep="")
