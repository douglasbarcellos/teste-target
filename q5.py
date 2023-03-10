string = 'Exemplo de string'

# converter a string em uma lista de caracteres
lista = list(string)

# percorrer a lista e trocar a posição dos caracteres
for i in range(len(lista)//2):
    temp = lista[i]
    lista[i] = lista[len(lista)-1-i]
    lista[len(lista)-1-i] = temp

# converter a lista de volta para string
nova_string = ''.join(lista)

print(nova_string)
