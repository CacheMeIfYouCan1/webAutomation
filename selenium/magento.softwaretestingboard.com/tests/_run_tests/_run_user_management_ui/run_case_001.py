from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import sys

sys.path.append('../..')

from _user_management_ui._001_register.case_001_automated_register import _001Register 

def main():
	try:
		print("############################")
		print("#    TEST 001: REGISTER    #")
		print("############################")

		driver = webdriver.Firefox()
		actions = ActionChains(driver)
		#Navigate to test site
		driver.get("https://magento.softwaretestingboard.com")

		#create object
		register = _001Register(driver, actions)

		#run tests
		register.step_0()
		register.step_1()
		register.step_2()
		
	except Exception as err:
		print(err)
	finally:
		# Close the browser
		if driver:
			driver.quit()

if __name__ == "__main__":
	main()
