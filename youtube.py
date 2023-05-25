import time, os
import re
import csv
from datetime import datetime, timedelta
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


load_dotenv()


def get_data(song_name):
    try:
        driver_path = os.getenv('DRIVER_PATH')
        website_url = os.getenv('WEBSITE_URL')
      
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-dev-shm-usage')
       
        browser = webdriver.Chrome(driver_path, chrome_options=chrome_options)
        browser.get("https://www.youtube.com/watch?v=zGPJkcWjgbM")
        time.sleep(5)

       
        # browser.find_element(By.CLASS_NAME, "s7ugfhf").send_keys(song_name)
        browser.find_element(By.CLASS_NAME, "ytp-play-button").click()

        # search_page_html = browser.page_source
        # soup = BeautifulSoup(search_page_html, features="html.parser")
        # contents = soup.find('div',class_="r1sfefmq").find("section").find_all("a")
        pog = browser.find_element(By.ID, "info")
        print("POG", pog)
        randomNumber = random.randint(5, 10)
        print("Random number", randomNumber)

        for i in range(0, randomNumber):
            browser.find_element(By.CLASS_NAME, "ytp-play-button").click()
            random_sec = random.randint(2, 5)
            time.sleep(random_sec)

        print("FINISHED")

        # time.sleep(2)

        # # Choosing based upon whether the song is already chordified

        # search_page_html = browser.page_source
        # soup = BeautifulSoup(search_page_html, features="html.parser")
        # contents = soup.find('div',class_="r1sfefmq").find("section").find_all("a")

        # for id, content in enumerate(contents):
        #     is_chordified = content.find("span", class_="slvxdu2").string

        #     if is_chordified == "Chordified":
        #         link = browser.find_element_by_xpath(f"//div[contains(@class, 'r1sfefmq')]/section/a[{id+1}]")
        #         link.click()
        #         break

        # time.sleep(3)

        # iframe1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'https://as.cloudfastcdn.net/youtube_embed.html?20220623')]")))
        # print("iframe1", iframe1)
        # browser.switch_to.frame(iframe1)

        # iframe = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'youtube.com')]")))
        # browser.switch_to.frame(iframe)

        # play_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Play']")))
        # play_button.click()

        # browser.switch_to.default_content()




        # play_button = browser.find_element_by_xpath(f"//iframe[@id='embedWrapper']")
        # play_button = browser.find_element_by_xpath(f"//button[contains(@class, 'ytp-large-play-button')]")
        # play_button.click()

        # time.sleep(10)
        
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
    views = random.randint(11, 15)
    print("The views will hopefully be increased by:", views)
    
    for i in range(1, views):
        th = threading.Thread(target=concurrentFunction, args=(i, i,))
        th.start()

    with open('youtube.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        count = int(next(reader)[0])

    count += views

    # Write the new count to the CSV file
    with open('youtube.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([count])
   
        
