import random
import subprocess as sp
import time

low_guards = ["Middle boar's tooth", "Boar's tooth", "Middle iron door", 
"Open iron door", "Tail guard"]
middle_guards = ["Short guard", "Long guard", "Bicorn", "Crown guard"]
high_guards = ["Women's guard", "Window guard", "Women's guard on the left"]
steps = ["Accrehsehreh", "Dehccrehsehreh", "Mezzo volta", "Circle step", 
"Volta stabile", "Tutti volta"]

action_types = [low_guards, middle_guards, high_guards, steps]

# FIXME: MORE SENSIBLE ORDERS OF ACTIONS
# FIXME: BETTER BLEND OF ACTION SETS
# FIXME: INTRODUCE COMPLETELY RANDOM MODE (ANY ACTION AT ANY TIME)
print "Push Ctrl+C to exit."
while True:
    current_type = random.choice(action_types)
    for action in current_type:
        print action
        sp.call(['say', action])
        time.sleep(2)
