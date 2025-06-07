dotaz = input("Chceš počítat? (ano/ne) ")
if dotaz == "ne":
    print("Dobře, třeba příště.")
elif dotaz == "ano":
    Cislo1 = int(input("Zadej první číslo: "))
    Cislo2 = int(input("Zadej druhé číslo: "))
    Operace = input("Zadej operaci (+ nebo -): ")
    if Operace == "+":
        print("Tvůj výsledek je: ", Cislo1, " + ", Cislo2, " = ", Cislo1 + Cislo2)
    else:
        print("Tvůj výsledek je: ", Cislo1, " - ", Cislo2, " = ", Cislo1 - Cislo2)
else:
    print("Odpověď musí být pouze 'ano' nebo 'ne'")


