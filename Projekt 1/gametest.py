import turtle
import tkinter
win = turtle.Screen()
win.title("test")
win.bgcolor("white")
win.setup(width=600, height=600)
win.tracer(0)

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("black")
pen1.penup()
pen1.hideturtle()
pen1.goto(-2, -2)
pen1.color("black")
pen1.write("test", align="center", font=("Helvetica Narrow", 68, "bold"))
while True:
    win.update()