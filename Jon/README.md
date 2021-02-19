# To Do List

## Provisioning of Docker Images and Monitoring (Module A)

- [x] Create a basic docker image (ubuntu)
- [x] Create initialization script
- [x] Launch docker GUI with Firefox
- [ ] Provide a mechanism to bring up N number docker instances based on user's input via python scripts [**Derrick**]
- [ ] Provide a mechanism for user to provide input on the landing page (TBD) 
- [ ] Provide a mechanism to on how long to play a particular video streaming based on user's input via python scripts (in the length of minutes) [**Derrick**]

- [ ] Ensure docker GUI can be launched 

- [ ] Ensure ansible, and selenium is installed in the environment

- [ ] Ensure automation of Docker and monitoring via Kubernetes

  

## YouTube Play Bot (Module B) - (one sub module: **Kok Suan**)

This module will be executing play command on a randomized length (between 1-5 minutes. Configurable via configuration file)

- [ ] module to check length of Video and ensure the randomize length of play does not exceed length of video (otherwise play of video will not be continuous).

- [ ] module to play video (without skipping ads)

- [ ] nice to have functionality: write into output file the url of the video played and the length of the video played, including time stamp logs in a directory shared with the container host.

  Example of the logs: 

  2021-02-16 19:30:21 - Play https://www.youtube.com/watch?v=VKf4A-VPBfc for 2 minutes

  2021-02-16 19:30:23 - Start to Play https://www.youtube.com/watch?v=dRARDe5NT0I for 4 minutes

  

## Scrap YouTube Playlist module (Module C) - **Kok Suan**

- [ ] Scrap Youtube page and take a list of links with "/watch?v=" keywords

  example: https://www.youtube.com/watch?v=VKf4A-VPBfc

- [ ] at least 5-10 links should be extracted from the page

- [ ] scrapping module should be able to scrape two types of pages, main YouTube page (where links of videos are in the main page) and specific YouTube page (where links of videos are on the right).

- [ ] Upon reaching the end of the links extracted, it will automatically scrap the subsequent 5-10 links

- [ ] Writing list of the links obtain from scrap and write into log files for debug or information purposes. Log files to be written to a directory shared with the container host.

  Example:

  2021-02-16 19:20:35 - Extracted 10 video playlist 

  https://www.youtube.com/watch?v=VKf4A-VPBfc 

  https://www.youtube.com/watch?v=EENcwlwCMQE 

  ...etc

  

## Main Python Module (Module D) - **Jon**

- [ ] To process user input
  - Process number of docker instances to launch
  - Process number of Play time
  - Process capturing the URL information
- [ ] Create a folders based on number of instances (to store logs and statuses)
- [ ] Check timing and generate output from each docker instances
- [ ] Stop docker and destroy docker instances once time is up



## Validation and Verification of Running Instances (Testing - Module E)

- [ ] Each running instance will have a directory created, ie "runYYYYMMDDHHmmss"

- [ ] Within this directory it will contain a list of folders (according to the number of instance)

  for example, Python3 main.py --instance 4 --playtime 300 --page "file.txt"

  This means, user would like to run 4 docker instance, and play a random YouTube stream for 300 minutes (5 hours)

  file.txt will contain the first landing page of the youtube. It will be:

  - https://www.youtube.com/ (main YouTube Page)
  - https://www.youtube.com/watch?v=EENcwlwCMQE (specific video landing page - video links on the right side)

- [ ] Each of the running docker instance will run independently, ie, scrap its own page and play YouTube video stream in a randomized play length for each YouTube Video. 



## Implementation of Container instances using Kubernetes

- [ ] Use kubectl and other means to monitor the health of each instances



## Implementation of Network Usage Statistics (Module F)

- [ ] Provide a mechanism to capture network statistics via vnStat and/or other means




## Documentation Update

Each team member to update their documentation on the module they work on and to be integrated thereafter.