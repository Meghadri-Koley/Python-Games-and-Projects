
import itertools
import random

faces = ['Spade', 'Club', 'Heart', 'Diamond']
deck = list(itertools.product(range(1, 14), faces))

random.shuffle(deck)
print(deck[0])
# itertools.
