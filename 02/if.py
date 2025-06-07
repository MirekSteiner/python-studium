strana = float(input("Zadej stranu čtverce v centimetrech: "))
Kladne_cislo = strana > 0
if Kladne_cislo:
    print("*" * 80)
    print("Obvod čtverce se stranou", strana, "je", 4 * strana, "cm")
    print("Obsah čtverce se stranou", strana, "je", strana ** 2, "cm2")
else:
   print("*" * 80)
   print("Strana musí být kladné číslo")
print("*" * 80)
print("Děkuji za použití geometrické kalkulačky")
print("*" * 80)
print("*" * 80)

