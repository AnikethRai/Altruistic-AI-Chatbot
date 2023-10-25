from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Initialize the Chrome WebDriver


def google_search(user_input = 'google'):
    driver = webdriver.Chrome()
    user_input = user_input.split(' ')
    del user_input[0]
    search = ' '.join(user_input)

    search_url = f"https://www.google.com/search?q={search}"
    driver.get(search_url)
    time.sleep(60)
    driver.quit()
# Close the browser
