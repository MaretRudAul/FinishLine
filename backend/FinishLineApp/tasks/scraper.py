from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def scrape_anchorlink():
    BUTTON_CLICK_TIMES = 0
    TIME_OUT = 10
    driver = webdriver.Chrome()
    driver.get("https://anchorlink.vanderbilt.edu/events")

    # Set up wait and timeout length
    wait = WebDriverWait(driver, TIME_OUT) 

    def hit_buttton(): 
        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button div div")))
        for i in range(BUTTON_CLICK_TIMES):
            button.click()
            time.sleep(0.25)
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    hit_buttton()

    event_count = len(driver.find_elements(By.CLASS_NAME, "MuiCard-root"))
    data = []
    for i in range(event_count):
        events = driver.find_elements(By.CLASS_NAME, "MuiCard-root")
        event = events[i]
        title = event.find_element(By.CSS_SELECTOR, "div span h3").text
        

        image_style = event.find_element(By.CSS_SELECTOR, 'div[role="img"]').get_attribute("style")
        try:
            image_url = re.search(r'https:.*\.*\?', image_style).group(0)[:-1]
        except AttributeError:
            # TODO: Insert default image
            image_url = "Default Image Used"

        # Click into event to get description
        wait.until(EC.element_to_be_clickable(event))
        event.click()
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        date_loc_and_desc = driver.find_elements(By.TAG_NAME, "p")
        date_string = date_loc_and_desc[0].text
        location = date_loc_and_desc[2].text
        desc = date_loc_and_desc[3].text

        link = driver.current_url

        hosts_web_elements = driver.find_elements(By.CSS_SELECTOR, 'div div h3')
        hosts = ", ".join([host.text for host in hosts_web_elements])


        driver.back()
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        hit_buttton()

        data.append({
            "title": title,
            "date": date_string,
            "location": location,
            "image_url": image_url,
            "desc": desc,
            "link": link,
            "host": hosts,
            "tags": '', 
            "origin": 'Anchorlink',
        })


    driver.close()

    return data
