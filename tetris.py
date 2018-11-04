import random

end = ""

while end != 'N':

    pieces = ['Line-Block', 'L-Block', 'Z-Block', 'Square Block', 'Reverse Z-Block', 'T-Block']

    bag = len(pieces)

    while bag > 1:
        selected = (random.choice(pieces))
        print(selected)
        pieces.remove(selected)
        bag = bag - 1

    end = input('Get new set of pieces?: ')

print('Exiting...')
