from random import randint

pos_l1 = 0
pos_l2 = 0
while True:
    de = randint(1, 6)
    print('dé =', de)
    if de % 2 != 0:
        pos_l1 += 1
        print("Position Dubsy :", pos_l1)
    else:
        pos_l2 += 1
        print("Position Gipsy :", pos_l2)
    if pos_l1 == 4 or pos_l2 == 4:
        break

if pos_l1 == 4:
    print('Dubsy gagne.')
else:
    print('Gipsy gagne.')