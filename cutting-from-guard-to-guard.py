# Drill focusing on performing cuts while moving between
# guards.

import random
import time
import subprocess as sp

from collections import namedtuple

import pandas as pd

# N.B: Commented-out guards are not normally the endpoint of any cuts
Guard = namedtuple('Guard', ['name', 'height', 'direction'])
guards = [
        #Guard("Tail guard", "low", "back"),
        Guard("Open Iron Door", "low", "right"),
        Guard("Middle Iron Door", "low", "middle"),
        Guard("Boar's Tooth", "low", "middle"),
        #Guard("Middle Boar's Tooth", "low", "middle"),
        Guard("Short guard", "middle", "up"),
        #Guard("Bicorn", "middle", "middle"),
        #Guard("Crown guard", "middle", "up"),
        Guard("Long guard", "middle", "middle"),
        Guard("Posta falcone", "high", "up"),
        Guard("Women's guard", "high", "back"),
        Guard("Women's guard on the left", "high", "back"),
        #Guard("Window guard", "high", "left")
        ]


def say(instruction, wait_time=3):
    sp.call(['say', instruction])
    time.sleep(wait_time)


def deliver(instruction):
    print instruction
    say(instruction)


def mezzana(destination):
    instruction = 'Mezzana to %s.' % destination
    deliver(instruction)


def fendente(destination, direction=''):
    instruction = "Fendenteh %s to %s." % (direction, destination)
    deliver(instruction)


def sottani(destination):
    instruction = "Sottani to %s." % destination
    deliver(instruction)

def switch_guard(destination):
    instruction = "Switch to %s." % destination
    deliver(instruction)

current_guard = random.choice(guards)
switch_guard(current_guard.name)
while True:
    proposed_guard = random.choice(guards)
    if proposed_guard == current_guard:
        # Don't repeat guards
        continue

    # Starting from a high guard
    if current_guard.height == 'high':
        if proposed_guard.height == 'low':
            if proposed_guard.direction == 'right':
                fendente(proposed_guard.name, 'sinestra')
            else:
                fendente(proposed_guard.name)
        elif proposed_guard.height == 'middle':
            if proposed_guard.direction == 'up':
                switch_guard(proposed_guard.name)
            else:
                mezzana(proposed_guard.name)
        else:
            switch_guard(proposed_guard.name)

    # Starting from a middle guard
    elif current_guard.height == 'middle':
        switch_guard(proposed_guard.name)

    # Starting form a low guard
    elif current_guard.height == 'low':
        if proposed_guard.height == 'low':
            switch_guard(proposed_guard.name)
        elif proposed_guard.height == 'middle':
            mezzana(proposed_guard.name)
        else:
            sottani(proposed_guard.name)

    # This should never happen
    else:
        raise RuntimeError("This is impossible!")

    current_guard = proposed_guard
