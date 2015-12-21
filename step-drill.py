import random
import subprocess as sp
import time

# FIXME: MORE SENSIBLE ORDER TO THE STEPS (NOT ALL TRANSITIONS ARE ACTUALLY
# SENSIBLE).
steps = ["Accrehsehreh", "Accrehsehreh left", "Accrehsehreh right", "Dehccrehsehreh", "Dehccrehsehreh left", "Dehccrehsehreh right", "Circle step", "Mezzo volta", "Volta stabile right", "Volta stabile left", "Tutti volta"]

print "Push Ctrl+C to exit."
while True:
    action = random.choice(steps)
    print action
    sp.call(['say', action])
    time.sleep(3)
