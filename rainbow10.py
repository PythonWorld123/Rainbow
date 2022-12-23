import turtle

myPen = turtle.Turtle()
scr=turtle.Screen()
scr.title("Rainbow Colors")
myPen.speed(500)

window = turtle.Screen()
window.bgcolor("sky blue")

rainbowColors = ["red","#FFA600","#FFFF00", "#62FF00", "#1E56FC", "#4800FF","#CC00FF","#69C5FF"]

size=450

myPen.penup()
myPen.goto(0,-560)

for color in rainbowColors:
  myPen.color(color)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(size)
  myPen.end_fill()
  size -= 10
