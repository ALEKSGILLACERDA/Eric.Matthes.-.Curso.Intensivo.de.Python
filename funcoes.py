usernames =  ['hannah', 'ty', 'margot']

def greet_users(names):
  for name in names:
    msg = f'Hello {name.title()}'
    print(msg)
#passamos um parametro em greet user, e usamos a lista como argumento, ficou um pouco confuso
#mas lembra que podemos colocar qualquer variável na função? e depois chamar qualquer coisa
#chamamos isso de argumento posicional, no caso names aí se torna a lista usernames
#quando a gente chama a função com a lista, complicado, mas funciona
greet_users(usernames)
