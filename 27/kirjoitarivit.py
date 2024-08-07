f = open('rivit.txt', 'w')

while True:
    rivi = input('> ')
    if not rivi:
        break
    f.write(rivi + '\n')

f.close()
