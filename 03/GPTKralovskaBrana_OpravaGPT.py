# Importy
from turtle import *
import time

# Textové hlášky
OK1 = "SUPER! Podařilo se Ti otevřít" 
OK2 = "K R Á L O V S K O U   P O K L A D N I C I ! "

# Funkce pro odpočet
def odpočet():
    for i in range(3):
        print(3 - i, end=" ", flush=True)
        time.sleep(1)
    print()

# Funkce pro otevření brány
def otevri_pokladnici():
    odpočet()
    print(OK1)
    print(OK2)

# Hlavní funkce
def kralovska_brana():
    brana_otevrena = False

    vek = int(input("Zadej, prosím, svůj věk: "))
    if vek < 0:
        print("Bohužel, záporný věk nemůžeš zadat, byl by to nesmysl.")
    elif vek < 18:
        print("Je mi líto, ale pro otevření Královské brány musíš být plnoletý.")
        print("Ale NEVADÍ, ještě máš jednu možnost, jak otevřít Královskou pokladnici!")
        jmeno = input("Zadej své jméno: ")
        if len(jmeno) > 5 or jmeno.lower() == "miroslav":
            otevri_pokladnici()
            brana_otevrena = True
        else:
            print("Bohužel, Tvé jméno nemělo dostatečnou moc otevřít Královskou pokladnici.")
    else:
        print("SUPER! První podmínka pro otevření brány je splněna, můžeme pokročit dále.")
        pokladnice = float(input("Kolik zlaťáků má Král v pokladnici? "))
        if pokladnice >= 100 and vek >= 18:
            otevri_pokladnici()
            brana_otevrena = True
        else:
            print("To je mi líto, v pokladnici je méně zlaťáků, než je požadováno.")
            print("Ale NEVADÍ, ještě máš jednu možnost, jak otevřít Královskou pokladnici!")
            jmeno = input("Zadej své jméno: ")
            if len(jmeno) > 5 or jmeno.lower() == "miroslav":
                otevri_pokladnici()
                brana_otevrena = True
            else:
                print("Bohužel, Tvé jméno nemělo dostatečnou moc otevřít Královskou pokladnici.")

    print("Stav Královské brány:", brana_otevrena)

    # Pokud se brána otevřela → vykreslíme symbol brány
    if brana_otevrena:
        kresli_branu()

# Funkce pro kreslení brány pomocí Turtle
def kresli_branu():
    a = 80
    speed(5)
    pensize(3)
    color("brown")

    forward(1 * a)
    left(90)
    forward(4 * a)
    left(90)
    forward(4 * a)
    left(90)
    forward(4 * a)
    left(90)
    forward(1 * a)
    left(90)
    forward(3 * a)
    right(90)
    forward(2 * a)
    right(90)
    forward(3 * a)

    hideturtle()
    exitonclick()

# --- SPUŠTĚNÍ PROGRAMU ---
kralovska_brana()
