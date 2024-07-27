import botAssistantModule as bot
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from botAssistantModule import Devices, Browsers


username = "223CS1107"
password = "Skasikilahi100@"

def main():
    model = bot.botAssistant()
    model.sleepRandom_minTime = 0
    model.sleepRandom_maxTime = 1
    model.openBrowser(headless=True, browser=Browsers.CHROME)
    model.goToLink("https://login.nitrkl.ac.in/PortalMain")

    try:
        model.browser.find_element(By.ID, "LoginUserPassword_auth_username").send_keys(username)
        model.browser.find_element(By.ID, "LoginUserPassword_auth_password").send_keys(password)
        model.browser.find_element(By.ID, "UserCheck_Login_Button").click()
        model.sleepRandom(1,2)
    except Exception as e:
        print("Error Occurred")
    model.closeBrowser()

if __name__ == "__main__":
    while True:
        main()
        print("Last Logged In at: ", time.ctime())
        time.sleep(10 * 60)