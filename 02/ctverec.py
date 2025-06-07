# Tady mám nějakou poznámku. xixixi
print("Tento program počítá obvod a obsah čtverce, následně pak obvod a obsah kruhu.")
strana = int(input("Zadej stranu čtverce a zároveň poloměr kruhu (v centimetrech): "))
print("Obvod čtverce se stranou", strana, "cm je ", strana * 4, "cm")
print("Obsah čtverce se stranou", strana, "cm je ", strana ** 2, "cm2")
print("Výpočet kruhu")
pi = 3.1415926
r = strana
print("Obvod kruhu o poloměru", r, "je ", 2 * pi * r, "cm")
print("Obsah kruhu o poloměru", r, "je ", pi * r ** 2, "cm2")
