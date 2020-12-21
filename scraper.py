from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import time
import threading

def main():
    # setting up the driver and sending a a get request to the url
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.thepfs.org/yourmoney/find-an-adviser')
    time.sleep(1)

    # selecting the search bar and filling it up and checking mortgages
    try:
        # waits until the page is loaded
        search_bar = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'advisorSearch')))
    except TimeoutException:
        print("Loading took too much time!")
    # search_bar = driver.find_element_by_id('advisorSearch')
    mortgages_checkbox = driver.find_element_by_xpath('//*[@id="search-filter-specialism"]/label[12]/input')
    mortgages_checkbox.click()
    search_bar.send_keys('London, UK')

    # direct click on the search button does not work so this procedure is used..
    time.sleep(2)
    down_arrow = Keys.DOWN
    enter_key = Keys.ENTER
    search_bar.send_keys(down_arrow)
    time.sleep(1)
    search_bar.send_keys(enter_key)
    time.sleep(1)
    search_bar.send_keys(enter_key)


    time.sleep(3)
    # Parsing with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # finding all the lists for finding person info
    all_persons = soup.find_all('li')

    # stores all the data
    all_data = dict()

    # iterates over the li items to find person info
    for person in all_persons:
        if person is not None:

            # all person info
            name = person.find('h3', class_='adviser-name')
            company = person.find('p', class_='adviser-company mod-content')
            phone = person.find('div', class_='yui3-u adv-item adv-telephone')
            email = person.find('div', class_='yui3-u adv-item adv-email')
            linked_in = person.find('div', class_='yui3-u adv-item adv-lnkIn')

            if name and phone and company:
                name, phone, company = name.text.strip(), phone.text.strip(), company.text.strip()
                all_data[name] = {'phone': phone, 'company': company}

            elif name and email and company:
                name, email, company = name.text.strip(), email.text.strip(), company.text.strip()
                all_data[name] = {'email': email, 'company': company}

            elif name and linked_in and company:
                name, linked_in, company = name.text.strip(), linked_in.text.strip(), company.text.strip()
                all_data[name] = {'linked_in': linked_in, 'company': company}


    print(all_data)


main()


