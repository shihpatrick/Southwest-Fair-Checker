from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

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
  driver.implicitly_wait(5)
  driver.switch_to_frame(driver.find_element_by_id('destination_publishing_iframe_swa_0'))

  driver.implicitly_wait(5)

  button = driver.find_elements_by_class_name('actionable_button')
  for b in button:
    print(b.text)

if __name__ == "__main__":
  main(sys.argv[1:])