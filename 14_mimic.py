"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys


def filtro(linha):
  return linha.replace(',', '') \
    .replace('.', '') \
    .replace(':', '') \
    .replace('!', '') \
    .replace('?', '') \
    .replace('--', '') \
    .replace('`', '') \
    .replace('"', '') \
    .replace(';', '')



def mimic_dict(filename):
  lista_palavras = []
  with open(filename, 'r') as f:
    for linha in f:
      linha = filtro(linha)
      for palavra in linha.split():
        lista_palavras.append(palavra.lower())
  
  dict_opcoes = {}
  dict_opcoes[''] = [lista_palavras[0]]
  pos = 0
  pos_max = len(lista_palavras) - 1
  
  for palavra in lista_palavras:
    if pos <= pos_max:
      if not palavra in dict_opcoes:
        dict_opcoes[palavra] = []
      proxima_palavra = lista_palavras[pos+1] if not pos == pos_max else ''
      if not proxima_palavra in dict_opcoes[palavra]:
        dict_opcoes[palavra].append(proxima_palavra) 
      
      pos += 1

  return dict_opcoes

  

  
def print_mimic(mimic_dict, word):
  """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
  # +++ SUA SOLUÇÃO +++
  MAX_PALAVRAS = 200
  resultado = []
  for i in range(MAX_PALAVRAS):
    proxima = random.choice(mimic_dict[word])
    resultado.append(proxima)
    word = proxima

  print(' '.join(resultado)) 


# Chama mimic_dict() e print_mimic()
def main():
  if len(sys.argv) != 2:
    print('Utilização: ./14_mimic.py file-to-read')
    sys.exit(1)
 
  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')
  

if __name__ == '__main__':
  main()
