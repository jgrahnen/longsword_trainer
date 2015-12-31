import random
import subprocess as sp
import time

import pandas as pd
import numpy as np

# Read the (possibly poorly scaled) transition probabilities
affinity_mat = pd.read_csv('guard-transition-probs.csv', index_col='Guard')

# Re-scale them appropriately.
trans_probs = affinity_mat / affinity_mat.sum()

print "Transition probabilities between guards:"
print trans_probs

# Find an approximation to the stationary distribution
n = 100
stationary_dist = pd.Series(np.linalg.matrix_power(trans_probs.values, n)[:,0], index=trans_probs.index)

print "\n\nLong-run probability of being in each guard:"
print stationary_dist

print "Push Ctrl+C to exit."
next_action = np.random.choice(trans_probs.index)
while True:
    next_action = np.random.choice(trans_probs.index.values, p=trans_probs[next_action])
    print next_action
    sp.call(['say', next_action])
    time.sleep(2)
