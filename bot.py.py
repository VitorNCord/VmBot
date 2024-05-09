import os
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#comando para criar e atualizar executavel(pyinstaller --onefile --ico=icone.ico bot.py.py)


total_processo = 100
# Configurações do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Define o nível de log como 'ERROR'
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Exclui a mensagem de log do DevTools

# Configurar o serviço do ChromeDriver sem logs
chrome_service = Service(executable_path=ChromeDriverManager().install(), log_path=os.devnull)

# Inicializar o driver do Selenium com as opções configuradas e o serviço
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://vmpay.vertitecnologia.com.br/nutricar_/tools/products")

with tqdm(total=total_processo, desc="Processando") as pbar:
    # Loop para simular processamento
    for _ in range(total_processo):
        # Atualiza a barra de progresso
        pbar.update(1)
        time.sleep(0.01)  # Simula algum processamento

print("Processamento concluído!")

input("Apos fazer login precione ENTER para continuar")

def maquina():
    print("-")
    print("-")

    while True:
        try:
            machines_search_box = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Máquina')]")
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
        print("Para reiniciar o Progama digite----(1)")
        print("Para fechar o progama digite-------(2)")
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
            with tqdm(total=total_processo, desc="Processando") as pbar:
                    # Loop para simular processamento
                for _ in range(total_processo):
                    # Atualiza a barra de progresso
                    pbar.update(1)
                    time.sleep(0.01)  # Simula algum processamento
            maquina()
            break
        else:
            max_tentativas = 3
            tentativa = 1

            while tentativa <= max_tentativas:
                try:
                    machines_search_box.clear()
                    machines_search_box.send_keys(pesquisa)
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