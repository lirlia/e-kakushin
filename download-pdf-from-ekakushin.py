import chromedriver_binary
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='./chromedriver')

url = "https://www0.e-kakushin.com/emember/servicetop.do?p=init"
driver.get(url)

company = ""
user = ""
password = ""

company_id = driver.find_element_by_id("customer-code")
company_id.send_keys(company)

user_id = driver.find_element_by_id("user-code")
user_id.send_keys(user)

password_id = driver.find_element_by_id("keyboard-output")
password_id.send_keys(password)

# click login button
login_button = driver.find_element_by_id("btn-login")
login_button.click()

time.sleep(1)

# click給与明細電子化サービス
login_button2 = driver.find_element_by_id("給与明細電子化サービス")
login_button2.click()

time.sleep(1)

driver.get("https://www1.e-kakushin.com/e-spec/selectspec.do")

# ダウンロード
download_button = driver.find_elements_by_xpath("//input[@type='button' and @value='閲覧']")
for i in download_button:
  i.click()