# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from botcity.web.util import element_as_select
from botcity.web.parsers import table_to_dict
from botcity.plugins.excel import BotExcelPlugin

"""Para interagi com elementos web
//tag[@atributo='valor']
ex://select[@id='uf']"""


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# criamos uma nova intancia atravez de uma varialve
excel = BotExcelPlugin()
excel.add_row(['CIDADE', 'POPULACAO'])

def main():
    # Runner passa a url do servidor, o id da tarefa que está sendo executada,
    # o token de acesso e os parâmetros que esta tarefa recebe (quando aplicável).
    maestro = BotMaestroSDK.from_sys_args()
    # Busque o BotExecution com detalhes da tarefa, incluindo parâmetros
    execution = maestro.get_execution()

    #Log no botcity maestro manual
    #maestro.login(server='https://developers.botcity.dev', login='a476ae97-5807-46df-9237-86c5d056cb99',
                 # key='A47_DSIVYAELKZRXOLLHP0II')

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure se deseja ou não executar no modo headless
    bot.headless = False

    # Remova o comentário para alterar o navegador padrão para CHROME
    bot.browser = Browser.CHROME

    # Remova o comentário para definir o caminho do WebDriver
    bot.driver_path = r"C:\Users\BlueShift\Documents\BotCity\chromedriver-win64\chromedriver.exe"

    # Abre o site do Busca CEP.
    bot.browse("https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/index.php")

    # Captura e a seleção do Estado de SP.
    drop_uf = element_as_select(bot.find_element("//select[@id='uf']", By.XPATH))
    drop_uf.select_by_value("SP")

    # Selecionei o elemento button e cliquei no botão buscar(pesquisar).
    btn_pesquisar = bot.find_element("//button[@id='btn_pesquisar']", By.XPATH)
    btn_pesquisar.click()

    # tempo de espera para a proxima ação.(para carregar).
    bot.wait(3000)

    # Captura da tabela de dados com os nomes das cidades.
    table_dados = bot.find_element("//table[@id='resultado-DNEC']", By.XPATH)
    table_dados = table_to_dict(table=table_dados) # Transformação da Tabela em um dicionario.

    # Navegação para o site do IBGE.
    bot.navigate_to(r"https://cidades.ibge.gov.br/brasil/sp/panorama")

    int_contador = 1
    str_CidadeAnterior = ''
    for cidade in table_dados:

        str_cidade = cidade['localidade'] # Definimos o nomes da cidades

        if str_CidadeAnterior == str_cidade:
            continue

        if int_contador <= 5:

            campo_pesquisa = bot.find_element("//input[@placeholder='O que você procura?']", By.XPATH)
            campo_pesquisa.send_keys(str_cidade)

            opcao_cidade = bot.find_element(f'//a[span[contains(text(), "{str_cidade}")] and span[contains(text(), "SP")]]', By.XPATH)
            bot.wait(1000)
            opcao_cidade.click()

            bot.wait(2000)

            populacao = bot.find_element('//div[@class="indicador__valor"]', By.XPATH)
            str_populacao = populacao.text # trabsforma em texto

            print(str_cidade, str_populacao)
            excel.add_row([str_cidade, str_populacao])# adicionando uma nova linha na tabela na memoria do robo
            maestro.new_log_entry(activity_label='CIDADES', values={'CIDADE': f'{str_cidade}',
                                                                    'POPULACAO': f'{str_populacao}'})


            int_contador += 1
            str_CidadeAnterior = str_cidade
        else:
            print('Número de cidade já alcançado.')
            break
    # escrevendo em um arquivo excel
    excel.write(r'C:\Users\BlueShift\PycharmProjects\BotCity\intensivo_botcity\resources\Infos_Cidades.xlsx')


    # Implemente aqui sua lógica ...
    ...

    # Aguarde 3 segundos antes de fechar
    bot.wait(5000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

   # Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
         task_id=execution.task_id,
         status=AutomationTaskFinishStatus.SUCCESS,
         message="Task Finished OK."
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
