import random

def nopanheitto(sivuja=6, montako=1):
    luvut = []
    for n in range(montako):
        luku = random.randrange(0, sivuja) + 1
        luvut.append(luku)
    return {'luvut': tuple(luvut), 
            'summa': sum(luvut)}
