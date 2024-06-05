import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

header = {
  'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Links
monitor_samsung = 'https://www.buscape.com.br/monitor/monitor-ips-24-samsung-full-hd-lf24t350fhl?_lc=88&searchterm=Samsung%20%20T350#historico-de-precos'

monitor_aoc = 'https://www.buscape.com.br/monitor/monitor-gamer-led-ips-24-aoc-full-hd-24g2he5?_lc=88&searchterm=Monitor%20Gamer%20AOC%20SPEED%2024%2075Hz%20IPS%201ms%2024G2HE5#lista-de-ofertas'

mouse = 'https://www.amazon.com.br/INPHIC-Ergon%C3%B4mico-Recarreg%C3%A1vel-Receptor-Computer/dp/B085FRSC2M?th=1'

mesa = 'https://www.amazon.com.br/dp/B0BQ3PB9N2?linkCode=sl1&tag=matheusmp01-20&linkId=3fac0039d8312a908637e703a899c14a&language=pt_BR&ref_=as_li_ss_tl&th=1'

# Lista de links
lista = [monitor_samsung, monitor_aoc, mouse, mesa]

# Funções
def buscape(soup):
  string_preco = soup.find('strong', class_='Text_Text__h_AF6 Text_DesktopHeadingM__C_e4f')
  string_nome = soup.find('h1', class_='Text_Text__h_AF6 Text_MobileTitleM__24Ah0 Text_MobileTitleLAtLarge__CTrpI')
  # Usando expressão regular para encontrar o valor entre os caracteres '>' e '<'
  padrao = r'>\s*(.*?)\s*<'
  resultadoPreco = re.search(padrao, str(string_preco))
  resultadoNome = re.search(padrao, str(string_nome))
  # Se um resultado for encontrado, imprime o valor
  if resultadoPreco and resultadoNome:
    valor = resultadoPreco.group(1)
    nome = resultadoNome.group(1)
    
    print(nome,"\nPreço: ", valor, "\n")
  else:
      print("Nenhum valor encontrado.")


def amazon(soup):
  #<span class="aok-offscreen">   R$&nbsp;63,95  </span>
  string_preco = soup.find('span', class_='a-offscreen')
  string_nome = soup.find('span', class_='a-size-large product-title-word-break')
  # Usando expressão regular para encontrar o valor entre os caracteres '>' e '<'
  padrao = r'>\s*(.*?)\s*<'
  resultadoPreco = re.search(padrao, str(string_preco))
  resultadoNome = re.search(padrao, str(string_nome))
  # Se um resultado for encontrado, imprime o valor
  if resultadoPreco and resultadoNome:
    valor = resultadoPreco.group(1)
    nome = resultadoNome.group(1)

    print(nome,"\nPreço: ", valor.replace("R$", "R$ "), "\n")
  else:
      print("Nenhum valor encontrado.")


def mercadoLivre(soup):
  # Encontrar a tag meta com itemprop="price"
  string_valor = soup.find('meta', {'itemprop': 'price'})
  string_nome = soup.find('h1', class_='ui-pdp-title')


  resultadoNome = re.search(r'>(.*?)<', str(string_nome))
  # Verificar se a tag foi encontrada
  if string_valor and 'content' in string_valor.attrs:
    # Obter o valor do atributo content
    valor = string_valor['content'].replace('.',',')
    nome = resultadoNome.group(1) 
    print(f'{nome}.\nPreço: R$ {valor}\n')
  else:
    print("Nenhum valor encontrado.")
    

# Loop principal
for item in lista:
  site = requests.get(item, headers=header)
  soup = BeautifulSoup(site.content, 'html.parser')

  if "www.buscape.com" in item:
    buscape(soup)
  if "www.amazon.com" in item:
    amazon(soup)
  if "mercadolivre.com.br" in item:
    mercadoLivre(soup)

  

'''<div class="a-section a-spacing-micro">                        <span class="a-price aok-align-center" data-a-size="xl" data-a-color="base"><span class="a-offscreen">R$465,90</span><span aria-hidden="true"><span class="a-price-symbol">R$</span><span class="a-price-whole">465<span class="a-price-decimal">,</span></span><span class="a-price-fraction">90</span></span></span>        <span id="taxInclusiveMessage" class="a-size-mini a-color-base aok-align-center aok-nowrap">  </span>             </div>
'''