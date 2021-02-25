## Testing Plan for Video Streaming Bot

Ensure environment is setup with ubuntu 20.04 and Python3.8 is installed including the relevant python packages. Below steps are pre-requisites to install Python3 on Ubuntu. Follow each of the steps below

- sudo apt-get install software-properties-common

- sudo add-apt-repository ppa:deadsnakes/ppa

- sudo apt-get update

- sudo apt-get install python3.8

- sudo apt install -y python3-pip

- sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

- sudo apt install -y python3-venv

  

#### Test Case:  01 - Python Environment Test

Description: Pre-requisites validation
 Steps (if any):

- Clone the repository: git clone https://github.com/TIC4302/video-streaming-bot.git
- Navigate to test directory, 001 folder: cd test/001
- Execute "test.py" by running python3 : python3 test.py

Input: <NA>
Expected Output: 
3.8.5 (default, Jul 28 2020, 12:59:40)
[GCC 9.3.0]

#### 

#### Test Case:  02 - Usage of Main.py

Description: To test main functionality of program to show usage o

- Run python3 main.py with -h arguments

Input: -h
Expected Output: 

Usage:
test.py -i <number of instance> -l <length of play time>

Options:
-i, --inst       : specify number of docker instance to run
-l, --lplay      : specify length of play time to run in minutes
-u, --url        : specify url page or first landing page