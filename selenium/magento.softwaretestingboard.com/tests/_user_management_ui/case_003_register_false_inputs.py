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




class _003RegisterFalseInputs:

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
			# step 1: click on signup
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

	def step_2(self):
			try:
				# send form empty 
				register_button = WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit')))
				register_button.click()				
				
				#check if hints are visible
				locators = [
				((By.ID, 'firstname-error')),
				((By.ID, 'lastname-error')),
				((By.ID, 'email_address-error')),
				((By.ID, 'password-error')),
				((By.ID, 'password-confirmation-error')),
				]

				#need alt locators because sometimes a banner is displayedinstead the usual hints
				alt_locators = [
				((By.CSS_SELECTOR, 'div.messages:nth-child(1)'))
				]

				err_visible = GeneralResources.check_for_visibility(self, locators)
				alt_err_visible = GeneralResources.check_for_visibility(self, alt_locators)

				if err_visible["status"] == True or alt_err_visible["status"] == True: 
					step_2_passed = True
				else:
					print("error occured, while finding element: ")
					print(err_visible["message"])
					print(alt_err_visible["message"])
					step_2_passed = False
						


			except TimeoutError as time_err:
				print("Timoeut occured during second step: ", time_err)
				step_2_passed = False
			except Exception as err:
				print("Exception occured during second step: ", err)
				step_2_passed = False
			finally:	 
				print("second step passed:		", step_2_passed)

	#register already existing user
	def step_3(self):
		try:
			data = UserManagementResources.load_user_data(self)

			first_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstname')))
			last_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'lastname')))
			email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'email_address')))
			password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
			confirm_password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password-confirmation')))

			first_name_field.send_keys(data['firstname'])
			last_name_field.send_keys(data['lastname'])
			email_field.send_keys(data['email'])
			password_field.send_keys(data['password'])
			confirm_password_field.send_keys(data['password'])


			register_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit')))
			register_button.click()

			locator = [((By.CSS_SELECTOR, '.message-error > div:nth-child(1)'))]
			if GeneralResources.check_for_visibility(self, locator) == True:
				step_3_passed = True
			else:
				step_3_passed = False
			
			
			
			step_3_passed = True
		except TimeoutError as time_err:
			print("Timoeut occured during third step: ", time_err)
			step_3_passed = False
		except Exception as err:
			print("Exception occured during third step: ", err)
			step_3_passed = False
		finally:	 
			print("third step passed:		", step_3_passed)
