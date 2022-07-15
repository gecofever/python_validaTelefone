from Telefonebr import Telefonebr
import re

telefone = "558333415560"
telefone_objeto = Telefonebr(telefone)

#Primeira Possibilidade
#padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

#telefone_objeto.format_numero()

print (telefone_objeto)