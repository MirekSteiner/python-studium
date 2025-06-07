import turtle

# Nastavení okna
window = turtle.Screen()
window.bgcolor("white")
window.title("Květinka")

# Nastavení želvy
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("magenta", "pink")
pen.speed(10)

# Funkce na okvětní lístek
def petal():
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)

# Kreslení květiny
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.begin_fill()
for _ in range(6):  # počet okvětních lístků
    petal()
    pen.left(60)
pen.end_fill()

# Stonek
pen.color("green")
pen.right(90)
pen.forward(300)

# Dokončení
pen.hideturtle()
window.mainloop()
