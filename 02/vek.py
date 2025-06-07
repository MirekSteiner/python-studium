vek = int(input("Kolik Ti je let? "))
if vek >= 150:
    print("A ze kterépak jsi planety?")
elif vek >= 18:
    print("Můžeme nabídnout víno, cider nebo vodku.")
elif vek >= 1:
    print("Můžeme nabídnout mléko, čaj nebo vodu.")
elif vek >= 0:
    print("Sunar už bohužel došel.")
else:
    print("Pro návštěvy z budoucnosti bohužel nemáme nic v nabídce.")
    