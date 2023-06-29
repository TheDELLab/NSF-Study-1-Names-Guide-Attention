from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time 
import os 
from glob import glob


# Set Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless") 


print("Verbose Mode")

"""
THE CODE TO PICK SENTENCES FROM THE CONDITION FILES GOES HERE 
use pandas 
- read conditions
- sentences = df['number-names']
"""

conditions = pd.read_csv("Sample_Conditions.csv")
#print(conditions)
condition_1 = conditions[conditions['Conditions']==1]['Audio'].to_list()
condition_2 = conditions[conditions['Conditions']==2]['Audio'].to_list()


folder_path = os.path.expanduser('~/Downloads/condition_2')
os.makedirs(folder_path, exist_ok=True)


# INSTANTIATE AND LOGIN
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
# Navigate to a webpage
driver.get("https://www.naturalreaders.com/login-service/login?redir=pw&dest=online")


# Wait for the email input field to be visible
wait = WebDriverWait(driver, 10)
user_email = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-input-0"]')))
user_email.send_keys("dellab@colorado.edu")

# Next button
driver.find_element(By.XPATH, '/html/body/app-root/app-sign-in/div/div/div/div[3]/div/div[3]/div[1]/button').click()

# Wait for the password input field to be visible
password = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-input-1"]')))
password.send_keys("Kidsfun0077+")

# Next again 
time.sleep(2)
driver.find_element(By.XPATH, '''/html/body/app-root/app-auth-password/div/div/div/div[3]/div/div[3]/div/button''').click()


# AUDIO PROFILE SELECTION 

# click audio profiles
wait.until(EC.element_to_be_clickable((By.XPATH, '''/html/body/app-root/app-main/app-pw-page/div/div[2]/app-pw-single-page/div[1]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[1]'''))).click()


time.sleep(3)
# AUDIO PROFILE RADIO BUTTON ( ANA CHILD )
driver.find_element(By.XPATH, '''/html/body/div[2]/div[2]/div/mat-dialog-container/app-pw-voices/mat-dialog-content/mat-selection-list/mat-list-option[4]/div/div[2]/div/div[2]/div''').click()

# Cross
time.sleep(3)
driver.find_element(By.XPATH, '''/html/body/div[2]/div[2]/div/mat-dialog-container/app-pw-voices/div/div/div[2]/button[3]''').click()


# time.sleep(3)
# driver.find_element(By.XPATH, '''/html/body/app-root/app-main/app-pw-page/div/div[2]/app-pw-single-page/div[1]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]''').click()


# Click Play 
#driver.find_element(By.XPATH, f'''//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]''').click()



# CHANGE THIS to condition_2 to download condition_2 audio and vice versa
for key,condition in zip(["Condition 1", "Condition 2"],[condition_1, condition_2]):
    print('--'*25)
    print(f'{key}')
    for NUMBER_NAME in condition:
        
        print(f'''- Generating: "{NUMBER_NAME}", ''',end='')


        time.sleep(3)
        # Find the <div> element by its CSS selector
        div_element = driver.find_element(By.XPATH, '''//*[@id="inputDiv"]''')

        # Clear the existing text inside the <div>
        div_element.clear()


        # Enter your custom text
        div_element.send_keys(f"{NUMBER_NAME}")


        # Download Sequence.
        # Click on the 3 Dots
        driver.find_element(By.XPATH, '''//*[@id="pwReadingMenuTrigger"]''').click()

        time.sleep(1)
        # Convert to MP3 
        driver.find_element(By.XPATH, '''//*[@id="mat-menu-panel-6"]/div/div/mat-list/mat-list-item[1]/span/button''').click()
        

        # Convert Now,
        time.sleep(4) 
        driver.find_element(By.XPATH, '''/html/body/div[2]/div[2]/div/mat-dialog-container/app-convert-dialog/mat-dialog-actions/button[2]''').click()

        time.sleep(4)
        # Download
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/app-convert-dialog/mat-dialog-actions/a'))).click()


        # CLOSE DOWNLOAD SECTION 
        wait.until(EC.element_to_be_clickable((By.XPATH, '''/html/body/div[2]/div[2]/div/mat-dialog-container/app-convert-dialog/div/div/button'''))).click()

        time.sleep(3)
        #driver.quit()


        print('Done!')

        

print('--'*25)
print('Sequence Completed')
print("Audio Files will be in ~/Downloads.")


    
    




