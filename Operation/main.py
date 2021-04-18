import selenium
from selenium import webdriver as wb
import sys, getopt
from urllib.parse import urlparse

def launchFirefox(url, webbrowser):
    #webb=wb.Firefox(executable_path=r'C:\programdata\Anaconda3_JKExtra\geckodriver-v0.29.0-win64\geckodriver.exe')
    webb=wb.Firefox(executable_path=r'C:\programdata\Anaconda3_JKExtra\geckodriver-v0.29.0-win64\geckodriver.exe')
    #webb.get('https://www.youtube.com')
    webb.get(url)
    print('Title: %s' % webb.title)
    webb.quit()

# To scrap YouTube videos from a given URL
# return list of First Level video URLs
def ScrapWeb(url):
    #print('test')
    return

#play youtube a single YouTube video for a random time
def PlayURL(url):
    return

def generateRandomTime():
    return

# Print the help/usage of the main.py
def printusage():
    print('Usage: ')
    print('test.py -i <number of instance> -l <length of play time>')
    print('')
    print('Options: ')
    print('-i, --inst       : specify number of docker instance to run')
    print('-l, --lplay      : specify length of play time to run in minutes')
    print('-u, --url        : specify url page or first landing page')
    return

def verifySyntax(instance, lplay, url):
    #instance and lplay has to be numeric above 0
    if instance.isnumeric() == True:
        if int(instance) <= 0:
            print('number of instance should be greater than 0')
            sys.exit(3)
    else:
        print('number of instance should be numeric and greater than 0')
        sys.exit(4)

    if lplay.isnumeric() == True:
        if int(lplay) <=0:
            print('length of play time should be greater than 0')
            sys.exit(5)
    else:
        print('length of play time should be numeric and greater than 0')
        sys.exit(6)

    parsed_url = urlparse(url)
    if bool(parsed_url.scheme) == False:
        print('Invalid URL parsed')
        sys.exit(7)

    # call instantiate docker etc
    return

def callDocker():
    # create X number of landing page for each docker instance
    # 1.url, 2.url, 3.url
    # Call Docker run for each instance and provide file to be copied to each docker instance
    # files to be copied are: 1.url, videorun.py
    # call Docker to run docker instance
    return

def readConfig():
    # read configuration file
    return

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      #opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      opts, args = getopt.getopt(argv,"hi:l:u",["inst=","lplay=","url="])
   except getopt.GetoptError:
      printusage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         printusage()
         sys.exit()
      elif opt in ("-i", "--inst"):
         instancenum = arg
      elif opt in ("-l", "--lplay"):
         lentime = arg
      elif opt in ("-u","--url"):
         playurl = arg
   print ('Number of Instance :', instancenum)
   print ('Length of Play Time is :', lentime)
   print ('Play URL is :', playurl)

   verifySyntax(instancenum, lentime, playurl)

if __name__ == "__main__":
   main(sys.argv[1:])

