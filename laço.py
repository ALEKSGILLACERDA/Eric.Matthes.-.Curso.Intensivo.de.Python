lista_1 = ['fernando', 'aleks', 'gay']
lista_2 = []
for elemento in lista_1:
    while lista_1:
        nova_lista = lista_1.pop()
        lista_2.append(nova_lista)

    print(lista_2[::-1])