vek = int(input("Kolik Ti je let? "))
if vek < 18:
    print("Jsi příliš mladý na vstup.")
else: 
    karta = input("Máš členskou kartu? (ano/ne)")
    if karta == "ano":
        print("Vítej v klubu!")
    else:
        print("Bez členské karty nemůžeš dovnitř.")
