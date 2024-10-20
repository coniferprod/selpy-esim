# Turun kaupunginosat (lähde: https://fi.wikipedia.org/wiki/Turun_kaupunginosat)

k_osat = [
    # Keskusta
    'I', 'II', 'III', 'IV (Martti)', 'V (Itäranta)',
    'VI', 'VII', 'VIII (Port Arthur)', 'IX (Länsiranta)',
    'Kupittaa', 'Kurjenmäki', 'Mäntymäki', 'Vähäheikkilä',
    'Korppoolaismäki', 'Ruissalo', 'Satama', 'Iso-Heikkilä',

    # Hirvensalo - Kakskerta
    'Pikisaari', 'Lauttaranta', 'Maanpää', 'Jänessaari', 'Särkilahti',
    'Illoinen', 'Oriniemi', 'Moikoinen', 'Kukola', 'Toijainen',
    'Kaistaniemi', 'Friskala', 'Haarla', 'Papinsaari', 'Satava',
    'Vepsä', 'Kakskerta',

    # Skanssi - Uittamo
    'Vasaramäki', 'Luolavuori', 'Puistomäki', 'Pihlajaniemi',
    'Peltola', 'Ilpoinen', 'Ispoinen', 'Uittamo', 'Skanssi',
    'Koivula', 'Katariina', 'Harittu',

    # Varissuo - Lauste
    'Varissuo', 'Pääskyvuori', 'Vaala', 'Lauste', 'Huhkola',

    # Nummi - Halinen
    'Oriketo', 'Räntämäki', 'Koroinen', 'Halinen', 'Nummi',
    'Kohmo', 'Kurala', 'Itäharju',

    # Runosmäki - Raunistula
    'Runosmäki', 'Kärsämäki', 'Kaerla', 'Kastu', 'Raunistula',

    # Länsikeskus
    'Mälikkälä', 'Teräsrautela', 'Ruohonpää', 'Pitkämäki',
    'Vätti', 'Kähäri', 'Pohjola',

    # Pansio - Jyrkkälä
    'Artukainen', 'Pahaniemi', 'Perno', 'Pansio',

    # Maaria - Paattinen
    'Paattinen', 'Yli-Maaria', 'Moisio', 'Lentokenttä',
    'Koskennummi', 'Jäkärlä', 'Paimala', 'Urusvuori',
    'Saramäki', 'Tasto', 'Metsämäki', 'Haaga'
]

print(f'Kaupunginosia yhteensä: {len(k_osat)}')

print('Kaupunginosat, joiden nimessä ei ole r-kirjainta:')
r_osat = []
for k in k_osat:
    k_pien = k.lower()
    if 'r' in k_pien:
        r_osat.append(k)
    else:
        print(k)

print(f'Kaupunginosia, joiden nimessä on r-kirjain: {len(r_osat)}')

osuus = int(len(r_osat) / len(k_osat) * 100)
print(f'Näiden osuus kaikista kaupunginosista: {osuus} %')
