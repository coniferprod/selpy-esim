# Lue geenijakso käyttäjältä:
#dna = input('Anna geenijakso (ACGT): ')

dna = 'GATTACA'  # A=3  C=1  G=1  T=2

print(f'Geenijakso = {dna}')
print(f'Jakson pituus = {len(dna)}')

dna = dna.upper()  # muunna isoiksi kirjaimiksi

n_a = 0
n_c = 0
n_g = 0
n_t = 0

for n in dna:
    if n == 'A':
        n_a += 1
    elif n == 'C':
        n_c += 1
    elif n == 'G':
        n_g += 1
    elif n == 'T':
        n_t += 1
    else:
        print(f'Geenivirhe! {n} ei ole nukleotidi.')
        break

print(f'A = {n_a}  C = {n_c}  G = {n_g}  T = {n_t}')
