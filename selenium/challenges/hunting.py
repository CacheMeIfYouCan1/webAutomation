from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time

def is_in_array(number, array):
	return number in array

def main():

	print("#####################")
	print("#    CHALLENGE 01   #")
	print("#####################")
	print("challenge can be found here: ")
	print("https://showdownspace-rpa-challenge.vercel.app/challenge-hunting-fed83d58/")

	driver = webdriver.Firefox()
	actions = ActionChains(driver)
	
	driver.get("https://showdownspace-rpa-challenge.vercel.app/challenge-hunting-fed83d58/")

	start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button")))
	start_button.click()

	number_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/span[1]")))
	number_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/span[2]"))) 
	number_3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/span[3]")))
	number_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/span[4]")))
	number_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/span[5]")))

	number_content = [0,1,2,3,4]

	number_content[0] = number_1.text
	number_content[1] = number_2.text
	number_content[2] = number_3.text
	number_content[3] = number_4.text
	number_content[4] = number_5.text


	for i in range(1, 64):
		box = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div/div[2]/div[{i}]')
		actions.move_to_element(box).perform()

		tooltip = driver.find_element(By.XPATH, '/html/body/div[3]')
		number_to_check = tooltip.text

		if is_in_array(number_to_check, number_content):
			box.click()

	time.sleep(5)

	driver.quit()


if __name__ == "__main__":
	main()
