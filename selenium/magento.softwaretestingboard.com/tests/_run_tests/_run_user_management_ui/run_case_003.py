from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import sys

sys.path.append('../..')

from _user_management_ui.case_003_register_false_inputs import _003RegisterFalseInputs



def main():
	try:
		print("########################################")
		print("#    TEST 003: REGISTER FALSE INPUTS   #")
		print("########################################")

		driver = webdriver.Firefox()
		actions = ActionChains(driver)
		#Navigate to demoblaze
		driver.get("https://magento.softwaretestingboard.com")

		#create object
		registerFalseInputs = _003RegisterFalseInputs(driver, actions)

		#run tests
		registerFalseInputs.step_0()
		registerFalseInputs.step_1()
		registerFalseInputs.step_2()
		registerFalseInputs.step_3()
		
	except Exception as err:
		print(err)
	finally:
		# Close the browser
		if driver:
			driver.quit()



if __name__ == "__main__":
	main()
