from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains

# Open browser and navigate to URL
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://demoqa.com/buttons')

# Creating actions object
actions = ActionChains(driver)

### TASK 1: Perform double_clickc ###

# Find target element
double_click_button = driver.find_element(By.CSS_SELECTOR, '#doubleClickBtn')
print('Name of this button is: ' + double_click_button.text)

# Perform mouse action
actions.double_click(double_click_button).perform()
driver.save_screenshot('double_click.png')

# Read result message and check 
result_message = driver.find_element(By.CSS_SELECTOR, '#doubleClickMessage').text
print(result_message)
print('You have done a double click' in result_message)
sleep(3)


### TASK 2: Perform right mouse button clicking ###

# Find target element
right_button = driver.find_element(By.CSS_SELECTOR, '#rightClickBtn')
print('Name of this button is: ' + right_button.text)

# Perform mouse action
actions.context_click(right_button).perform()
driver.save_screenshot('right_click.png')

# Read result message and check 
result_message2 = driver.find_element(By.CSS_SELECTOR, '#rightClickMessage').text
print(result_message2)
print('You have done a right click' in result_message2)
sleep(3)


## TASK 3: Perform dynamic mouse button click ###

# Find all button elements on the webpage
dynamic_click = driver.find_elements(By.CSS_SELECTOR, 'button')

# Click the "Click me" button using its index
button_index = 3  
print('Name of this button is: ' + dynamic_click[button_index].text)
actions.click(dynamic_click[button_index]).perform()
driver.save_screenshot('click.png')

# Read result message and check 
result_message3 = driver.find_element(By.CSS_SELECTOR, '#dynamicClickMessage').text
print(result_message3)
print('You have done a dynamic click' in result_message3)
sleep(3)

driver.close()

