from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Path to the ChromeDriver executable
chromedriver_path = "/Users/rohan/Desktop/Code/DataScience/Del-Lab/Selenium-Automate/chromedriver-arm/chromedriver"

# Set Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless") 

print("Verbose Mode")

number_name_list = ["Eighty four"]
for NUMBER_NAME in number_name_list:

    
    print('--'*25)
    print(f'''- Generating: "{NUMBER_NAME}", ''',end='')

    # Create a new instance of the Chrome driver
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # for headless mode 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Navigate to a webpage
    driver.get("https://www.naturalreaders.com/login-service/login?redir=pw&dest=online")


    user_email = driver.find_element(By.XPATH, '''//*[@id="mat-input-0"]''')
    user_email.send_keys("dellab@colorado.edu")

    time.sleep(2)
    # next button 
    driver.find_element(By.XPATH, '''/html/body/app-root/app-sign-in/div/div/div/div[3]/div/div[3]/div[1]/button''').click()

    time.sleep(2)
    password = driver.find_element(By.XPATH, '''//*[@id="mat-input-1"]''')
    password.send_keys("Kidsfun0077+")

    # Next again 
    time.sleep(2)
    driver.find_element(By.XPATH, '''/html/body/app-root/app-auth-password/div/div/div/div[3]/div/div[3]/div/button''').click()


    time.sleep(2)
    # Find the input field by its CSS selector and enter text into it
    #driver.find_element(By.XPATH,'''/html/body/app-root/app-voice-selection/div/div/div[3]/button''').click()


    time.sleep(3)
    # Find the <div> element by its CSS selector
    div_element = driver.find_element(By.XPATH, '''//*[@id="inputDiv"]''')

    # Clear the existing text inside the <div>
    div_element.clear()


    # Enter your custom text
    div_element.send_keys(f"{NUMBER_NAME}")


    # Click Play 
    #driver.find_element(By.XPATH, f'''//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]''').click()


    # Download Sequence.
    # Click on the 3 Dots
    driver.find_element(By.XPATH, '''//*[@id="pwReadingMenuTrigger"]''').click()

    time.sleep(1)

    # Convert to MP3 
    driver.find_element(By.XPATH, '''//*[@id="mat-menu-panel-6"]/div/div/mat-list/mat-list-item[1]/span/button''').click()
    time.sleep(2)

    # Convert Now, 
    driver.find_element(By.XPATH, '''//*[@id="mat-dialog-0"]/app-convert-dialog/mat-dialog-actions/button[2]''').click()

    time.sleep(1)
    # Download
    driver.find_element(By.XPATH, '''//*[@id="mat-dialog-0"]/app-convert-dialog/mat-dialog-actions/a''').click()

    

    time.sleep(7)
    #driver.quit()

    print('Done!')


print('--'*25)
print('Sequence Completed')
print("Audio Files will be in ~/Downloads.")


    
    




