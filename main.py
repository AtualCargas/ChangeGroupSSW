from functions import *
from selenium import webdriver

''''''''''''''''''''''''''''''''''''
''' Todas as funções devem passar '''
''' o driver como parâmetro       '''
''''''''''''''''''''''''''''''''''''

# Usuários para realizar a mudança de Grupo separados por \n
usuarios = '''thiago'''

# URL do sistema, no caso o SSW
url = ("https://sistema.ssw.inf.br/")

# Navegador usado seguido do caminho de seu webdriver
driver = webdriver.Chrome(executable_path=".\chromedriver.exe")

# Realiza a conexão
driver.get(url)
print('>> Processando acesso ao site')
sleep()

# Realiza o login
login(driver, "dominio", "cpf", "user", "senha")
print('>> Processando login')
sleep()

# Acessa a operação
openOperation(driver, "925")
print('>> Processando operação')
sleep()

# Troca de janelas
window_before  = driver.current_window_handle
window_after = driver.window_handles
new_window = [x for x in window_after if x != window_before][0]
driver.close()
driver.switch_to.window(new_window)

# Para cada usuário, o loop irá acessar e trocar de grupo
for user in usuarios.split("\n"):
    # Pesquisa pelo usuário
    sendSearch(driver, user)
    print('>> Processando pesquisa por '+user)
    sleep()

    # Verifica se há algum pop-up na tela e aceita
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        sleep()
    except:
        pass
        
    # Troca de janela novamente
    window_before = driver.current_window_handle
    window_after = driver.window_handles
    new_window = [x for x in window_after if x != window_before][0]
    driver.switch_to.window(new_window)

    # Se o usuário não possui esses 4 elementos, ele está criando um novo
    if semCPF(driver) and semEmail(driver) and semNome(driver) and semGrupo(driver):
        driver.find_element_by_id("btn_fec").click()
    
    else:
        # Checa se existe CPF e E-mail
        if semCPF(driver):
            driver.find_element_by_id("cpf").send_keys(geradorDeCpf())

        if semEmail(driver):
            driver.find_element_by_id("email").send_keys('Sem e-mail')

        # Faz a mudança do grupo desejado
        changeGroup(driver, "54")
        print('>> Processando mudança de grupo')
        sleep()

    # Muda para a janela anterior
    driver.switch_to.window(window_before)