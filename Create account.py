from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Firefox()
driver.implicitly_wait(50)
driver.maximize_window()

# Step 1: Open Skillcamper website
driver.get("https://app.skillcamper.com/")
# driver.get("https://app.skillcamper.com/?_gl=1*151pd4a*_gcl_au*Nzg5MjAzNjQ3LjE3NTMxOTQ2MTk.")


# Step 2: Click on "Get Started for Free" button
# driver.find_element(By.XPATH, "//div[@class='uui-navbar_button-wrapper']/a[2]/div[1]").click()

# Step 3: Click on "Sign Up"
driver.find_element(By.XPATH, "//div[@class='flex gap-4']/button[@class='py-3 px-4 bg-[#000000] text-[#FFFFFF]']").click()


# Step 4: Fill the sign-up form
driver.find_element(By.CSS_SELECTOR, "#form-username").send_keys("Amalaa")

driver.find_element(By.CSS_SELECTOR, "#form-temp-name").send_keys("Yarramm")
email= driver.find_element(By.CSS_SELECTOR, "#wf-sign-up-email")
email.send_keys("amalayarram18@gmail.com")


driver.find_element(By.CSS_SELECTOR, "#wf-sign-up-password").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "#wf-sign-up-confirm-password").send_keys("123456789")

# Click on "Next" button
driver.find_element(By.XPATH, "//div[@id='next-button']/span").click()

# it's print the error message of the email id field
print(driver.find_element(By.XPATH,"//div[@id='email-error']").text)

# Step 5: Wait for 10 seconds
# time.sleep(10)

# Step 6: Enter phone number and click "Get OTP"
driver.find_element(By.CSS_SELECTOR, "#wf-sign-up-mobile").send_keys("9916686301")

driver.find_element(By.CSS_SELECTOR, ".getOtpBtn").click()

# Step 7: Wait for 10 seconds
time.sleep(40)

# Step 8: Click on "Verify & Continue"
driver.find_element(By.XPATH, "//div[@id='verifyBtn']/span").click()

# Step 9:
Check = driver.find_element(By.XPATH,"//div[@class='flex gap-2 ']/input[@id='wf-sign-up-accept-privacy']")
Check.click()

assert Check.is_selected()
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='flex gap-2 ']/input[@name='user.attributes.email_marketing']").click()
time.sleep(15)

# Done
driver.find_element(By.XPATH,"//button[@id='submit-btn']/span[text()='Submit']").click()
print("Signup automation completed.")
# Close the browser (optional)
# driver.quit()
