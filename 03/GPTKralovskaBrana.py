#Zde definuji textové hlášky
OK1 = "SUPER! Podařilo se Ti otevřít" 
OK2 = "K R Á L O V S K O U   P O K L A D N I C I ! "
import time

def otevri_pokladnici():
    for i in range(3):
        print(3-i, end=" ", flush=True)
        time.sleep(1)
    print(OK1)
    print(OK2)

vek = int(input("Zadej, prosím, svůj věk: "))
if vek < 0:
    print("Bohužel, záporný věk nemůžeš zadat, byl by to nesmysl.")
elif vek < 18:
    print("Je mi líto, ale pro otevření Královské brány musíš být plnoletý.")
    print("Ale NEVADÍ, ještě máš jednu možnost, jak otevřít Královskou pokladnici!")
    jmeno = str(input("Pokud napíšeš své jméno - a budeš vyhodnocen jako Král, pak se Ti pokladnice sama otevře! "))
    if len(jmeno) > 5: #Jméno očekávám "Miroslav", ale kontrola je pouze na 5 znaků.
        otevri_pokladnici()
    else:
        print("Bohužel, Tvé jméno nemělo dostatečnou moc otevřít Královskou pokladnici.")
else:
    print("SUPER! První podmínka pro otevření brány je splněna, můžeme pokročit dále.")
    pokladnice = int(input("Kolik zlaťáků má Král v pokladnici? "))
    if pokladnice < 100:
        print("To je mi líto, v pokladnici je více zlaťáků, než jsi zadal.") 
        print("Zkus to příště znovu, určitě se Ti povede lépe!")
        print("Ale NEVADÍ, ještě máš jednu možnost, jak otevřít Královskou pokladnici!")
        jmeno = str(input("Pokud napíšeš své jméno - a budeš vyhodnocen jako Král, pak se Ti pokladnice sama otevře! "))
        if len(jmeno) > 5: #Jméno očekávám "Miroslav", ale kontrola je pouze na 5 znaků.
            otevri_pokladnici()
        else:
            print("Bohužel, Tvé jméno nemělo dostatečnou moc otevřít Královskou pokladnici.")
    else:
        otevri_pokladnici()

# Nejsem si jistý jak použít BOOL

from turtle import *
a = 80

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

exitonclick()