import random
import subprocess as sp
import time

import pandas as pd
import numpy as np

class Opponent:
    def __init__(self, guard_trans_probs, dist_trans_probs):
        self.guard_trans_probs = guard_trans_probs
        self.dist_trans_probs = dist_trans_probs
        self.current_guard = guard_trans_probs.index[0]
        self.current_dist = dist_trans_probs.index[0]

    def take_next_stance(self):
        self.current_guard= np.random.choice(self.guard_trans_probs.index.values, 
                p=self.guard_trans_probs[self.current_guard])
        self.current_dist = np.random.choice(self.dist_trans_probs.index.values, 
                p=self.dist_trans_probs[self.current_dist])

    def say_current_stance(self):
        stance_str = 'In %s, %s.' % (self.current_guard, self.current_dist)
        print stance_str
        sp.call(['say', stance_str])

# Read the (possibly poorly scaled) transition probabilities
affinity_mat_guards = pd.read_csv('guard-transition-probs.csv', index_col='Guard')
affinity_mat_dists = pd.read_csv('distance-transition-probs.csv', index_col='Distance')

# Re-scale them appropriately.
guard_trans_probs = affinity_mat_guards / affinity_mat_guards.sum()
dist_trans_probs = affinity_mat_dists / affinity_mat_dists.sum()

print "Push Ctrl+C to exit."
adversary = Opponent(guard_trans_probs, dist_trans_probs)
while True:
    adversary.take_next_stance()
    adversary.say_current_stance()
    time.sleep(5)
