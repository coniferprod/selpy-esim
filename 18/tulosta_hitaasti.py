import time

def tulosta_hitaasti(teksti, viive=0.1):
    for merkki in teksti:
        print(merkki, end='', flush=True)
        time.sleep(viive)

tulosta_hitaasti('\nINCOMING MESSAGE\n\n', viive=0.2)
tulosta_hitaasti('FROM: MISSION COMMAND\n\n')
tulosta_hitaasti('SUBJECT: MISSION UPDATE\n\n')
tulosta_hitaasti('PROCEED TO RENDEZVOUS POINT. REPORT TO BASE.\n\n')
tulosta_hitaasti('MESSAGE ENDS\n\n', viive=0.2)
