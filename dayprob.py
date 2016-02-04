#!/usr/bin/env python
"""
    <name>
        dayprob.py

    <description>
        Provides a somewhat inaccurate measurement of the probability of finding a random
        video on youtube by just pulling the trigger with a random string as a video id.

    <usage>
        ./dayprob.py [days]

    <Notes>
        As you'll notice, the probability of hitting something is really low.
"""
from math import pow
import sys

# Approximate number of youtube videos
success = pow(10, 9)

# Approximate possible combinations (the last two bits of the youtube video id don't count)
keyspace = pow(2,63)

# We perform a dumb geometric CDF to see what's the probability. This assumes a video a second 
prob = success/keyspace
q = 1 - prob

trials_per_second = 1
days = int(sys.argv[1])
trials = float(days * 3600 * 24)
total_prob = 1 - pow(q, trials)

print ("[{}] {:.5f}".format(trials, total_prob))
