import pyautogui
import time
import pandas
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")
time.sleep(5)
# entrar no no sistema da empresa 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login no sistema
# selecionar o campo de email
pyautogui.click(x=436, y=412)
# escrever o seu email
pyautogui.write("matheusmendesbmf@outlook.com") #emailfake
#passar para selecionar o campo da senha 
pyautogui.click(x=429, y=504)
#escrever a senha:
pyautogui.write("matheus01") #senhafake
#logar
pyautogui.click(x=675, y=570)
pyautogui.press("enter")

#Importar a base de dados
#instalar: pip install pandas numpy openpyxl
tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    #Cadastrar produto, até acabar a base de dados 
    pyautogui.click(x=403, y=292)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo de produto
    pyautogui.write(tabela.loc[linha, "produto"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco unitario
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")
    #custo do produtomatheusmendesbmf@outlook.com
        #enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    #subir a pagina
    pyautogui.scroll(5000)
    

