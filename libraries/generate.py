import random

coin = random.choice(['heads', 'tails'])

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)