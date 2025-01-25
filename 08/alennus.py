hinta = float(input('Anna tuotteen hinta: '))
alennusprosentti = int(input('Anna alennusprosentti: '))
lopullinen_hinta = hinta - (hinta * alennusprosentti / 100.0)
print(f'Tuotteen hinta: {hinta}')
print(f'Alennus: {alennusprosentti} %')
print(f'Lopullinen hinta: {lopullinen_hinta}')
 