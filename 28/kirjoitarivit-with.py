rivit = []
while True:
    rivi = input('> ')
    if not rivi:
        break
    rivit.append(rivi)

rivit = [rivi + '\n' for rivi in rivit]

with open('rivit.txt', 'a') as f:    
    f.writelines(rivit)
