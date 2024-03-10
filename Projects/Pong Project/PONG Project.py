import turtle as t
import os


a_score = 0
b_score = 0
#########Screen##########
umr = t.Screen()
umr.title("LEVEL 1")
umr.bgcolor('yellow')
umr.setup(width=800,height=600)
umr.tracer(0)

#############Left Box###################

leftbox = t.Turtle()
leftbox.speed(3)
leftbox.shape('square')
leftbox.color('green')
leftbox.shapesize(stretch_wid=5,stretch_len=1)
leftbox.penup()
leftbox.goto(-350,0)

######################Right Box###############

rightbox = t.Turtle()
rightbox.speed(3)
rightbox.shape('square')
rightbox.shapesize(stretch_wid=5,stretch_len=1)
rightbox.color('green')
rightbox.penup()
rightbox.goto(350,0)

#333333333333333333333#POng Ball############

ball = t.Turtle()
ball.speed(3)
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0,0)
ball_dx = 0.25   ###############Speed for ball movement.
ball_dy = 0.25

#$$$$$$$$$$$$$$$$$$$$$Updating Score

pen = t.Turtle()
pen.speed(3)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 \t\t Player B: 0 ",align="center",font=('Arial',24,"normal"))


# Moving the left Paddle box

def leftboxup():
    y = leftbox.ycor()
    y = y + 25
    leftbox.sety(y)

# Moving the left paddle box down

def leftboxdown():
    y = leftbox.ycor()
    y = y - 25
    leftbox.sety(y)

# Moving the right box paddle up

def rightboxup():
    y = rightbox.ycor()
    y = y + 25
    rightbox.sety(y)

# Moving right paddle box down

def rightboxdown():
    y = rightbox.ycor()
    y = y - 25
    rightbox.sety(y)


# Keyboard

umr.listen()
umr.onkeypress(leftboxup,"w")
umr.onkeypress(leftboxdown,"s")
umr.onkeypress(rightboxup,"Up")
umr.onkeypress(rightboxdown,"Down")



    


# Main Game Loop

while True:
    umr.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   # Right top paddle Border
        #ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Left top paddle Border
        #ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        a_score+= 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {} ".format(a_score,b_score),align="center",font=('Arial',24,"normal"))
        #os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        b_score+= 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {} ".format(a_score,b_score),align="center",font=('Arial',24,"normal"))
        #os.system("afplay wallhit.wav&")


    # Handling the collisions with paddles.

    if(ball.xcor() > 330) and (ball.xcor() < 360) and (ball.ycor() < rightbox.ycor() + 50 and ball.ycor() > rightbox.ycor() - 50):
        ball.setx(330)
        ball_dx = ball_dx * -1
       

    if(ball.xcor() < -330) and (ball.xcor() > -360) and (ball.ycor() < leftbox.ycor() + 50 and ball.ycor() > leftbox.ycor() - 50):
        ball.setx(-330)
        ball_dx = ball_dx * -1
       

    if a_score == 5:
        umr.clearscreen()
        umr.bgcolor("orange")
        pen.goto(0,0)
        pen.write("Player A wins", align="center", font=("Courier", 50, "normal"))
        break

    elif b_score== 5:
        umr.clearscreen()
        umr.bgcolor("green")
        pen.goto(0,0)
        pen.write("Player B wins", align="center", font=("Courier", 50, "normal"))
        break
    


#umr.clearscreen()
#umr.exitonclick()
#umr.reset()
#################################################################################################

a_score = 0
b_score = 0
#########Screen##########
umr = t.Screen()
umr.title("LEVEL 2")
umr.bgcolor('grey')
umr.setup(width=800,height=600)
umr.tracer(0)

#############Left Box###################

leftbox = t.Turtle()
leftbox.speed(3)
leftbox.shape('square')
leftbox.color('green')
leftbox.shapesize(stretch_wid=5,stretch_len=1)
leftbox.penup()
leftbox.goto(-350,0)

######################Right Box###############

rightbox = t.Turtle()
rightbox.speed(3)
rightbox.shape('square')
rightbox.shapesize(stretch_wid=5,stretch_len=1)
rightbox.color('green')
rightbox.penup()
rightbox.goto(350,0)

#333333333333333333333#POng Ball############

ball = t.Turtle()
ball.speed(3)
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0,0)
ball_dx = 0.6   ###############Speed for ball movement.
ball_dy = 0.6

#$$$$$$$$$$$$$$$$$$$$$Updating Score

pen = t.Turtle()
pen.speed(3)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 \t\t Player B: 0 ",align="center",font=('Arial',24,"normal"))


# Moving the left Paddle box

def leftboxup():
    y = leftbox.ycor()
    y = y + 25
    leftbox.sety(y)

# Moving the left paddle box down

def leftboxdown():
    y = leftbox.ycor()
    y = y - 25
    leftbox.sety(y)

# Moving the right box paddle up

def rightboxup():
    y = rightbox.ycor()
    y = y + 25
    rightbox.sety(y)

# Moving right paddle box down

def rightboxdown():
    y = rightbox.ycor()
    y = y - 25
    rightbox.sety(y)


# Keyboard

umr.listen()
umr.onkeypress(leftboxup,"w")
umr.onkeypress(leftboxdown,"s")
umr.onkeypress(rightboxup,"Up")
umr.onkeypress(rightboxdown,"Down")






# Main Game Loop

while True:
    umr.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   # Right top paddle Border
        #ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Left top paddle Border
        #ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        a_score+= 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {} ".format(a_score,b_score),align="center",font=('Arial',24,"normal"))
        #os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        b_score+= 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {} ".format(a_score,b_score),align="center",font=('Arial',24,"normal"))
        #os.system("afplay wallhit.wav&")


    # Handling the collisions with paddles.

    if(ball.xcor() > 330) and (ball.xcor() < 360) and (ball.ycor() < rightbox.ycor() + 50 and ball.ycor() > rightbox.ycor() - 50):
        ball.setx(330)
        ball_dx = ball_dx * -1
       

    if(ball.xcor() < -330) and (ball.xcor() > -360) and (ball.ycor() < leftbox.ycor() + 50 and ball.ycor() > leftbox.ycor() - 50):
        ball.setx(-330)
        ball_dx = ball_dx * -1
       

    if a_score == 10:
        umr.clearscreen()
        umr.bgcolor("orange")
        pen.goto(0,0)
        pen.write("Player A wins", align="center", font=("Courier", 50, "normal"))
        break

    elif b_score== 10:
        umr.clearscreen()
        umr.bgcolor("green")
        pen.goto(0,0)
        pen.write("Player B wins", align="center", font=("Courier", 50, "normal"))
        break
umr.exitonclick()
        



        



