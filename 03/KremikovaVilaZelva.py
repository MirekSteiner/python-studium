import turtle
import random

# Nastavení okna
turtle.bgcolor("midnight blue")

# Vytvoření želvy (štětec Víly!)
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Barvy křemíkové víly ✨
colors = ["violet", "deepskyblue", "magenta", "lightcyan", "plum", "gold", "orchid"]

# Kouzelné křídla Víly 🧚‍♀️
for i in range(60):
    t.color(random.choice(colors))
    t.forward(i * 5)
    t.left(59)
    t.circle(30)

# Dokončení
t.hideturtle()  # Víla zmizí v kouzelném třpytu ✨
turtle.done()
