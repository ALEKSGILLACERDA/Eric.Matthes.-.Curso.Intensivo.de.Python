pet_1 = {'animal':'cachorro', 'idade':4, 'barulho':'latido'}
pet_2 = {'animal':'gato', 'idade':6, 'barulho':'miado'}
pet_3 = {'animal':'priquito', 'idade':6, 'barulho':'piu'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print('')
    for key, value in pet.items():
        if value == 'cachorro':
            print(key, value)