from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys

def main(argv):

  # cmp_price = (int(input("Enter Price: ")))
  # depart = input("Enter Depart Location, e.g. (SJC): ")
  # arrive = input("Enter Arrive Location, e.g. (LAX): ")
  # date = input("Enter Depart Date: ")

  cmp_price = (int(argv[0]))
  depart = argv[1]
  arrive = argv[2]
  date = argv[3]

  # driver = webdriver.Chrome('/Users/patrickkshih/Desktop/projects/automateproj/chromedriver')
  driver = webdriver.Chrome('/Users/jimmysmacbook/Desktop/automateproj/chromedriver')
  driver.get("https://www.southwest.com/")

  driver.find_element(By.ID, 'trip-type-one-way').click()

  depart_field = driver.find_element(By.ID, 'air-city-departure')
  depart_field.send_keys(depart)

  arrive_field = driver.find_element(By.ID, 'air-city-arrival')
  arrive_field.send_keys(arrive)

  date_field = driver.find_element(By.ID, 'air-date-departure')
  date_field.clear()
  date_field.send_keys(date)

  driver.find_element(By.ID, 'jb-booking-form-submit-button').click()

  prices = driver.find_elements_by_class_name('product_price')
  index = 0

  convert_prices = []

  for price in prices:
    if index % 3 == 2:
      convert_prices.append(price.text[1:])
    index = index + 1

  time_list = driver.find_elements_by_class_name('time')
  indicator_list = driver.find_elements_by_class_name('indicator')
  index = 0

  convert_time = []

  for time in time_list:
    if index % 2 == 0:
      convert_time.append(time.text + " " + indicator_list[index*2].text)

    index = index + 1

  price_time = {}

  index = 0
  for price in convert_prices:
    if price not in price_time:
      price_time[price] = [convert_time[index]]
    else:
      price_time[price].append(convert_time[index])
    index = index + 1

  for price in price_time.keys():
    if cmp_price > (int(price)):
      print(price)
      for time in price_time[price]:
        print(time)


if __name__ == "__main__":
  main(sys.argv[1:])
