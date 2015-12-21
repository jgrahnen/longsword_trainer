import random
import subprocess as sp
import time

import pandas as pd
import numpy as np

# FIXME: BETTER TRANSITION PROBS (SOME GUARDS NEVER APPEAR!)

# Read the (possibly poorly scaled) transition probabilities
affinity_mat = pd.read_csv('guard-transition-probs.csv', index_col='Guard')

# Re-scale them appropriately.
trans_probs = affinity_mat / affinity_mat.sum()

print trans_probs

print "Push Ctrl+C to exit."
next_action = np.random.choice(trans_probs.index)
while True:
    next_action = np.random.choice(trans_probs.index.values, p=trans_probs[next_action])
    print next_action
    sp.call(['say', next_action])
    time.sleep(2)
