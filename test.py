from turtle import *
from functools import partial
import time
from random import *

row_card = 2
columns_card = 4
open_count = 0

def my_click(index,x,y):
    print(x, y, index)
    global open_count 
    if open_count < 2:
        frip_turtle(index)
        print("go flip")
                    
    else:
        check_complientse()
        print("go check")


def reverse_all():
    global open_count
    open_count = 0
    for i in list_turtle:
        if i.is_open and not i.is_block:
            i.is_open = False
            i.shape("stop.gif")

def check_win():
    count = 0
    for i in range(len(list_turtle)):
        if list_turtle[i].is_block:
            count += 1
            if count >= len(list_turtle):
                print("Поздравляем, вы победили!")
                break

def check_complientse():
    global open_count
    first_t = None
    for i in range(len(list_turtle)):
        
        if not list_turtle[i].is_block:
            if list_turtle[i].is_open and first_t == None:
                first_t = i 
            elif list_turtle[i].is_open:
                if list_turtle[i].name_shape == list_turtle[first_t].name_shape:
                    list_turtle[i].is_block = True
                    list_turtle[first_t].is_block = True
                    open_count = 0
                    check_win()  
                else:
                    reverse_all()
                    break

def frip_turtle(index):
    global open_count
    t = list_turtle[index]

    if not t.is_block:
        if t.is_open:
            t.is_open = False
            t.shape("stop.gif")
        else:
            open_count += 1
            t.is_open = True
            image = t.name_shape
            t.shape(image)


current_image = ""

scr = Screen()
scr.setup(800, 600)

image = "stop.gif"
scr.register_shape(image)

image_list = ["Star1.gif", "Square1.gif", "Triangle1.gif", "Heart1.gif"]
for i in image_list:
    scr.register_shape(i)

image_list = ["Star1.gif", "Square1.gif", "Triangle1.gif", "Heart1.gif"] * row_card
shuffle(image_list)

index = 0
list_turtle = []
y = 250
for i in range(row_card):
    x_cor_t = 300
    for j in range(columns_card):
        t = Turtle()
        t.shape("stop.gif")
      #  t.fillcolor('blue')
        t.penup()
        t.goto(x_cor_t,y)
        x_cor_t += -100
        t.onclick(partial(my_click, len(list_turtle)))
        t.is_open = False
        t.is_block = False
        t.name_shape = image_list[index]
        list_turtle.append(t)
        index +=1
    y -= 100

scr.mainloop()
