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
        
ok = False
while not ok:
    try:
        k_teksti = input('Anna kuukausi: ')
        k = int(k_teksti)
        v_teksti = input('Anna vuosi: ')
        v = int(v_teksti)
    except ValueError as e:
        print(f'Virhe: {e}')
        continue
    else:
        try:
            lkm = paivia_kuukaudessa(k, v)
        except ValueError as e:
            print(f'Virhe: {e}')
        else:
            ok = True
            print(lkm)
