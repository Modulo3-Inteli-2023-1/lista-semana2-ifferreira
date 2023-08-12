#Ivan Fellipy Gonçalves Ferreira
#  Se achar necessario, faça import de outras bibliotecas
import numpy as np




# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
  lista_de_palavras_da_frase = frase.split()
  lista_de_palavras_unicas_da_frase = np.unique(np.array(lista_de_palavras_da_frase))
  print(len(lista_de_palavras_unicas_da_frase))

# Teste a sua função aqui (caso ache necessário)
#conta_palavras_unicas('um um um um um um um um um um um um um um um dois um um tres dois dois')













