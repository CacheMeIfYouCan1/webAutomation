from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import sys

sys.path.append('../..')

from _user_management_ui._002_login_logout.case_002_automated_login_logout import _002LoginLogout

def main():
	try:
		print("################################")
		print("#    TEST 002: LOG IN AND OUT  #")
		print("################################")

		driver = webdriver.Firefox()
		actions = ActionChains(driver)
		#Navigate to demoblaze
		driver.get("https://magento.softwaretestingboard.com")

		#create object
		login_logout = _002LoginLogout(driver, actions)

		#run tests
		login_logout.step_0()
		login_logout.step_1()
		login_logout.step_2()
		login_logout.step_3()
		login_logout.step_4()
		
	except Exception as err:
		print(err)
	finally:
		# Close the browser
		if driver:
			driver.quit()



if __name__ == "__main__":
	main()
