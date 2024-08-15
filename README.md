# Telegram reminder bot
## Description
Simple telegram bot I use to create reminders for my future self. The script works only with russian language with using corresponding parser lib. For different language you shouldn't use it.

## Environment
There must be an API_TOKEN environment variable with your bot's api key for the script to work.  

## Libraries
To install all dependencies use:  
```
pip install -r requirements.txt
```
Used libraries:
 - aiogram — async telegram bot framework
 - scheduler — lib for jobs scheduling
 - rutimeparser — lib for parsing russian texts to extract datetime