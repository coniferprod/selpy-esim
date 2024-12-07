"""Generates the lyrics to "The Twelve Days of Christmas."""

# Ordinals for the days (see also the num2words and inflect packages)
ordinals = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth'
}

gifts = [
    'a partridge in a pear tree',
    'two turtle doves',
    'three French hens',
    'four calling birds',
    'five gold rings',
    'six geese a-laying',
    'seven swans a-swimming',
    'eight maids a-milking',
    'nine ladies dancing',
    'ten lords a-leaping',
    'eleven pipers piping',
    'twelve drummers drumming'
]

def get_verse_rows(day):
    """Gets the rows of the verse for day number `day` (1 to 12)."""

    if not 1 <= day <= 12:
        raise ValueError('day must be 1...12')

    gifts_today = gifts[:day]
    rows = []
    rows.append(f'On the {ordinals[day]} day of Christmas my true love sent to me')

    last_index = len(gifts_today) - 1
    for index, item in enumerate(reversed(gifts_today)):
        gift = item.upper() if item.startswith('five') else item
        #print(f'day={day} index={index} gift={gift}')
        row = ''
        if day == 1:
            row += gift + '.'
        else:
            if index != last_index:
                row += gift + ','
            else:
                row += 'and ' + gift + '.'
        rows.append(row)

    rows.append('') # add empty row to separate the verses
    return rows

all_rows = []
for r in range(1, 13):
    all_rows.extend(get_verse_rows(r))

for row in all_rows:
    print(row)
