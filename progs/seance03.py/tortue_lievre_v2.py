from random import randint

pos_lievre = 0
pos_tortue = 0
while True:
    de = randint(1, 6)
    print('dé =', de)
    if de != 6:
        pas = (de + 1) // 2 
        pos_tortue += pas
        if pos_tortue > 8:
            pos_tortue = 8
        print("La tortue avance à la position :", pos_tortue)
    else:
        pos_lievre = pos_lievre + 4
        print("Le lièvre avance à la position :", pos_lievre)
    if pos_lievre == 8 or pos_tortue == 8:
        break

if pos_lievre == 8:
    print('Le lièvre gagne.')
else:
    print('La tortue gagne.')