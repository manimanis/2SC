from random import randint
from turtle import *
age = int(input('Votre age ? '))
nom = input('Votre nom ? ')
print('Bienvenue', nom, ', quelle chance de programmer à', age, 'ans')
y = -300
for j in range(20):
    penup()
    setpos(-300, y)
    pendown()
    y += 30
    for i in range(20):
        x = randint(0, 1)
        if x == 0:
            print('Un carré vert')
            color('green', 'green')
            begin_fill()
            for i in range(4):
                forward(20)
                left(90)
            end_fill()
        else:
            print('Un triangle rouge')
            color('red', 'red')
            begin_fill()
            for i in range(3):
                forward(20)
                left(120)
            end_fill()
        penup()
        forward(30)
        pendown()
    
    
mainloop()