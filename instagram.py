from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import csv
#Bot para 2 amigos
#Fazer a transformação manual, onde a primeira rodada começando com 0, precisa criar no diretório o contator-linha 
#e alterar o CSV com valor 1 obs: vai rodar de 5 em 5 porém exclui o primeiro amigo sempre, ai precisa ver se for impar pode incluir manual esse nome, se não, deixe ele de fora mesmo
#para você pegar o último da lista basta rodar o interador como -1 em python.
# Para salvar arquivo csv com o valor dentro dele antes de rodar, basta alterar ele e comando (control b), depois feche sem salvar, por incrivel que pareça ele salva kkkkkkk
#------Abaixo------ Link de teste 
#https://www.instagram.com/p/BproW0oHFn-/

class Imdb:
        def __init__(self, driver, *, file='contador.csv'):
            self.driver = driver
            self.driver1 = driver
            self.base = 'https://www.instagram.com'
            self.base_url = f'{self.base}/accounts/login/'
            self.url_site1 = f'https://www.instagram.com/p/BproW0oHFn-/'
            ff.get(self.base)
            sleep(1)
            ff.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button").click()
            user = ff.find_element_by_css_selector('#email')
            user.send_keys('user')
            password = ff.find_element_by_css_selector('#pass')
            password.send_keys('senha')
            login = ff.find_element_by_css_selector("#loginbutton")
            login.click()
            sleep(1)
            self.cont = 0
            self.contador = 0
            self.file = file
            with open('contador.csv') as csv_file:
                arq_contador = csv_file.readlines()
            arq_cont = list(map(lambda x: x.strip().split(';'), arq_contador))

            self.hard = int(arq_cont[0][0])
            if(self.hard == 0):
                self.h = self.hard
            else:
                self.hard = int(arq_cont[0][0])
                self.h = self.hard
            sleep(1)
            try:
                ff.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
                sleep(1)
                ff.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
            except:
                sleep(3)
                ff.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]').click()
                sleep(1)
                ff.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
                
        def abrir(self):
            if(self.hard  == 0):
                imdb.scrap()
            else:
                ff.get(self.url_site1)
                ff.execute_script("window.scrollTo(0, 1080)")
                sleep(1)
                with open('contador-linha.csv') as csv_files:
                    arq_contadores = csv_files.readlines()

                arq_conts = list(map(lambda x: x.strip().split(';'), arq_contadores))
                self.hards = str(arq_conts[0][0])
                
                #pegar o última posição para rodar mais 5 nomes seguintes
                ultimoNome = self.hards.split(',')[-11].strip(" '[]' ")
                primeiroNome = self.hards.split(',')[0].strip(" '[]' ")
                while(self.cont < 5):
                    nome1 = self.hards.split(',')[self.h].strip(" '[]' ")
                    nome2 = self.hards.split(',')[self.h + 1].strip(" '[]' ")
                    
                    #Verificação se o nome na posição do último a ser publicado, é igual ao nível que estamos, para pular e pegar os últimos 5, 
                    if(ultimoNome == nome1):
                        print(self.h)
                        self._write_csv(f'{self.h + 1}\n')
                        print('---------- Verificar os nomes se repetiram ou não SUCESSO! ----------')
                        ff.quit()
                    self.nome = (f'@{nome1} @{nome2}')
                    nome = self.nome
                    print(self.cont)
                    print(nome)
                    txt = ff.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
                    actions = webdriver.ActionChains(self.driver)
                    actions.move_to_element(txt)
                    actions.click()
                    actions.send_keys(nome).send_keys(Keys.TAB).send_keys(Keys.ENTER).send_keys(Keys.RETURN)
                    actions.click().click()
                    
                    #Teste sem enviar os nomes basta habilitar linha abaixo
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    sleep(1)
                    
                    #não repete nomes de 2 em 2, varificar o primeiro nome que ficou sem escrever,
                    # se faltar nomes para enviar, ele fica repetindo sempre os últimos enviados. (list index out of range) e não altera o self.h
                    self.h += 2
                    self.cont += 1
                    ff.get(self.url_site1)
                    ff.execute_script("window.scrollTo(0, 1080)")
                    sleep(1)
                else:
                    self._write_csv(f'{self.h}\n')
                    print("Acabou as 5 interações")
                ff.quit()
                
        def _write_csv(self, fmt_string):
        
            # com a troca do 'w' por 'a' ele incrementa um número no arquivo
            with open(self.file, 'w') as file:
                file.write(fmt_string)
                
        def _write_csv1(self, fmt_string):
            with open(self.file, 'w') as file:
                file.write(fmt_string)

        def scrap (self):
        
            #Vai trocar de pessoa? -> Troque linha abaixo
            sleep(2)
            ff.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
            sleep(3)
            j = 0
            pop = ff.find_element_by_xpath('/html/body/div[3]/div/div/div[2]')
            ff.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop)
            ff.execute_script(f"arguments[0].scrollTop = arguments[0].scrollTop - 1000", pop)
            
            #Vai trocar de pessoa? -> #57 matilde-ozzy 19 johndelara1 e 10 no johndelara11 vezes pois é quantas vezes rodam de 10 em 10 seguidores no popup
            while(j < 10): 
                sleep(1)
                
                #Vai trocar de pessoa? -> Troque linha abaixo matilde -> 2000 || john -> 500
                self.mm = 500
                ff.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop)
                sleep(1)
                ff.execute_script(f"arguments[0].scrollTop = arguments[0].scrollTop - {self.mm}", pop)
                j = j + 1
            self.hard = 1
            imdb.persistir_csv()
            
        def persistir_csv(self):
            bs_obj = bs(ff.page_source, 'html.parser')
            
            #Verifique se a classe está correta, o instagram altera sempre
            todos = bs_obj.find('div',{'class': 'PZuss'})
            linhas = todos.find_all('li')
            maximo = len(linhas)
            h = self.h
            stri = "@"
            nomes = []
            nome = ''
            while(h < maximo-1):
                amigo1 = linhas[h].find('button').text
                if(amigo1 == 'Following'):
                    nome = linhas[h].find_all('div')[4].text
                    nomes.append(nome)
                    h += 1
                else:
                    print(h)
                    print('OPS!!!')
                    h += 1
                print(nomes)
            self._write_csv1(f'{nomes}\n')
            imdb.abrir()
        
ff = webdriver.Chrome()
imdb = Imdb(ff)
imdb.abrir()
ff.quit()