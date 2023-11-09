from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os

user = "YourUserHere"
password = "YourPasswordHere"

try:
	options = Options()
	options.add_argument("--headless")
	service = Service(log_path=os.devnull)
	browser = webdriver.Firefox(options=options, service=service)

	browser.get(r'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
	sleep(2)

	browser.find_element(By.ID, 'email').send_keys(user)
	browser.find_element(By.NAME, 'password').send_keys(password)
	sleep(1)

	browser.find_element(By.NAME, 'submit-button').click()
	print('logged in')
	sleep(60)

except Exception as error:
	print(error)
	browser.close()

finally:
	try:
		browser.close()
	except:
		pass
