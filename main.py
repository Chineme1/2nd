import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scrape_main import MAIN_SCRAPER
from upload import packIT


'''
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.neuralnine.com/books'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

headings = soup.find_all('h2', {'class': 'elementor-heading-title'})

for heading in headings:
    print(heading.getText())


time.sleep(10)
'''


print(packIT(MAIN_SCRAPER('https://umdearborn.campuslabs.com/engage/events')))

#Now it's time to pack it and upload it to Flask

#driver.quit()