def alennettu_hinta(hinta, alennusprosentti):
    alennus = hinta * alennusprosentti / 100.0
    return hinta - alennus

hinta = float(input('Anna alkuperäinen hinta euroina: '))

ale10 = alennettu_hinta(hinta, 10)
print(f'Alennus 10 % = {ale10}')

ale20 = alennettu_hinta(hinta, 20)
print(f'Alennus 20 % = {ale20}')

ale50 = alennettu_hinta(hinta, 50)
print(f'Alennus 50 % = {ale50}')
