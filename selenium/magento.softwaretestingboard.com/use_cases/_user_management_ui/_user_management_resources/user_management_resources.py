import time
import sys
import json
import os
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

class UserManagementResources:

	def __init__(self, driver):
		self.driver = driver

	def generate_test_data(self):
		self.current_dir = os.path.dirname(os.path.abspath(__file__))
		self.file_path = os.path.join(self.current_dir, 'user.json')

		#create pseudo-random usedata
		firstname = 'FirstName' +  str(random.randint(100000, 200000))
		lastname = 'LastName' + str(random.randint(100000,200000))
		email = str(random.randint(100000,200000)) + '@ma.il'
		password = 'Password.' + str(random.randint(100000, 200000))

		#write username + password to file for usage in second test
		user = {
		 "firstname" : firstname,
		 "lastname" : lastname,
		 "email" : email,
		 "password" : password
		}

		with open(self.file_path, 'w') as file:
			json.dump(user, file, indent=4)

	def load_user_data(self):
		self.current_dir = os.path.dirname(os.path.abspath(__file__))
		self.file_path = os.path.join(self.current_dir, 'user.json')

		with open(self.file_path, 'r') as file:
			data = json.load(file)

			return data
			
	
