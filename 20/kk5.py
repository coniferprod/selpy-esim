import calendar

def paivia_kuukaudessa(kuukausi, vuosi):
    if not 1 <= kuukausi <= 12:
        raise ValueError('kuukauden numeron pitää olla 1...12')
     
    # Nyt kuukauden numero on varmasti halutulla välillä.
    
    if kuukausi in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif kuukausi in [4, 6, 9, 11]:
        return 30
    else:
        if calendar.isleap(vuosi):
            return 29
        else:
            return 28

print(paivia_kuukaudessa(2, 2024))
print(paivia_kuukaudessa(13, 2024))
