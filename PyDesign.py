import turtle

window = turtle.Screen()
window.bgcolor('black')

may = turtle.Turtle()
may.shape('arrow')
may.speed(100) #Sets the turtle's speed
may.turtlesize(0.3) #Sets the turtle's size

colors = ['white','violet','indigo','blue','green','yellow','red',]

may.left(89.5)

def color(z):
    may.color(z)

def design(length):
    may.forward(length)
    may.right(91.2)

line_len=100
x=0

for a in range(305):
    y = colors[x]
    color(y)
    design(line_len/2)
    line_len+=2
    x+=1
    if x<7:
        continue
    else:
        x=0

turtle.exitonclick()
















