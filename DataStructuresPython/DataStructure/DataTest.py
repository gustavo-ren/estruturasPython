'''
Created on 25 de jan de 2017

@author: Gustavo
'''

#listas
listaString=["who", "wants", "to", "be", "king"]

for i in listaString:
    print (i.capitalize(), end=' ')
    
listaString.remove("to")
print()

for i in listaString:
    print (i.capitalize(), end=' ')
    
listaString.pop()
print()

for i in listaString:
    print (i.capitalize(), end=' ')
    
listaString.append("Ragnar")
print()

for i in listaString:
    print(i.capitalize(), end=' ')
    
listaString.pop()
print()
print()


dicionario = {1:"f", 2:"l", 3:"e", 4:"i"}

print(dicionario[2])

print(dicionario)

#deleta o elemento
del dicionario[2]

print(dicionario)

#exibe o tamanho
print("%d" %(len(dicionario)))

