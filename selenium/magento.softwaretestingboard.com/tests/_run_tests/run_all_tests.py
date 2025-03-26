from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

sys.path.append ('..')


from _user_management_ui.case_001_automated_register import _001Register 
from _user_management_ui.case_002_automated_login_logout import _002LoginLogout
from _user_management_ui.case_003_register_false_inputs import _003RegisterFalseInputs
from _user_management_ui.case_004_login_false_inputs import _004LoginFalseInputs

def clear_browser_data(driver):
	
	driver.delete_all_cookies()
	driver.refresh()
	
def main():

	print("##########################")
	print("#    RUNNUNG ALL TESTS   #")
	print("##########################")
	print("")
	print("")
	print("#########################")
	print("#    USER MANAGEMENT    #")
	print("#########################")
	
	driver = webdriver.Firefox()
	actions = ActionChains(driver)
	#Navigate to page
	
	#create objects
	register = _001Register(driver, actions)
	login_logout = _002LoginLogout(driver, actions)
	false_register = _003RegisterFalseInputs(driver, actions)
	false_login = _004LoginFalseInputs(driver, actions)

	driver.get("https://magento.softwaretestingboard.com")
	
	try:
		print("###########################")
		print("#    TEST 001: SIGN UP    #")
		print("###########################")
		
		register.step_0()
		register.step_1()
		register.step_2()

		print("#################################")
		print("#    TEST 002: LOG IN AND OUT   #")
		print("#################################")

		clear_browser_data(driver)
			
		login_logout.step_0()
		login_logout.step_1()
		login_logout.step_2()
		login_logout.step_3()
		login_logout.step_4()

		print("#################################################")
		print("#    TEST 003: FALSE INPUTS WHILE REGISTERING   #")
		print("#################################################")

		clear_browser_data(driver)

		false_register.step_0()
		false_register.step_1()
		false_register.step_2()
		false_register.step_3()

		print("################################################")
		print("#    TEST 004: FALSE INPUTS WHILE LOGGING IN   #")
		print("################################################")

		clear_browser_data(driver)

		false_login.step_0()
		false_login.step_1()
		false_login.step_2()
		false_login.step_3()

		

	except Exception as err:
		print(err)
	finally:
		# Close the browser
		if driver:
			driver.quit()


if __name__ == "__main__":
	main()
