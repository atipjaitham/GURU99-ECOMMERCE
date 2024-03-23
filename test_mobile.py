import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_view():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://live.techpanda.org/index.php/")
    title_home = driver.find_element(By.XPATH,"//h2[1]").text
    print(title_home)
    assert title_home == "THIS IS DEMO SITE FOR   "
    driver.find_element(By.XPATH,"//a[normalize-space()='Mobile']").click()
    title_mobile = driver.find_element(By.XPATH,"//h1[normalize-space()='Mobile']").text
    print(title_mobile)
    assert title_mobile == "MOBILE"
    sort = driver.find_element(By.XPATH,"(//select[@title='Sort By'])[1]")
    dropdown = Select(sort)
    dropdown.select_by_visible_text("Name")
    driver.save_screenshot("MobileProducts_sorted.png")
    driver.quit()