import calendar

def paivia_kuukaudessa(kuukausi, vuosi):
    """
    Palauttaa kuukauden päivien lukumäärän annettuna vuonna.
    Parametrissa `kuukausi` on kuukauden numero välillä 1...12,
    ja parametrissa `vuosi` on vuosiluku (ei tarkisteta).
    """
    paivat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    tulos = paivat[kuukausi - 1]  # indeksit alkavat nollasta!
    if kuukausi == 2:
        if calendar.isleap(v):
            tulos += 1
    return tulos

def kuukauden_nimi(kuukausi):
    """Palauttaa kuukauden numero 1...12 nimen."""
    nimet = ['tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä', 
             'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu']
    return nimet[kuukausi - 1] + 'kuu'

k = int(input('Anna kuukauden numero (1-12): '))
v = int(input('Anna vuosi: '))

p = paivia_kuukaudessa(k, v)
nimi = kuukauden_nimi(k)
print(f'Vuonna {v} {nimi}ssa on {p} päivää.')
