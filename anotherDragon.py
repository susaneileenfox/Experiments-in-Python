

import turtle
import math
import time


def fraggy(goTurt, levels, size):
    if levels == 1:
        goTurt.forward(size)
    else:
        newSize = size / math.sqrt(2)
        goTurt.right(45)
        fraggy(goTurt, levels - 1, newSize)
        goTurt.up()
        goTurt.left(90)
        goTurt.forward(newSize)
        goTurt.left(180)
        goTurt.down()
        fraggy(goTurt, levels - 1, newSize)
        goTurt.up()
        goTurt.right(180)
        goTurt.forward(newSize)
        goTurt.right(45)
        

if __name__ == '__main__':
    s = turtle.Screen()
    t = turtle.Turtle()

    for i in [13]: #[1, 2, 3, 4, 7, 10]:
        t.reset()
        t.speed(0)
        t.up()
        t.backward(200)
        t.down()
        fraggy(t, i, 400)
        time.sleep(1.5)
    
    s.exitonclick()