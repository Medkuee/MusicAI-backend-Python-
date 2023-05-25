import time, os
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading


load_dotenv()


def get_data(song_name):
    try:
        driver_path = os.getenv('DRIVER_PATH')
        website_url = os.getenv('WEBSITE_URL')
      
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
       
        browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        browser.get(website_url)
        time.sleep(1)
       
        browser.find_element(By.CLASS_NAME, "s7ugfhf").send_keys(song_name)
        browser.find_element(By.CLASS_NAME, "s1jkewg4").click()
        time.sleep(2)

        # Choosing based upon whether the song is already chordified

        search_page_html = browser.page_source
        soup = BeautifulSoup(search_page_html, features="html.parser")
        contents = soup.find('div',class_="r1sfefmq").find("section").find_all("a")

        for id, content in enumerate(contents):
            is_chordified = content.find("span", class_="slvxdu2").string

            if is_chordified == "Chordified":
                link = browser.find_element_by_xpath(f"//div[contains(@class, 'r1sfefmq')]/section/a[{id+1}]")
                link.click()
                break

        time.sleep(10)
        
    except Exception as e:

        print(
            "-----------------------\n",
            "ERROR: An error occured\n", 
            "MESSAGE:", f'{e}\n',
            "-----------------------\n"
        )

def concurrentFunction(media=None, column_names=None):
    get_data(media)

if __name__ == '__main__':
    song_names = ['coldplay everglow', "coldplay hymn for the weekend", 'coldplay viva la vida']
    for song_name in song_names:
        th = threading.Thread(target=concurrentFunction, args=(song_name, song_name,))
        th.start()
