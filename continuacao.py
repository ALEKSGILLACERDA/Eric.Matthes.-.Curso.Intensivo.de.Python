favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
pessoas = ['jen', 'sarah', 'rob', 'gay', 'edward', 'phil']

for name in pessoas:
    if name in favorite_languages:
        print(f'Olá {name} muito obrigado por participar,sua lingagem favorita é {favorite_languages[name]} ')
    else:
        print(f'venha participar da enquete {name}')