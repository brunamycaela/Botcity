

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    local = input('Qual o Estado:')
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    # Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = r"C:\Users\BlueShift\Documents\BotCity\chromedriver-win64\chromedriver.exe"

    # Opens the BotCity website.
    bot.browse("https://www.ibge.gov.br/cidades-e-estados")
    bot.maximize_window()

    # Implement here your logic...
    # Aceitar cookies (se necessário)
    bot.wait(3000)
    bot.find_element('//button[@class="cookie-btn"]', By.XPATH).click()
    bot.wait(3000)

    bot.find_element('//input[@class="navegacao-uf"]', By.XPATH).send_keys(local)
    bot.enter()

    bot.find_element('//button[@class="botao botao-dropdown"]', By.XPATH).click()
    bot.wait(3000)
    bot.find_element('//button[contains(text(), "XLSX")]', By.XPATH).click()
    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
