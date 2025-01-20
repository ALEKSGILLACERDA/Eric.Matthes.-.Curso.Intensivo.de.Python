favorite_languages = {'ana': 'java', 'bruno': 'py', 'belle': 'c', 'phill': 'c#'}
friends = ['phill', 'ana']
for names in favorite_languages.keys():
    if names in friends:
        print(f'Oi {names.title()}')
