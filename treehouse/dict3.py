dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory (dicts, string):
    list = []
    for dict in dicts:
        rString = string.format(**dict)
        list.append(rString)
    return(list)

string_factory(dicts,string)