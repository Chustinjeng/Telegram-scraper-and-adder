# Telegram code for scraping members and adding them
This is a code for scraping members of a telegram group and adding them into another group (**NOTE**: please do not use this code to spam people or mass-add people, this code does not supercede Telegram's laws so please use it carefully. We are also not responsible for any illegal activity using this code.)

This code was taken from @th3unkn0n and edited accordingly.

## GENERATE API_ID AND API_HASH IN TELEGRAM
- Go to my.telegram.org and log in
- Click on API development tools and fill in the required fields (you don't have to do this properly because you are merely retrieving your account details)
- Copy "api_id" & "api_hash" after clicking create app ( will be used in setup.py )

## HOW TO USE

1. You need to have Python installed, just go to the Internet and install the latest version of Python
2. Download the zip of this file
3. Use command prompt/terminal to go to the directory of this code
```
cd/(Your Path)/Telegran-scraper-bot
```
4. Set up the program
```
python3 setup.py
```
- You would have to first choose "install", which will allow you to install all the relevant modules required for the program to run
- After installing, run this code again
```
python3 setup.py
```
- Choose "config" to set up your Telegram account (your api_id and api_hash and phone number needed)
5. Start scraping members
```
python3 scraper.py
```
- Name your csv file to your preference, this is where all the users' details would be added to
- Choose any group to scrape members from
6. Start adding members to groups
```
python3 add2group.py
```
- Can add members to any of your groups
- You can choose to name your new csv file, this is a new csv file **minus** all the new users added in the target group
- **Note**: The target group's privacy settings should be public and allow you to add members in

## Alternative
- The codes can also be converted to .exe files
- Install pyinstaller 
```
pip install pyinstaller
```
- Convert the codes to .exe files **(one by one)**
```
pyinstaller --onefile setup.py
pyinstaller --onefile scraper.py
pyinstaller --onefile add2group.py
```
- You can run the codes by simply clicking on the .exe files
