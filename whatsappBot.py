
# Bibliotecas 
import pandas as pd
from selenium import webdriver # Abre o navagador.
from selenium.webdriver.common.keys import Keys # Enviar a mensagem para as pessoas especificas.
import time # Contador de tempo.
import urllib #Codifica o texto para o link de URl.

contatos_df = pd.read_excel('Enviar.xlsx', engine='openpyxl') # Ler o arquivo

navegador = webdriver.Chrome() # Criar um navegador novo
navegador.get('https://web.whatsapp.com/') # Vai até o link especifico.

 # Esperar a tela do whatsapp carregar
while len(navegador.find_elements_by_id('side')) < 1: # Lista de item
    time.sleep(1) # Esperar um segundo e verificar se existe a tela esperada e se ela carregou.

# Login já feito no WhatsApp Web
for i, mensagem in enumerate(contatos_df['Mensagem']): # Pega o texto e armazena em uma variavel chamada 'Mensagem'

    # enviar uma mensagem para a pessoa
    pessoa = contatos_df.loc[i, 'Pessoa'] # i - indice, Pessoa - coluna. Localiza o indice e a pessoa na lista e sempre vai atualizando.
    numero = contatos_df.loc[i, 'Número'] # 'Número' - contato
    texto = urllib.parse.quote(f"Olá, {pessoa}! {mensagem}") # Codifica a mensagem. Aqui personaliza a mensagem que será enviada para a pessoa especifica.
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}' # Qual o número e a mensagem que desejar enviar a mensagem.
    navegador.get(link) # Navegar no link.

     # esperar a tela do whatsapp web carregar
    while len(navegador.find_elements_by_id("side")) < 1: # -> Se a lista for vazia -> o elemento não existe ainda.
        time.sleep(1) # Esperar um segundo e verificar se existe a tela esperada e se ela carregou.

    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER) # Enviar mensagem a pessoa especifica. O Keys permitirar apertar o ENTER para enviar a mensagem.
    time.sleep(10) # Espera 10 segundo para enviar a mensagem.

