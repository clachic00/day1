import time

from selenium.webdriver import Chrome

chromeDriver = 'C:\\temp\\chromedriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://login.11st.co.kr/auth/front/login.tmall')

time.sleep(3)

input_login = driver.find_element_by_id("loginName")

input_login.send_keys("kych74")

input_login2 = driver.find_element_by_id("passWord")

input_login2.send_keys("1qaz2wsx@#")

input_login3 = driver.find_element_by_class_name("btn_Atype")

time.sleep(3)

input_login3.click()

time.sleep(3)

driver.get()

#driver.quit()