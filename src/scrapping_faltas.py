import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

def scrappFaltas(matricula, senha): 
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)
  driver.get("https://academico.iff.edu.br/qacademico/index.asp?t=1001")

  

  driver.find_element(By.NAME, "LOGIN").send_keys(matricula)
  driver.find_element(By.NAME, "SENHA").send_keys(senha)
  driver.find_element(By.CLASS_NAME, "btnOk").click()

  driver.get("https://academico.iff.edu.br/qacademico/index.asp?t=2071")

  time.sleep(1)

  td = driver.find_elements(By.XPATH, "//tr/td[contains(text(), 'Faltas')]/following-sibling::td")

  absences = 0
  for el in td:
    absences += int(el.text)

  print(f'O usuário possui {absences} faltas.') 

