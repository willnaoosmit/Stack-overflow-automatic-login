from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

user = "YourUserHere"
password = "YourPasswordHere"

try:

	options = Options()
	options.add_argument("--headless")
	browser = webdriver.Firefox(options=options)

	browser.get(r'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
	time.sleep(2)

	browser.find_element_by_id('email').send_keys(user)
	browser.find_element_by_name('password').send_keys(password)
	time.sleep(1)

	browser.find_element_by_name('submit-button').click()
	print('logged in')
	time.sleep(60)

except Exception as error:
	browser.close()

finally:
	browser.close()