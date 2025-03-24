import turtle
import random

screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')
t=turtle.Turtle()

t.penup()
t.goto(0,200)
t.pendown()
t.pencolor('white')
t.write('Background color',font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor('tan')
t.write('1. Tan',font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor('Aquamarine')
t.write('3. Aquamarine',font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor('Azure')
t.write('2. Azure',font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor('Darkkhaki')
t.write('4. DarkKhaki',font=("Arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor('white')
t.write('Choose a color',font=("Arial",30,"normal"),align="center")

choice=int(input('Choose a color: '))
if choice==1:
    screen.bgcolor('tan')
elif choice==2:
    screen.bgcolor('azure')
elif choice==3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('darkkhaki')

t.clear()

name=input('Enter your name: ')

operation=random.randint(1,4)
if operation==1:
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    sum1=num1+num2
    symbol="+"
elif operation==2:
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    sum1=num1-num2
    symbol = "-"
elif operation==3:
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    sum1=num1*num2
    symbol = "*"
elif operation==4:
    symbol = "/"
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    sign=random.randint(1,2)
    if sign==2:
        num2=-1*num2
        sum1=num1/num2

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor('red')
t.write(num1,font=("Arial",20,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor('green')
t.write(symbol,font=("Arial",20,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('blue')
t.write(num2,font=("Arial",20,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor('green')
t.write('=',font=("Arial",20,"normal"),align="center")



t.penup()
t.goto(0,150)
t.pendown()
t.pencolor('black')
t.write(name,font=("Arial",20,"normal"),align="center")

answer=float(input('What is the answer: '))


t.penup()
t.goto(200,0)
t.pendown()
t.pencolor('purple')
t.write(sum1,font=("Arial",20,"normal"),align="center")



t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor('black')
t.write('Your answer: '+str(answer),font=("Arial",20,"normal"),align="center")

if answer == sum1:
    screen.bgcolor('dodgerblue')
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.pencolor('black')
    t.write('Good job!', font=("Arial", 20, "normal"), align="center")
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.pencolor('black')
    t.write('Wrong!', font=("Arial", 20, "normal"), align="center")

turtle.done()