vek = int(input ("Kolik Ti je let? "))
prijem = float(input("Jaký máš čistý měsíční příjem? (v EUR)"))
prace = input("Máš stálý pracovní poměr? (ano/ne)")
if 18 < vek < 65:
    if prijem > 1500:
        if prace == "ano":
            print("Půjčka schválena")
        else:
            print("Půjčka zamítnuta")
    else:
        print("Půjčka zamítnuta")
else:
    print("Půjčka zamítnuta")