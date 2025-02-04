sandwich_orders = ['pastrami' ,'misto quente', 'pastrami' , 'podrão', 'artesanal', 'pastrami' ]
finished_sandwiches = []
new_sanduiches = []
print('\n No momento estamos sem pastrami \n' )
for sanduiche in sandwich_orders:
    if sanduiche != 'pastrami':
        new_sanduiches.append(sanduiche)
    sanduiches_de_hoje = ', '.join(new_sanduiches)
print(f'os sanduiches de hoje são {sanduiches_de_hoje}')

for sanduiche in new_sanduiches:
    print(f' preparei o seu {sanduiche}')
    finished_sandwiches.append(sanduiche)
print()
for sauiche_pronto in finished_sandwiches:
    print(f'o {sauiche_pronto} está pronto')
