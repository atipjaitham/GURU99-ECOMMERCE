import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_purchase():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/")
    driver.find_element(By.XPATH,"//span[@class='label'][normalize-space()='Account']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Log In']").click()
    driver.find_element(By.XPATH,"//input[@id='email']").send_keys("gregchou_test28@gmail.com")
    driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("12345678")
    driver.find_element(By.XPATH,"//button[@id='send2']").click()
    driver.find_element(By.XPATH,"//span[@class='label'][normalize-space()='Account']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='My Wishlist (1 item)']").click()
    driver.find_element(By.XPATH,"//span[contains(text(),'Add to Cart')]").click()
    driver.find_element(By.XPATH,"//li[@class='method-checkout-cart-methods-onepage-bottom']//button[@title='Proceed to Checkout']").click()
    driver.find_element(By.XPATH,"//input[@id='billing:street1']").send_keys("ABC")
    driver.find_element(By.XPATH,"//input[@id='billing:city']").send_keys("New York")
    driver.find_element(By.XPATH,"//select[@id='billing:region_id']/option[text()='New York']").click()
    driver.find_element(By.XPATH,"//input[@id='billing:postcode']").send_keys("542896")
    driver.find_element(By.XPATH,"//select[@id='billing:country_id']/option[text()='United States']").click()
    driver.find_element(By.XPATH,"//input[@id='billing:telephone']").send_keys("12345678")
    driver.find_element(By.XPATH,"//button[@onclick='billing.save()']//span//span[contains(text(),'Continue')]").click()
    time.sleep(5)
    shipping_cost = driver.find_element(By.XPATH,"//label[@for='s_method_flatrate_flatrate']").text
    print(shipping_cost)
    driver.save_screenshot("ShippingCost.png")
    driver.find_element(By.XPATH,"//button[@onclick='shippingMethod.save()']//span//span[contains(text(),'Continue')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//label[normalize-space()='Check / Money order']").click()
    driver.find_element(By.XPATH,"//button[@onclick='payment.save()']").click()
    time.sleep(5)
    driver.save_screenshot("GrandTotalPrice.png")
    driver.find_element(By.XPATH,"//span[contains(text(),'Place Order')]").click()
    time.sleep(5)
    completed_order = driver.find_element(By.XPATH,"//h1[normalize-space()='Your order has been received.']").text
    print(completed_order)
    order_number = driver.find_element(By.XPATH,"//div[@class='main-container col1-layout']//p[1]").text
    print(order_number)
    driver.save_screenshot("CompleteOrder.png")
    driver.quit()