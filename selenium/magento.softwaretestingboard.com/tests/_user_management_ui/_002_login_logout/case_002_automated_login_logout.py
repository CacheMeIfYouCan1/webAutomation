import time
import sys
import json
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append('../..')

from  _user_management_ui._user_management_resources.user_management_resources import UserManagementResources
from _general_resources.general_resources import GeneralResources




class _002LoginLogout:

	def __init__(self, driver, actions):
		self.driver = driver
		self.actions = actions

	def open_login_page(self):
		sign_in_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.header:nth-child(2) > li:nth-child(2) > a:nth-child(1)')))
		sign_in_link.click()

		

	def step_0(self):
		# disagree on cookies
		try:
			GeneralResources.decline_cookies(self)
			step_0_passed = True
			
			step_0_passed = True
		except TimeoutError as time_err:
			print("Timoeut occured during first step: ", time_err)
			step_0_passed = False
		except Exception as err:
			print("Exception occured during first step: ", err)
			step_0_passed = False
		finally:	 
			print("step zero passed:		", step_0_passed)
	
	def step_1(self):
		try:
			self.open_login_page()
			step_1_passed = True

		except TimeoutError as time_err:
			print("Timoeut occured during first step: ", time_err)
			step_1_passed = False
		except Exception as err:
			print("Exception occured during first step: ", err)
			step_1_passed = False
		finally:	 
			print("first step passed:		", step_1_passed)

	
	#fill in user data
	def step_2(self):
		
		try:
			# load user data
			data = UserManagementResources.load_user_data(self)

			email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
			password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'pass')))
			sign_in_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'send2')))

			email_field.send_keys(data['email'])
			password_field.send_keys(data['password'])

			sign_in_button.click()
			
			locator = [((By.CSS_SELECTOR, 'ul.header:nth-child(2) > li:nth-child(1)'))]
			if GeneralResources.check_for_visibility(self, locator) == True:
				step_2_passed = True

			else:
				step_2_passed = False


		except TimeoutError as time_err:
			print("Timoeut occured during second step: ", time_err)
			step_2_passed = False
		except Exception as err:
			print("Exception occured during second step: ", err)
			step_2_passed = False
		finally:	 
			print("second step passed:		", step_2_passed)
	
	def step_3(self):
		try:
			user_dropdown_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.header:nth-child(2) > li:nth-child(2) > span:nth-child(1) > button:nth-child(1)')))
			user_dropdown_element.click()

			locator = [((By.CSS_SELECTOR, 'li.active > div:nth-child(2) > ul:nth-child(1)'))]
			if GeneralResources.check_for_visibility(self, locator) == True:
				step_3_passed = True
			else:
				step_3_passed = False
		except TimeoutError as time_err:
			print("Timoeut occured during third step: ", time_err)
			step_3_passed = False
		except Exception as err:
			print("Exception occured during third step: ", err)
			step_3_passed = False
		finally:	 
			print("third step passed:		", step_3_passed)


	def step_4(self):
		try:
			logout_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.active > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')))
			logout_element.click()

			locator = [((By.CSS_SELECTOR, 'ul.header:nth-child(2) > li:nth-child(2) > a:nth-child(1)'))]
			if GeneralResources.check_for_visibility(self, locator) == True:
				step_4_passed = True
			else:
				step_4_passed = False
		except TimeoutError as time_err:
			print("Timoeut occured during fourth step: ", time_err)
			step_4_passed = False
		except Exception as err:
			print("Exception occured during fourth step: ", err)
			step_4_passed = False
		finally:	 
			print("fourth step passed:		", step_4_passed)



