import turtle as t
t.hideturtle()
t.penup()
t.goto(0,0)
t.pendown()
t.bgcolor('white')
t.speed(3)
t.pensize(3)

t.color('orange')
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(400)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.end_fill()
t.penup()
t.goto(-200, -100)
t.pendown()
t.color('green')
t.begin_fill()
t.right(90)
t.forward(100)
t.left(90)
t.forward(400)
t.left(90)
t.forward(100)
t.left(90)
t.forward(400)
t.end_fill()
t.penup()
t.goto(0, 0)
t.pendown()
t.color('blue')
t.circle(50)
i=1
while i<=24:
	t.penup()
	t.goto(0, -50)
	t.pendown()
	t.left(360/24)
	t.forward(50)
	i += 1
	
t.done()