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
    bot.browse("https://www.youtube.com/@pythonbrasiloficial")

    # Implement here your logic...
    if not bot.find( "sobre", matching=0.97, waiting_time=10000):
        not_found("sobre")
    bot.click()
    
    if not bot.find( "inscritos", matching=0.97, waiting_time=10000):
        not_found("inscritos")
    bot.click_relative(-29, 12)

    # Selecionando o valor da página
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando o valor do clipboard
    bot.control_c()
    numero_inscritos = bot.get_clipboard()
    print(f"Inscritos => {numero_inscritos} mil.")
    
    if not bot.find( "visualizacao", matching=0.97, waiting_time=10000):
        not_found("visualizacao")
    bot.click_relative(-29, 6)

    # Selecionando o valor da página
    bot.mouse_down()
    bot.move_relative(-50, 0)
    bot.mouse_up()

    # Coletando o valor do clipboard
    bot.control_c()
    numero_visualizacoes = bot.get_clipboard()
    print(f"Visualizações => {numero_visualizacoes}.")

    bot.control_w()
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
