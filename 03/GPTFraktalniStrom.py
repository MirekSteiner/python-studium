import turtle

# Nastavení želvy
t = turtle.Turtle()
t.speed(0)  # maximální rychlost
t.left(90)  # ať roste vzhůru
t.color("forest green")

# Fraktální funkce
def strom(délka):
    if délka < 10:
        return
    t.forward(délka)
    t.left(30)
    strom(délka * 0.7)
    t.right(60)
    strom(délka * 0.7)
    t.left(30)
    t.backward(délka)

# Zavolání funkce
strom(100)

# Konec
turtle.done()
