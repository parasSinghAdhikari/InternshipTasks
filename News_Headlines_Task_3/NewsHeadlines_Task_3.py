
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException


NEWS_URL = "https://indianexpress.com/"
TOP_HEADLINES_OUTPUT_FILE = "news_topheadlines.txt"
LATEST_HEADLINES_OUTPUT_FILE = "news_latestheadlines.txt"
HEADLINE_FUllXPATH = "/html/body/div[3]/div[6]/div/div[2]/div[5]"  
WAIT_TIME = 3


def save_to_file(headlines, filename,storyType):
    """Save list of headlines to a .txt file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"\t\t\t\t{storyType }\n")
        for idx, title in enumerate(headlines, 1):
            f.write(f"{idx}. {title}\n")


driver = webdriver.Chrome(service = Service("C:/Driver/chromedriver.exe"))
time.sleep(WAIT_TIME)
driver.get(NEWS_URL)
time.sleep(WAIT_TIME)



headlines = driver.find_element(By.XPATH,HEADLINE_FUllXPATH)
top = headlines.find_element(By.XPATH, "./div[1]").text.split("\n")
latest = headlines.find_element(By.XPATH, "./div[2]").text.split("\n")
temp = []
for i in range(0,len(top)):
    if top[i].isupper():
            continue
    temp.append(top[i])

if temp:
    save_to_file(t, TOP_HEADLINES_OUTPUT_FILE ,"TOP HEADLINES")
    print(f"Saved {len(top)} headlines to {TOP_HEADLINES_OUTPUT_FILE}")
else:
    print("No Top headlines found. Try updating the XPath for your chosen site.")
if latest:
    save_to_file(latest[1:], LATEST_HEADLINES_OUTPUT_FILE,"LATEST HEADLINES")
    print(f"Saved {len(latest)-1} headlines to {LATEST_HEADLINES_OUTPUT_FILE}")
else:
    print("No Latest headlines found. Try updating the XPath for your chosen site.")
driver.quit()





