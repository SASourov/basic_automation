from selenium.webdriver.common.by import By
from selenium import webdriver


class Practice:
    def __init__(self, driver):
        self.driver = driver
        self.set_username = (By.ID, "username")
        self.set_user_password = (By.ID, "password")
        self.click_login_button = (By.ID, "submit")

    def set_username(self, username):
        self.driver.find_element(*self.set_username).clear()
        self.driver.find_element(*self.set_username).send_keys(username)

    def set_user_password(self, password):
        self.driver.find_element(*self.set_user_password).clear()
        self.driver.find_element(*self.set_user_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.click_login_button).click()


class NavigateMenu:
    def __init__(self, driver):
        self.driver = driver
        self.click_home = (By.XPATH, "//li[@id='menu-item-43']//a[1]")
        self.click_practice = (By.XPATH, "//li[@id='menu-item-20']//a[1]")
        self.click_course = (By.XPATH, "(//li[contains(@class,'menu-item menu-item-type-post_type')]//a)[3]")
        self.click_blog = (By.XPATH, "//li[@id='menu-item-19']//a[1]")
        self.click_contact = (By.XPATH, "//li[@id='menu-item-18']//a[1]")

    def click_home_link(self):
        self.driver.find_element(*self.click_home).click()

    def click_practice_link(self):
        self.driver.find_element(*self.click_practice).click()

    def click_course_link(self):
        self.driver.find_element(*self.click_course).click()

    def click_blog_link(self):
        self.driver.find_element(*self.click_blog).click()

    def click_contact_link(self):
        self.driver.find_element(*self.click_contact).click()