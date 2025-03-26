from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import sys

sys.path.append('../..')

from _user_management_ui.case_004_login_false_inputs import _004LoginFalseInputs



def main():
	try:
		print("#####################################")
		print("#    TEST 004: LOGIN FALSE INPUTS   #")
		print("#####################################")

		driver = webdriver.Firefox()
		actions = ActionChains(driver)
		#Navigate to demoblaze
		driver.get("https://magento.softwaretestingboard.com")

		#create object
		loginFalseInputs = _004LoginFalseInputs(driver, actions)

		#run tests
		loginFalseInputs.step_0()
		loginFalseInputs.step_1()
		loginFalseInputs.step_2()
		loginFalseInputs.step_3()
				
	except Exception as err:
		print(err)
	finally:
		# Close the browser
		if driver:
			driver.quit()



if __name__ == "__main__":
	main()
