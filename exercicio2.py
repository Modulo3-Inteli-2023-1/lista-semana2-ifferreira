#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
  lista_letras_da_string1 = []
  lista_letras_da_string2 = []
  
  def separar_letras(string, lista):
    for letra in string:
      lista += letra
      lista.sort()
    
  separar_letras(string1, lista_letras_da_string1)
  separar_letras(string2, lista_letras_da_string2)
  
  if lista_letras_da_string1 == lista_letras_da_string2:
    print(True)
  else:
    print(False)


# Teste a sua função aqui (caso ache necessário)
#is_anagram('pedra', 'padre')










