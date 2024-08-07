import calendar

def paivia_kuukaudessa(kuukausi, vuosi):
    if kuukausi in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif kuukausi in [4, 6, 9, 11]:
        return 30
    elif kuukausi == 2:
        if calendar.isleap(vuosi):
            return 29
        else:
            return 28
    else:
        return 0

def kuukauden_nimi(kuukausi):
    """Palauttaa kuukauden numero 1...12 nimen."""
    nimet = ['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 
             'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu']
    return nimet[kuukausi - 1] + 'kuu'

for k in range(1, 12+1):
    print(kuukauden_nimi(k), paivia_kuukaudessa(k, 2024))
