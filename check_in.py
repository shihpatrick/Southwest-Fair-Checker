from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import sys, polling

def main(argv):
  number = argv[0]
  first_name = argv[1]
  last_name = argv[2]

  driver = webdriver.Chrome('./chromedriver')
  driver.get("https://www.southwest.com/")

  check_in_button = driver.find_element(By.ID, 'booking-form--check-in-tab')
  check_in_button.click()

  conf_num = driver.find_element(By.ID, 'confirmationNumber')
  conf_num.send_keys(number)

  first = driver.find_element(By.ID, 'firstName')
  first.send_keys(first_name)

  last = driver.find_element(By.ID, 'lastName')
  last.send_keys(last_name)


  driver.find_element(By.ID, 'jb-button-check-in').click()

  submit_button = polling.poll(
      lambda: driver.find_elements_by_class_name('submit-button'),
      step=0.5,
      timeout=7,
      ignore_exceptions=[NoSuchElementException])

  submit_button[0].click()

  action_buttons = driver.find_elements_by_class_name('actionable_large-button')


  action_buttons[1].click() #email
  email = driver.find_element_by_id('emailBoardingPass')
  email.send_keys('email')

  action_buttons[2].click() #phone
  phonenumber = driver.find_element_by_id('textBoardingPass')
  phonenumber.send_keys('phone')


  submit = driver.find_element_by_id('form-mixin--submit-button')
  submit.click()

if __name__ == "__main__":
  main(sys.argv[1:])