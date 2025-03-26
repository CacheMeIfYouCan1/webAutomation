import time
import sys
import json
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

class GeneralResources:

	def __init__(self, driver):
		self.driver = driver
		
	# Check if elements are visible
	def check_for_visibility(self, locators):
		try: 
			for locator in locators:
				error_text_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
			return {"status": True, "message": "Successfully found elements"}
		except Exception as err:
			return {"status": False, "message": err}
	
	
	def accept_cookies(self):
		cookie_dialogue_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'accept-btn')))
		cookie_dialogue_button.click()
