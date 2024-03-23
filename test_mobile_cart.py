import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cart():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/index.php/")
    driver.find_element(By.XPATH,"//a[normalize-space()='Mobile']").click()
    driver.find_element(By.XPATH,"(//span[contains(text(),'Add to Cart')])[1]").click()
    driver.find_element(By.XPATH,"//input[@title='Qty']").send_keys("1000")
    driver.find_element(By.XPATH,"//button[@title='Update']//span//span[contains(text(),'Update')]").click()
    error_msg = driver.find_element(By.CSS_SELECTOR,"li[class='error-msg'] ul li span").text
    print(error_msg)
    assert error_msg == "Some of the products cannot be ordered in requested quantity."
    driver.find_element(By.CSS_SELECTOR,"button[id='empty_cart_button'] span span").click()
    title_page = driver.find_element(By.TAG_NAME,"h1").text
    print(title_page)
    assert title_page == "SHOPPING CART IS EMPTY"
    driver.save_screenshot("CartIsEmpty.png")
    driver.quit()