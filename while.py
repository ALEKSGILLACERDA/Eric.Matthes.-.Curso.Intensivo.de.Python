sandwich_orders = ['pastrami' ,'misto quente', 'pastrami' , 'podrão', 'artesanal', 'pastrami' ]
finished_sandwiches = []
new_sanduiches = []  #o exerxício pediu ra usar o laço while, mas não precisava, agora vou tentar fazer com o while

print('\n Não temos pastrami.')

while 'pastrami'in sandwich_orders:
       sandwich_orders.remove('pastrami')

for sanduiche in sandwich_orders:
    print(f'O seu {sanduiche} está pronto')

