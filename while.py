sandwich_orders = ['pastrami' ,'misto quente', 'pastrami' , 'podrão', 'artesanal', 'pastrami' ]
new_sanduiches = []  #o exerxício pediu ra usar o laço while, mas não precisava, agora vou tentar fazer com o while

print('\n Não temos pastrami.')

while sandwich_orders:
   sanduiche = sandwich_orders.pop()
   if sanduiche != 'pastrami':
       new_sanduiches.append(sanduiche)


for sanduiche in new_sanduiches:
    print(f'O seu {sanduiche} está pronto')

