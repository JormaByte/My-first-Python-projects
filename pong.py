import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong by Jorma")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)    #stops window from updating

#Score
score_a=0
score_b=0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)   #max-speed of animation 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)   #max-speed of animation 
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#The ball
ball=turtle.Turtle()
ball.speed(0)   #max-speed of animation 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.06
ball.dy=-0.06


#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0   Player 2: 0",align="center",font=("Courier",24,"normal"))


#Function
def paddle_a_up():
    y=paddle_a.ycor()  #Returns the y-coordinate
    y+=20
    paddle_a.sety(y)


def paddle_a_down():
    y=paddle_a.ycor()  #Returns the y-coordinate
    y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()  #Returns the y-coordinate
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y=paddle_b.ycor()  #Returns the y-coordinate
    y-=20
    paddle_b.sety(y)



#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") #Calls the function when the key is pressed
wn.onkeypress(paddle_a_down,"s") 
wn.onkeypress(paddle_b_up,"Up") 
wn.onkeypress(paddle_b_down,"Down") 



#main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1     #Reverses the direction
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1 
        score_a+=1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player 1: {score_a}   Player 2: {score_b}",align="center",font=("Courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player 1: {score_a}   Player 2: {score_b}",align="center",font=("Courier",24,"normal"))


    #Paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1