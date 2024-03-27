# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

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

    bot = DesktopBot()
    bot.browse("https://www.youtube.com/@google")
    bot.wait(3000)

    # Implemente aqui sua lógica...
    if not bot.find( "Sobre", matching=0.97, waiting_time=10000):
        not_found("Sobre")
    bot.click()
    bot.wait(2000)

    # Role para baixo 5 vezes.
    bot.scroll_down(clicks=5)
    
    # selecionando o numeroas de escritos
    if not bot.find_text( "inscritos", threshold=230, waiting_time=10000):
        not_found("inscritos")
    bot.click_relative(-33, 10)

    # Selecionando o número de assinantes
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando e imprimindo o valor
    bot.control_c()
    subscribers = bot.get_clipboard()
    print(f"Subscribers => {subscribers} mi.")

    if not bot.find_text( "visualizacao", threshold=230, waiting_time=10000):
        not_found("visualizacao")
    bot.click_relative(-54, 9)

    # Selecionando o número de visualizações
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando e imprimindo o valor
    bot.control_c()
    views = bot.get_clipboard()
    print(f"Views => {views}.")

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

