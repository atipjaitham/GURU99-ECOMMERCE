import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_create_account():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/")
    driver.find_element(By.XPATH,"//span[@class='label'][normalize-space()='Account']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
    create_headder = driver.find_element(By.XPATH,"//h1[normalize-space()='Create an Account']").text
    print (create_headder)
    driver.find_element(By.XPATH,"//input[@id='firstname']").send_keys("Greg")
    driver.find_element(By.XPATH,"//input[@id='lastname']").send_keys("Chouuu")
    driver.find_element(By.XPATH,"//input[@id='email_address']").send_keys("gregchosu@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("12345678")
    driver.find_element(By.XPATH,"//input[@id='confirmation']").send_keys("12345678")
    driver.find_element(By.XPATH,"//button[@title='Register']").click()
    complete_register = driver.find_element(By.XPATH,"//span[normalize-space()='Thank you for registering with Main Website Store.']").text
    print(complete_register)
    driver.save_screenshot("RegisterDone.png")
    driver.find_element(By.XPATH,"//a[normalize-space()='TV']").click()
    title_TV = driver.find_element(By.XPATH,"//h1[normalize-space()='TV']").text
    print(title_TV)
    driver.find_element(By.XPATH,"(//a[contains(text(),'Add to Wishlist')])[1]").click()
    driver.find_element(By.XPATH,"//span[contains(text(),'Share Wishlist')]").click()
    driver.find_element(By.XPATH,"//textarea[@id='email_address']").send_keys("atip.testmail@gmail.com")
    driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("Hey! view my wishlist!")
    driver.find_element(By.XPATH,"//button[@title='Share Wishlist']").click()
    complete_sharedwish = driver.find_element(By.XPATH,"//span[normalize-space()='Your Wishlist has been shared.']").text
    print(complete_sharedwish)
    driver.save_screenshot("SharedDone.png")
    driver.quit()