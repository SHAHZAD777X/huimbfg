import turtle
window= turtle.Screen()
window.bgcolor("Pink")
window.title("Turtle")
p=turtle.Turtle()
s=0
while True:
    for i in range(20):
        p.forward(s+1)
        p.left(36)
        s=s-5
    s=s+1