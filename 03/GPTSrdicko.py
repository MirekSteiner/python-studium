import turtle

# Nastavení okna
window = turtle.Screen()
window.bgcolor("white")
window.title(".")

# Nastavení želvy
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(3)

# Kreslení 
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Dokončení
pen.hideturtle()
window.mainloop()
