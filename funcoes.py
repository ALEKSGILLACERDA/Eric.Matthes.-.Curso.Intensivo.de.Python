def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name 
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
