from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# abre a página na web
browser.get('https://web.whatsapp.com/')

#tempo para QR Code
time.sleep(20)

#pesquisa nome
pesquisar = browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
pesquisar.click()
pesquisar.send_keys('Matheus')
pesquisar.send_keys(Keys.ENTER)

#envia mensagem
texto = browser.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
texto.click()

for i in range(100):
    texto.send_keys('Oi')
    texto.send_keys(Keys.ENTER)