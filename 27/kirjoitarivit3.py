rivit = []
while True:
    rivi = input('> ')
    if not rivi:
        break
    rivit.append(rivi)

rivit = [rivi + '\n' for rivi in rivit]

f = open('rivit.txt', 'a')
f.writelines(rivit)
f.close()
