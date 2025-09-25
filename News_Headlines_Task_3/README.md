# News Headlines Scraper
This project is a Python script that uses Selenium WebDriver to automatically scrape both the "Top Headlines" and "Latest Headlines" from the Indian Express news site. The scraped headlines are saved to numbered .txt files in your project directory for easy viewing.

## Features
Scrapes top and latest headlines from Indian Express

Writes headlines to neatly formatted text files (newstopheadlines.txt and newslatestheadlines.txt)

Structured, commented Python code for learning and easy improvement

Handles basic errors and prints useful messages

## Prerequisites
Before running the script, make sure you have:

Python 3.7 or newer installed

Google Chrome browser

Selenium installed (pip install selenium)

ChromeDriver for your version of Chrome (download here), placed in the project folder or adjust the script path

## How to Use
Download or clone this project, ensuring the script file and chromedriver.exe are in the same folder.

Open a terminal in the project folder.

Install Python requirements if needed:

bash
pip install selenium
Run the script:

bash
```
python NewsHeadlines_Task_3.py
When finished, you will find two output files:
newstopheadlines.txt (Top headlines)
```
newslatestheadlines.txt (Latest headlines)

## Customizing for Other News Sites
Change the values of NEWSURL and the XPath variables in the script to target a different news site or news section.

Adjust output filenames if desired.

Example Output
newstopheadlines.txt

text
TOP HEADLINES
1. India's G20 presidency brings global focus
2. Supreme Court delivers landmark verdict
...
newslatestheadlines.txt

text
LATEST HEADLINES
1. Markets rally after economic announcement
2. Major rainfall predicted this week
...
## Troubleshooting
No headlines found?
The website layout may have changed. Check and update the XPath in the script.

Driver errors?
Make sure ChromeDriver matches the installed Chrome version, and that it's in your project folder.

Write errors?
Make sure you have permission to write files in the project directory.

## License
Open-source and free for educational or non-commercial use.