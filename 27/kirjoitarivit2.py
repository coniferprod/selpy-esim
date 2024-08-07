rivit = []
while True:
    rivi = input('> ')
    if not rivi:
        break
    rivit.append(rivi)

rivit = [rivi + '\n' for rivi in rivit]

f = open('rivit.txt', 'w')
f.writelines(rivit)
f.close()
