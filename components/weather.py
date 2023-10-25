from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # Necessary when running in headless mode
def weather_today():
    driver = webdriver.Chrome(options=chrome_options)
    search_url  = 'https://www.google.com/search?q=weather&rlz=1C1CHBD_enIN953IN953&oq=weather&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDIJCAEQIxgnGIoFMhYIAhAuGIMBGMcBGLEDGMkDGNEDGIAEMgoIAxAAGJIDGIoFMgoIBBAAGJIDGIoFMhAIBRAuGMcBGLEDGNEDGIAEMg0IBhAAGIMBGLEDGIAEMgoIBxAAGLEDGIAEMg0ICBAAGIMBGLEDGIAEMg0ICRAAGIMBGLEDGIAE0gEIMzE5OWoxajeoAgCwAgA&sourceid=chrome&ie=UTF-8#ip=1'
    driver.get(search_url)
    driver.implicitly_wait(5)
    degrees = driver.find_element(By.CLASS_NAME, 'wob_t')
    degrees_number = degrees.text
    degrees_number = int((int(degrees_number) - 32) * 5/9)
    degrees_number = str(degrees_number) + '°C'
    today = driver.find_element(By.ID, 'wob_dts')
    today_is = today.text
    sky = driver.find_element(By.ID, 'wob_dc')
    sky_is = sky.text
    result = []
    result.append(degrees_number)
    result.append(today_is)
    result.append(sky_is)
    return ' '.join(result)
    