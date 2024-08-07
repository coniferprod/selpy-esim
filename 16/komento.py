while True:
    rivi = input('> ')

    komento = rivi.strip()
    if not komento:
        continue
    if komento == 'lopeta':
        break

    print(f'Komentosi oli: "{komento}"')
    print()

print('Kiitos pelistä! Nähdään taas!\n')
