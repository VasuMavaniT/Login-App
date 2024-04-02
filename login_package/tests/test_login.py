import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Replace 'chromedriver' with the path to your WebDriver executable
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000/login')

    def test_login_with_valid_credentials(self):
        # Fill in the login form with valid credentials
        username_input = self.driver.find_element(By.ID, 'username')
        password_input = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')

        username_input.send_keys('vasu')
        password_input.send_keys('V@su')
        submit_button.click()

        # Wait until the success message is displayed
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'alert-success'))
        )

        # Check if the success message is displayed
        success_message = self.driver.find_element(By.CLASS_NAME, 'alert-success')
        self.assertTrue('Login successful!' in success_message.text)

    def test_login_with_username_only(self):
        # Fill in the login form with only the username
        username_input = self.driver.find_element(By.ID, 'username')
        submit_button = self.driver.find_element(By.ID, 'submit')

        username_input.send_keys('vasu')
        submit_button.click()

        # Wait until the error message is displayed
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'passwordError'))
        )

        # Check if the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME, 'passwordError')
        self.assertTrue('Password is required.' in error_message.text)

    def test_login_with_password_only(self):
        # Fill in the login form with only the password
        password_input = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.ID, 'submit')

        password_input.send_keys('V@su')
        submit_button.click()

        # Wait until the error message is displayed
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'usernameError'))
        )

        # Check if the error message is displayed
        error_message = self.driver.find_element(By.CLASS_NAME, 'usernameError')
        self.assertTrue('Username is required.' in error_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
