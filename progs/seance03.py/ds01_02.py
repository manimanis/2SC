nav = int(input("Numéro du client ? "))
pv = float(input("Prix de vente de l'article ? "))
cat = input("Catégorie de l'article (A,B,C) ? ")

if cat == "A":
    remise = 20
elif cat == "B":
    remise = 30
else:
    remise = 50

mr = pv * remise / 100
print(f"Remise de {remise}% = {mr:0.3f}DT")

mp = pv - mr
print(f"Montant à payer = {mp:0.3f}DT")

if nav <= 50:
    print("Le client n°", nav, "gagne un bon d'achat de 100DT")
else:
    print("Le client n°", nav, "ne gagne pas un bon d'achat de 100DT")