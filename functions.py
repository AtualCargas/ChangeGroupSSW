import csv
import time
from cpf import geradorDeCpf
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def sleep():
    """Acesso rápido ao Sleep do Python com valor de 2 segundos"""
    time.sleep(2)


def get_elements_by_xpath(driver, xpath):
    """Realiza busca por caminho
    
    Params:\n
        xpath (string): É o caminho do qual você está buscando
    
    Return:\n
        element = O elemento encontrado"""
    return [entry.text for entry in driver.find_elements_by_xpath(xpath)]


def sendTo(driver, idElemento, string):
    """Envia dados para um certo elemento do html
    
    Params:\n
        idElemento (string): O ID do elemento dentro do HTML\n
        string (string): O valor que deseja inserir no campo

    Não há retorno
    """
    driver.find_element_by_id(idElemento).send_keys(string)


def login(driver, dominio, cpf, usuario, senha):
    """Envia dados para fazer o login no SSW

    Params:\n
        domínio (string) = É o domínio do usuário\n
        cpf (string) = É o cpf do usuário\n
        usuario (string) = É o usuário\n
        senha (string) = É senha do usuário

    Não há retorno
    """
    sendTo(driver, 1, dominio)
    sendTo(driver, 2, cpf)
    sendTo(driver, 3, usuario)
    sendTo(driver, 4, senha)
    driver.find_element_by_id(5).click()


def openOperation(driver, operation):
    """Abre a operação informada dentro do SSW
    
    Params:\n
        operation (string) = A operação do qual se quer acessar\n

    Não há retorno
    """
    sendTo(driver, 3, operation)


def sendSearch(driver, pesquisa):
    """Preenche o campo de pesquisa dentro da operação
    
    Params:\n
        pesquisa (string) = O que deseja buscar\n

    Não há retorno
    """

    # Pega a referência do input
    input = driver.find_element_by_id(2)
    input.clear()

    # Move a referência para o input e executa um double click
    actions = ActionChains(driver).move_to_element(input)
    actions.double_click(input).perform()
    
    # Envia os dados e pesquisa
    input.send_keys(pesquisa)
    driver.find_element_by_id(3).click()


def changeGroup(driver, novoGrupo):
    """Preenche o campo de grupo dentro do usuário
    
    Params:\n
        driver (driver) = É o driver de qual browser você está usando\n
        novoGrupo (string) = Numeração do grupo ao qual o usuário será movido

    Não há retorno
    """

    # Pega a referência do input
    input = driver.find_element_by_name("grupo")
    # Move a referência para o input e executa um double click
    actions = ActionChains(driver).move_to_element(input)
    actions.double_click(input).perform()
    # Envia os dados e salva
    driver.find_element_by_name("grupo").send_keys(novoGrupo)
    driver.find_element_by_id("btn_env").click()


def semCPF(driver):
    """Checa se o campo de CPF está preenchido
    
    Return:\n
        (boolean) True se não existir CPF
    """
    cpf = driver.find_element_by_id("cpf").get_attribute('value')
    return cpf == ""


def semEmail(driver):
    """Checa se o campo de E-mail está preenchido
    
    Return:\n
        (boolean) True se não existir E-mail
    """
    email = driver.find_element_by_id("email").get_attribute('value')
    return email == "" 


def semNome(driver):
    """Checa se o campo de Nome está preenchido
    
    Return:\n
        (boolean) True se não existir Nome
    """
    nome = driver.find_element_by_id("nome").get_attribute('value')
    return nome == ""


def semGrupo(driver):
    """Checa se o campo de Grupo está preenchido
    
    Return:\n
        (boolean) True se não existir Grupo
    """
    grupo = driver.find_element_by_id("grupo").get_attribute('value')
    return grupo == "000"     