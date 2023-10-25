from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
# Initialize the Chrome driver


# Open YouTube and perform a search
def yt_search(user_input = 'enchanted by taylor swift'):
    driver = webdriver.Chrome()
    user_input = user_input.split(' ')
    del user_input[0]
    search = ' '.join(user_input)
    driver.get('https://www.youtube.com/')
    search_box = driver.find_element(By.NAME,'search_query')
    search_box.send_keys(search)
    search_box.send_keys(Keys.RETURN)

# Wait for the search results to load (you may need to adjust the time)
    time.sleep(8)

# Click the first video link
    video_links = driver.find_element(By.CLASS_NAME,'style-scope ytd-video-renderer')
    print(video_links)
    video_links.click()
    time.sleep(360*60)
    driver.quit()
# Close the browser
