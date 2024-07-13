# Importa o módulo de Tempo
import time
# Importa a função tqdm para exibir barras de progresso
from tqdm import tqdm

# Importa ChromeDriverManager do webdriver_manager para gerenciamento automático do ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

#  IMPORTS DO SELENIUM #
# Importa o módulo webdriver do Selenium para automatização de navegador web
from selenium import webdriver
# Importa o enumerador By do Selenium para localização de elementos na página web
from selenium.webdriver.common.by import By
# Importa a classe WebDriverWait do Selenium para esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
# Importa expected_conditions do Selenium para condições esperadas em esperas explícitas, renomeando como EC
from selenium.webdriver.support import expected_conditions as EC
# Importa as exceções NoSuchElementException e TimeoutException do Selenium para tratamento de erros específicos
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# Importa a classe Service do Selenium para controle do serviço do navegador (por exemplo, ChromeDriver)
from selenium.webdriver.chrome.service import Service


#comando para criar e atualizar executavel(pyinstaller --onefile --ico=icone.ico Vmbot.py)

print("Iniciando programa")

total_processo = 100
with tqdm(total=total_processo, desc="Processando") as pbar:        
        # Configurações do Chrome
        chrome_options = webdriver.ChromeOptions()
        pbar.update(10)
        chrome_options.add_argument("--log-level=3")  # Define o nível de log como 'ERROR'
        pbar.update(10)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Exclui a mensagem de log do DevTools
        pbar.update(10)
        # Configurar o serviço do ChromeDriver sem logs
        chrome_service = Service(executable_path=ChromeDriverManager().install())
        pbar.update(10)
        # Inicializar o driver do Selenium com as opções configuradas e o serviço
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        pbar.update(10)
        driver.get("https://vmpay.vertitecnologia.com.br/nutricar_/tools/products")
        pbar.update(10)
        email = driver.find_element('xpath', '//*[@id="user_email"]').send_keys('')
        pbar.update(10)
        senha = driver.find_element('xpath', '//*[@id="user_password"]').send_keys('')
        pbar.update(10)
        pbar.update(total_processo - pbar.n) # Garante que a barra de progresso chegue a 100%
        
print("Processamento concluído!")
print("-")
input("Precione ENTER depois do login")

def maquina():
    print("-")
    print("-")

    while True:
        try:
            pesqeuisa_de_maquina = driver.find_element('xpath', "//input[contains(@placeholder, 'Máquina')]")
            print("-")
            print("Campo de pesquisa de máquinas encontrado.")
            print("-")
            break
        except NoSuchElementException:
            print("-")
            print("Campo de pesquisa de máquinas não encontrado. Volte para PESQUISA DE PRODUTO e aguarde")
            print("-")
            time.sleep(3)

    while True:
        print("Para reiniciar o Programa digite----(1)")
        print("Para fechar o programa digite-------(2)")
        print("")
        pesquisa = input("Digite o Numero da Maquina ou as Opções a cima:")
        print("-")
        if pesquisa.lower() == '2':
            print("Saindo do programa...")
            print("-")
            driver.quit()
            break
        elif pesquisa.lower() == '1':
            print("Reiniciando o programa...")
            print("-")
            def nova_guia():
                driver.execute_script("window.open('https://vmpay.vertitecnologia.com.br/nutricar_/tools/products', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
            nova_guia()
            maquina()
            break
        else:
            max_tentativas = 3
            tentativa = 1

            while tentativa <= max_tentativas:
                try:
                    pesqeuisa_de_maquina.clear()
                    pesqeuisa_de_maquina.send_keys(pesquisa)
                    print("-")
                    print(f"Tentativa {tentativa}: Texto '{pesquisa}' lançado no site.")
                    print("-")

                    wait = WebDriverWait(driver, 5)
                    option_xpath = f"//li[contains(@class, 'select2-results__option') and text()='{pesquisa}']"
                    option = wait.until(EC.visibility_of_element_located((By.XPATH, option_xpath)))

                    if option:
                        option.click()
                        print("-")
                        print(f"Opção '{pesquisa}' selecionada.")
                        print("-")
                        break
                except TimeoutException:
                    print("-")
                    print(f"Tentativa {tentativa}: Opção '{pesquisa}' não encontrada no site.")
                    print("-")

                tentativa += 1
            else:
                print("-")
                print(f"Limite de ({max_tentativas}) tentativas foi atingido. O elemento {pesquisa} não foi encontrado.")
                print("-")

maquina()