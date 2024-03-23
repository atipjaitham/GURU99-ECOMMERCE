import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cost():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/index.php/")
    driver.find_element(By.XPATH,"//a[normalize-space()='Mobile']").click()
    price_out = driver.find_element(By.XPATH,"//span[contains(text(),'$100.00')]").text
    print(price_out)
    driver.find_element(By.XPATH,"//a[@title='Sony Xperia']").click
    price_in = driver.find_element(By.XPATH,"//span[@class='price']").text
    print(price_in)
    assert price_out == price_in
    driver.quit()
    
