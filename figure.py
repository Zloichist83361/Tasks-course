import turtle

def sq(b):
    for i in range(4):
        a.color(colors[i % 4])
        a.forward(b)
        a.left(90)

colors = ['red', 'brown', 'green', 'blue']

a = turtle.Turtle()
a.speed(100)

dlina = 30
for i in range(60):
    a.circle(60)
    sq(dlina)
    a.right(10)
    dlina = dlina + 4
