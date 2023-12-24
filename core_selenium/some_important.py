import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import string

random = random.randint(0, 999)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
drop_down_url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"


def drop_down():
    driver.get(drop_down_url)
    select_country = Select(
        driver.find_element(By.XPATH, "//div[contains(@class,'single_tab_div resp-tab-content')]//select[1]"))
    select_country.select_by_value("BHR")
    time.sleep(5)


def take_screen_shot():
    driver.get(drop_down_url)
    ss = driver.save_screenshot(r"D:\basic_automation\Screen_Shot\test" + str(random) + ".png") #file_path/file_name.file_extention


def window_handle():
    click_cheatsheet = driver.find_element(By.XPATH, "//li[@id='menu-item-6898']/a[1]")
    click_cheatsheet.click()

    vim_cheatsheet = driver.find_element(By.XPATH, "//span[@class='has-inline-color has-vivid-cyan-blue-color']//a")
    vim_cheatsheet.click()


def upload_photo():
    driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
    upload_image = driver.find_element(By.ID, "photo")
    upload_image.send_keys(r"D:/File/pro_pic_demo.png") #file_path/file_name.file_extention
    time.sleep(10)


drop_down()
take_screen_shot()
upload_photo()