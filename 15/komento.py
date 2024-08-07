print('\nOlet synkän metsän laidalla.')
print('Edessäsi on polku, joka vie syvemmälle metsään.')
print('Mitä haluat tehdä?\n')

komento = input('> ')
while komento != 'lopeta':
    print(f'Komentosi oli: "{komento}"')
    print()
    komento = input('> ')

print('Kiitos pelistä! Nähdään taas!\n')
