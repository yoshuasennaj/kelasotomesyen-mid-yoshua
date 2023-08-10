from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = CHROME_BINARY_PATH

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/webtables")


user_data = [
    ["Ahmad", "Dani", "adp@mail.com", "47", "10000000", "QA"],
    ["Ari", "Lasso", "lasso@mail.com", "50", "15000000", "Dev"],
    ["Arya", "Permana", "arya@mail.com", "19", "70000000", "Marketing"]
    ]
try:
    for data in user_data:
        record_button = wait.until(EC.element_to_be_clickable((By.ID, 'addNewRecordButton')))
        record_button.click()
        driver.find_element(By.ID, 'firstName').send_keys(data[0])
        driver.find_element(By.ID, 'lastName').send_keys(data[1])
        driver.find_element(By.ID, 'userEmail').send_keys(data[2])
        driver.find_element(By.ID, 'age').send_keys(data[3])
        driver.find_element(By.ID, 'salary').send_keys(data[4])
        driver.find_element(By.ID, 'department').send_keys(data[5])
        driver.find_element(By.ID, 'submit').click()
    print("Success")
    driver.save_screenshot("success.png")
        
except:
    print("Fail")
    driver.save_screenshot("fail.png")

driver.quit()
