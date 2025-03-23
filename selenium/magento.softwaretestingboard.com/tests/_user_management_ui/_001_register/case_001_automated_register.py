import time
import sys
import json
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append('../..')
from _user_management_ui._user_management_resources.user_management_resources import UserManagementResources
from _general_resources.general_resources import GeneralResources




class _001Register:

	def __init__(self, driver, actions):
		self.driver = driver
		self.actions = actions

	def open_register_page(self):
		register_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.header:nth-child(2) > li:nth-child(3) > a:nth-child(1)')))
		register_link.click()

	def step_0(self):
		# disagree on cookies
		try:
			GeneralResources.decline_cookies(self)
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

			self.open_register_page()
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
			if GeneralResources.check_for_visibility(self, locator) == True:
				step_2_passed = True
						


		except TimeoutError as time_err:
			print("Timoeut occured during second step: ", time_err)
			step_2_passed = False
		except Exception as err:
			print("Exception occured during second step: ", err)
			step_2_passed = False
		finally:	 
			print("second step passed:		", step_2_passed)
