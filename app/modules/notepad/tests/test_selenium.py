from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver

class TestCrearnotepad():
  def setup_method(self, method):
    self.driver = initialize_driver()
    self.vars = {}
  
  def teardown_method(self, method):
    close_driver(self.driver)
  
  def test_crearnotepad(self):
    try:
        host = get_host_for_selenium_testing()
        self.driver.get(f'{host}')
        self.driver.set_window_size(962, 923)
        self.driver.find_element(By.CSS_SELECTOR, ".content").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
        self.driver.find_element(By.ID, "password").send_keys("1234")
        self.driver.find_element(By.ID, "submit").click()
        self.driver.get(f'{host}/notepad')
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys("Test")
        self.driver.find_element(By.ID, "body").click()
        self.driver.find_element(By.ID, "body").send_keys("Testing")
        self.driver.find_element(By.ID, "submit").click()
    except:
        raise AssertionError('Test failed!')
    finally:
        close_driver(self.driver)
    

def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f'{host}')
        driver.set_window_size(962, 923)
        driver.find_element(By.CSS_SELECTOR, ".content").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "email").send_keys("user1@example.com")
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "submit").click()
        
        driver.get(f'{host}/notepad')
        time.sleep(4)
    except:
        raise AssertionError('Test failed!')

    finally:
        close_driver(driver)