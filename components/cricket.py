from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Necessary when running in headless mode

# Initialize the Chrome driver with the specified options

def cricket_score():
    driver = webdriver.Chrome(options=chrome_options)
    search_url = 'https://www.hindustantimes.com/cricket/live-score'
    driver.get(search_url)
    driver.implicitly_wait(5)
    title = driver.find_element(By.CLASS_NAME, 'predic-head')
    title_text = title.text
    team_score = driver.find_elements(By.CLASS_NAME, 'team-score')
    scores = []
    for x in team_score:
        team_score_text = x.text
        scores.append(team_score_text)
    return title_text + ' ' +str(scores[0] + '-' + scores[1] + scores[2] + '-' + scores[3])
