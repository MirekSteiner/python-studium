vek = int(input ("Kolik Ti je let? "))
prijem = float(input("Jaký máš čistý měsíční příjem? (v EUR)"))
prace = input("Máš stálý pracovní poměr? (ano/ne)")
if 18 <= vek < 65:
    if prijem >= 1500:
        if prace == "ano":
            print("Půjčka schválena")
        else:
            print("Půjčka zamítnuta - musíš mít stálý pracovní poměr")
    elif prijem < 0:
        print("Půjčku nemůžeme spočítat - protože byl zaslaný neplatný příjem")
    else:
        print("Půjčka zamítnuta - nedostatečný příjem, minimální příjem musí být 1500 EUR (včetně)")
elif vek > 65:
    print("Půjčka zamítnuta - váš věk překročil mezní hodnotu pro schválení půjčky")
elif vek < 0:
    print("Půjčka zamítnuta - Zadali jste neplatný věk")
else:
    print("Půjčka zamítnuta - Pro schválení půjčky je vyžadována plnoletost")