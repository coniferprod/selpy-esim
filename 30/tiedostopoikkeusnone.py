tiedosto = None
try:
    tiedosto = open('olematon.txt')
except FileNotFoundError:
    print('Tiedostoa ei löydy.')
else:
    try:
        lukemat = [float(r.strip()) for r in tiedosto.readlines()]
    except IOError as e:
        print(f'Virhe luettaessa tiedostosta: "{e}"')
    except ValueError as e:
        print(f'Virhe muunnettaessa tietoalkioita: "{e}"')
    else:
        alin = min(lukemat)
        ylin = max(lukemat)
        keskiarvo = round(sum(lukemat) / len(lukemat), 1)
        print(f'alin={alin} ylin={ylin} ka={keskiarvo}')
finally:
    if tiedosto is not None:
        tiedosto.close()
