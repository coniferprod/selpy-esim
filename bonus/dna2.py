# Lue geenijakso käyttäjältä:
#dna = input('Anna geenijakso (ACGT): ')

dna = 'GATTACA'  # A=3  C=1  G=1  T=2
#dna = 'ACGTGTCGATXAGCT'  # virheellinen geenijakso

print(f'Geenijakso = {dna}')
print(f'Jakson pituus = {len(dna)}')

dna = dna.upper()  # muunna isoiksi kirjaimiksi

ok = True  # ensin oletetaan, että kaikki on hyvin
for n in dna:
    if n not in 'ACGT':
        print(f'Geenivirhe! {n} ei ole nukleotidi.')
        ok = False  # aseta lippumuuttuja
        break

if ok:
    n_a = dna.count('A')
    n_c = dna.count('C')
    n_g = dna.count('G')
    n_t = dna.count('T')

    print(f'A = {n_a}  C = {n_c}  G = {n_g}  T = {n_t}')
