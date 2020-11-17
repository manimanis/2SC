from random import randint

pos_lievre = 0
pos_tortue = 0
while True:
    de = randint(1, 6)
    print('dé =', de)
    if de != 6:
        pos_tortue += 1
        print('La tortue avance à la position :', pos_tortue)
    else:
        pos_lievre = 6
        print('Le lièvre avance à la position :', pos_lievre)
    if pos_lievre == 6 or pos_tortue == 6:
        break

if pos_lievre == 6:
    print('Le lièvre gagne.')
else:
    print('La tortue gagne.')