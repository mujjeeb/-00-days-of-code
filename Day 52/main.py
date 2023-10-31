from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(INSTAGRAM_USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(20)
        save_info = self.driver.find_element(By.CLASS_NAME, '_acan')
        save_info.click()
        time.sleep(40)
        turn_on_notifications = self.driver.find_element(By.CLASS_NAME, '_a9_0')
        turn_on_notifications.click()
        # try:
        #     save_info = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_+/"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button')
        #     save_info.click()
        #     print("done")
        # except:
        #     pass

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/')
        # self.driver.get('https://www.instagram.com/chefsteps/followers/')
        self.driver.implicitly_wait(10)
        followers_a = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'followers').click()
        self.driver.implicitly_wait(10)

        time.sleep(2)
        modal = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in all_buttons:
            print("it works to this point")
            if button.text != 'Follow':
                print('boomerang')
                pass
            else:
                button.click()
                print("boom")
                time.sleep(5)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()