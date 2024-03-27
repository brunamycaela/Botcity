# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
import pandas as pd

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

    # Remova o comentário para definir o caminho do WebDriver
    bot.driver_path = r"C:\Users\BlueShift\Documents\BotCity\chromedriver-win64\chromedriver.exe"

    # Opens the BotCity website.
    bot.browse("https://rpachallenge.com/")
    bot.maximize_window() # aumentar a tela do chrome

    # Implement here your logic...
    # clicar no butão para realizar o dowloand do arquivo
    comeca = bot.find_element("//a[@class=' col s12 m12 l12 btn waves-effect waves-light uiColorPrimary center']",
                              By.XPATH)
    comeca.click()

    arquivo = r"C:\Users\BlueShift\PycharmProjects\BotCity\Desafio_RPA_–_Com_BotCity\challenge.xlsx"
    arquivo_excel = pd.read_excel(arquivo, sheet_name='Sheet1', engine='openpyxl')

    # aguarda alguns segundos para proseguir
    bot.wait(3000)

    # clicar no butão para começa as rodada
    comeca = bot.find_element("//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']", By.XPATH)
    comeca.click()
    bot.wait(5000)
    # Cria duas variáveis auxiliares que serão utilizadas no loop
    Contador = 0

    for i in range(0, len(arquivo_excel["First Name"])):

        FirstName = arquivo_excel.loc[Contador, 'First Name']
        LastName = arquivo_excel.loc[Contador, 'Last Name ']
        CompanyName = arquivo_excel.loc[Contador, 'Company Name']
        RoleInCompany = arquivo_excel.loc[Contador, 'Role in Company']
        Adress = arquivo_excel.loc[Contador, 'Address']
        Email = arquivo_excel.loc[Contador, 'Email']
        PhoneNumber = arquivo_excel.loc[Contador, 'Phone Number']

        bot.find_element("//label[contains(text(), 'First Name')]/following-sibling::input",
                         By.XPATH).send_keys(FirstName)
        bot.find_element("//label[contains(text(), 'Last Name')]/following-sibling::input",
                         By.XPATH).send_keys(LastName)
        bot.find_element("//label[contains(text(), 'Company Name')]/following-sibling::input",
                         By.XPATH).send_keys(CompanyName)
        bot.find_element("//label[contains(text(), 'Role in Company')]/following-sibling::input",
                         By.XPATH).send_keys(RoleInCompany)
        bot.find_element("//label[contains(text(), 'Address')]/following-sibling::input",
                         By.XPATH).send_keys(Adress)
        bot.find_element('//label[contains(text(), "Email")]/following-sibling::input',
                         By.XPATH).send_keys(Email)
        bot.find_element('//label[contains(text(), "Phone Number")]/following-sibling::input',
                         By.XPATH).send_keys(str(PhoneNumber))
        Contador += 1

        # clicar no butão para proxima rodada
        rodada = bot.find_element("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input", By.XPATH)
        rodada.click()
        bot.wait(2000)

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
