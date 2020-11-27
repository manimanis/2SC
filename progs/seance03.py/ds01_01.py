nom1 = input("Nom du 1er pêcheur ? ")
nom2 = input("Nom du 2ème pêcheur ? ")

age1 = int(input(f"Age de {nom1} ? "))
age2 = int(input(f"Age de {nom2} ? "))

q1 = float(input(f"Quantité pêchée par {nom1} ? "))
q2 = float(input(f"Quantité pêchée par {nom2} ? "))

if q1 > q2:
    ng1 = nom1
    ng2 = nom2
elif q1 < q2:
    ng1 = nom2
    ng2 = nom1
else:
    if age1 > age2:
        ng1 = nom1
        ng2 = nom2
    else:
        ng1 = nom2
        ng2 = nom1

print(ng1, "gagne le titre du pêcheur de l'année et le poisson d'or")
print(ng2, "gagne le poisson d'argent")
