sandwich_orders = ['pastrami' ,'misto quente', 'pastrami' , 'podrão', 'artesanal', 'pastrami' ]
finished_sandwiches = []
print('\n No momento estamos sem pastrami \n' )
for sanduiche in sandwich_orders:
    print(f' preparei o seu {sanduiche}')
    finished_sandwiches.append(sanduiche)
print()
for sauiche_pronto in finished_sandwiches:
    print(f'o {sauiche_pronto} está pronto')
