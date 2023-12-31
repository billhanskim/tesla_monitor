from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')        # Head-less 설정
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


driver.get('https://www.naver.com')