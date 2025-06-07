import turtle

# Nastavení okna
turtle.bgcolor("white")

# Vytvoření želvy
t = turtle.Turtle()
t.speed(0)  # nejvyšší rychlost
t.pensize(2)
t.color("blueviolet")  # královská barva!

# Královská spirálová květina
for i in range(100):
    t.forward(i * 4)
    t.left(59)

# Ukončení kreslení
turtle.done()
