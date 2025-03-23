import time
import sys
import json
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append('../..')

from _general_resources.general_resources import GeneralResources
from _user_management_ui._user_management_resources.user_management_resources import UserManagementResources
from _user_management_ui._002_login_logout.case_002_automated_login_logout import _002LoginLogout




class _004LoginFalseInputs:

	def __init__(self, driver, actions):
		self.driver = driver
		self.actions = actions


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
			# step 1: click on signup
			_002LoginLogout.open_login_page(self)
 
			step_1_passed = True
				
		except TimeoutError as time_err:
			print("Timoeut occured during first step: ", time_err)
			step_1_passed = False
		except Exception as err:
			print("Exception occured during first step: ", err)
			step_1_passed = False
		finally:	 
			print("first step passed:		", step_1_passed)

	def step_2(self):
		try:
			# send form empty 
			login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'send2')))
			login_button.click()

			# chech visibility of required fields
			locators = [

			((By.ID, 'email-error')),
			((By.ID, 'pass-error'))

			]
			
			if GeneralResources.check_for_visibility(self, locators) == True:
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

	#using wrong password
	def step_3(self):
		try:
			data = UserManagementResources.load_user_data(self)
			email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
			password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'pass')))
			email_field.send_keys(data['email'])
			password_field.send_keys(data['password'])
			login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'send2')))
			login_button.click()

			locator = [((By.CSS_SELECTOR, 'div.messages:nth-child(1)'))]

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
	
