import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
# ID
driver.find_element(By.ID,"user-name").send_keys("standard_user")
# Using XPath with index
driver.find_element(By.XPATH,"(//input[@class='input_error form_input'])[2]").send_keys("secret_sauce")
# Using name
driver.find_element(By.NAME,"login-button").click()
# Alert
# alert =driver.switch_to.alert
# print(alert.text)
# alert.accept()
# driver.implicitly_wait(10)
# CssSelector path for drop-down
driver.find_element(By.CSS_SELECTOR,"select[class='product_sort_container']").click()
# Select the option from the drop-down
driver.find_element(By.CSS_SELECTOR,"select[class='product_sort_container'] [value='lohi']").click()
# Click on add-to card
driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie").click()

# Click on the Cart option
driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
time.sleep(5)
# Click on Checking_out button
driver.find_element(By.XPATH,"//div[@class='cart_footer']/button[text()='Checkout']").click()
time.sleep(5)
# User information form
driver.find_element(By.CSS_SELECTOR,"#first-name").send_keys("Tester")
driver.find_element(By.CSS_SELECTOR,"#last-name").send_keys("Tester")
driver.find_element(By.CSS_SELECTOR,"#postal-code").send_keys("522616")
driver.find_element(By.CSS_SELECTOR,"#continue").click()
time.sleep(5)
price=driver.find_element(By.XPATH,"//div[@class='inventory_item_price']").text
print("Print the price of the cart item "+price)
# Complete the order
driver.find_element(By.XPATH,"//div[@class='cart_footer']/button[text()='Finish']").click()
# Print the order placed and thank you message
message=driver.find_element(By.XPATH,"//div[@id='checkout_complete_container']/h2[@class='complete-header']").text
print("Order Placed Successfully Here the message-----"+message)
