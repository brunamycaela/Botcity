# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from random import choice
# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
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
    bot.browse("https://minesweeper.online/")
    bot.maximize_window()
    bot.wait(2000)
    # Implemente aqui sua lógica...

    bot.find_element("//img[@src='/img/homepage/expert.png']", By.XPATH).click()

    try:
        # Número máximo de tentativas para encontrar e clicar em elementos
        max_tentativas = 10
        tentativas = 0

        while tentativas < max_tentativas:
            # Localizar todos os elementos desejados
            elementos = bot.find_elements("//div[@class='cell size24 hd_closed']", By.XPATH)

            if elementos:
                # Escolher aleatoriamente um elemento
                elemento_escolhido = choice(elementos)

                # Realizar ação no elemento escolhido (por exemplo, clicar)
                elemento_escolhido.click()
                bot.wait(2000)

                # Incrementar o número de tentativas
                tentativas += 1
            elif bot.find_elements("//div[@class='cell size24 hd_opened hd_type10']", By.XPATH):
                print("BLooww.")
                bot.wait(3000)
                break  # Interrompe o loop quando a condição é atendida

            else:
                print("Nenhum elemento encontrado. Encerrando.")
                break

    finally:
    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
        bot.wait(2000)
        bot.stop_browser()

    # Finalizando tarefa no Maestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()


