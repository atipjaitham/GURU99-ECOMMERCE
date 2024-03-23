import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_compare():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/index.php/")
    driver.find_element(By.XPATH, "//a[normalize-space()='Mobile']").click()
    mobile_page = driver.current_window_handle
    driver.find_element(By.XPATH, "(//a[@class='link-compare'][normalize-space()='Add to Compare'])[1]").click()
    driver.find_element(By.XPATH, "(//a[@class='link-compare'][normalize-space()='Add to Compare'])[2]").click()

    # Click on Compare button to open the popup window
    driver.find_element(By.XPATH, "(//span[contains(text(),'Compare')])[2]").click()

    print(driver.current_window_handle) #1c696492-4cfc-4c89-8d79-b3a21e11be33 parent
    time.sleep(10)  
    
    # Get all window handles and switch to the popup window
    win_handles = driver.window_handles
    for handle in win_handles:
        if handle != mobile_page:
            driver.switch_to.window(handle)
            break 
    driver.maximize_window()
            
    page_title = driver.title
    print("Page Title:", page_title)
    driver.save_screenshot("CompareProducts.png")
    time.sleep(5) 
    
    # Check if the popup window is still open
    if len(driver.window_handles) > 1:
        # Close the popup window
        driver.find_element(By.XPATH, "//button[@title='Close Window']").click()
    # Close the driver
    driver.quit()
