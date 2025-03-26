import time
import sys
import json
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append('../..')
from _resources._user_management_resources.user_management_resources import UserManagementResources
from _resources._general_resources.general_resources import GeneralResources




class _001Register:

	def __init__(self, driver, actions):
		self.driver = driver
		self.actions = actions
		
	def step_0(self):
		# disagree on cookies
		try:
			GeneralResources.accept_cookies(self)
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
			# open link to register form
			UserManagementResources.open_register_page(self)
			step_1_passed = True

		except TimeoutError as time_err:
			print("Timoeut occured during first step: ", time_err)
			step_1_passed = False
		except Exception as err:
			print("Exception occured during first step: ", err)
			step_1_passed = False
		finally:	 
			print("first step passed:		", step_1_passed)

	#register with new test data
	def step_2(self):
		
		try:
			#self.generate_test_data()
			UserManagementResources.generate_test_data(self)
			# fill in fields with new test data

			firstname_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstname')))
			lastname_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'lastname')))
			email_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email_address')))
			password_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
			confirm_password_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password-confirmation')))

			# load user data
			data = UserManagementResources.load_user_data(self)
			
			firstname_element.send_keys(data['firstname'])
			lastname_element.send_keys(data['lastname'])
			email_element.send_keys(data['email'])
			password_element.send_keys(data['password'])
			confirm_password_element.send_keys(data['password'])

			register_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit')))
			register_button.click()

			locator = [((By.CSS_SELECTOR, '.message-success'))]

			find_element = GeneralResources.check_for_visibility(self, locator)
			
			if  find_element["status"] == True:
				step_2_passed = True
			else:
				print("an error occured while finding the element: ", find_element["message"])
				step_2_passed = False

		except TimeoutError as time_err:
			print("Timoeut occured during second step: ", time_err)
			step_2_passed = False
		except Exception as err:
			print("Exception occured during second step: ", err)
			step_2_passed = False
		finally:	 
			print("second step passed:		", step_2_passed)
