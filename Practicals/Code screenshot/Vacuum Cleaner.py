import random
env={'A':random.choice([0,1]),'B':random.choice([0,1])}
loc='A'
def reflex(loc):
    if env[loc]: env[loc]=0; return "SUCK"
    else:
        loc2='B' if loc=='A' else 'A'
        return "MOVE-"+loc2
for _ in range(10):
    act=reflex(loc)
    print(loc,env,act)
    if act.startswith("MOVE"): loc=act.split('-')[1]
