import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def scrappNotas(matricula, senha):
    # options = webdriver.ChromeOptions()
    # options.add_argument()
    driver = webdriver.Chrome()
    driver.get("https://academico.iff.edu.br/qacademico/index.asp?t=1001")

    driver.find_element(By.NAME, "LOGIN").send_keys(matricula)
    driver.find_element(By.NAME, "SENHA").send_keys(senha)
    driver.find_element(By.CLASS_NAME, "btnOk").click()
    time.sleep(2)

    driver.get("https://academico.iff.edu.br/qacademico/index.asp?t=2032")

    time.sleep(1)

    cont = 3
    data = []

    while cont < 20:
        nomeDisciplina = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[1]').text
        primeiroBim = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[6]').text
        segundoBim = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[8]').text
        terceiroBim = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[13]').text
        quartoBim = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[15]').text
        RS1 = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[10]').text
        RS2 = driver.find_element(
            By.XPATH, f'/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[4]/tbody/tr[{cont}]/td[17]').text

        possuiRS1 = False
        possuiRS2 = False

        if (primeiroBim == ' '):
            primeiroBim = '0.0'

        if (segundoBim == ' '):
            segundoBim = '0.0'

        if (terceiroBim == ' '):
            terceiroBim = '0.0'

        if (quartoBim == ' '):
            quartoBim = '0.0'

        primeiroBim = primeiroBim.replace(',', '.')
        segundoBim = segundoBim.replace(',', '.')
        terceiroBim = terceiroBim.replace(',', '.')
        quartoBim = quartoBim.replace(',', '.')

        primeiroBim = float(primeiroBim)
        segundoBim = float(segundoBim)
        terceiroBim = float(terceiroBim)
        quartoBim = float(quartoBim)

        if (RS1 != ' ' and RS1 != ',00'):
            RS1 = RS1.replace(',', '.')

            if (float(RS1) > ((primeiroBim + segundoBim) / 2)):
                primeiroBim = float(RS1)
                segundoBim = float(RS1)
                possuiRS1 = True

        if (RS2 != ' ' and RS2 != ',00'):
            RS2 = RS2.replace(',', '.')

            if (float(RS2) > ((terceiroBim + quartoBim) / 2)):
                terceiroBim = float(RS2)
                quartoBim = float(RS2)
                possuiRS2 = True

        notaRestante = 24 - (primeiroBim + segundoBim +
                             terceiroBim + quartoBim)

        cont = cont + 1
        ptsFaltantes = "Não possui nota restante" if notaRestante == 24 else round(notaRestante, 1)

        obj =  {nomeDisciplina, primeiroBim,
                segundoBim,  terceiroBim,  
                quartoBim, possuiRS1, 
                possuiRS2, ptsFaltantes} 
        notas = open("notas.json", "w")
        json.dump(nomeDisciplina, notas)
        json.dump(primeiroBim, notas)
        json.dump(segundoBim, notas)
        json.dump(terceiroBim, notas)
        json.dump(quartoBim, notas)
        json.dump(ptsFaltantes, notas)


        time.sleep(0.5)



scrappNotas("202310490331", "vviinnii@15")
