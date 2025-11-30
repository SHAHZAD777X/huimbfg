import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(600, 600)
poly=turtle.Turtle()

side=9
len=100
a=360.0/side

for i in range(side):
    poly.forward(len)
    poly.right(a)


turtle.done()