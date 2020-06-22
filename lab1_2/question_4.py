# draw square
def draw_square(side_length):
    for counter in range(4):
        fd(side_length)
        lt(90)

penup()
setpos(-225, 0)
pendown()
pensize(2)
pencolor("DarkOliveGreen4")
draw_triangle(50)


# draw triangle
def draw_triangle(side_length):



penup()
setpos(-150, 0)
pendown()
pensize(2)
pencolor("blue")
draw_square(70)

exitonclick()

