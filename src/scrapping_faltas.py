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

  time.sleep(1)

  driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[3]/a").click()

  faltas = driver.find_elements(By.XPATH, "//tr/td[contains(text(), 'Faltas')]/following-sibling::td")
  aulas = driver.find_elements(By.XPATH, "//tbody/tr/td[contains(text(), 'Aulas ministradas')]/following-sibling::td/a[1]")

  numFaltas = 0
  numeroAulas = 0

  for el in faltas:
    numFaltas += int(el.text)
  
  for el in aulas:
    numeroAulas += int(el.text)

  # numFaltas -= 41
  porcentFaltas = (numFaltas * 100) / numeroAulas

  print(f"{round(porcentFaltas, 2)}%")



