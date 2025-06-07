stastna = input("Jsi šťastná? - Odpověz 'ano' nebo 'ne' ")
bohata = input("Jsi bohatá? - Odpověz 'ano' nebo 'ne' ")

if stastna == "ano":
    if bohata == "ano":
        print("Gratuluji")
    else:
        print("Zkus míň utrácet")
else:
    if bohata == "ano":
        print("Zkus se víc usmívat")
    else:
        print("To je mi líto")

