import turtle

def doSierpinski(points, levels):
   """Creates a Sierpinski Triangle with input number of levels
   and input three points."""
   myWin = turtle.Screen()
   myTurtle = turtle.Turtle()
   myTurtle.speed(0)
   sierpinski(points, levels, myTurtle)
   myWin.clear()
   
   

def sierpinski(points, degree, myTurtle):
   """Takes in a set of 3 points, a number of repetitions (degree), and a
   turtle. Ask the turtle to draw a sierpinski triangle of a certain level
   between the input set of points. If the number of repetitions is one or above,
   the gasket is drawn by drawing three smaller ones, of lesser degree at the
   top, left, and right of the current triangle."""
   colormap = ['red', 'orange', 'yellow', 'green', 'blue', '#4B0082', 'violet']
   whichColor = degree % len(colormap)
   drawTriangle(points, colormap[whichColor], myTurtle)
   mid1 = getMid(points[0], points[1])
   mid2 = getMid(points[0], points[2])
   mid3 = getMid(points[1], points[2])
   if degree > 0:
      sierpinski([points[0], mid1, mid2], degree - 1, myTurtle)
      sierpinski([points[1], mid1, mid3], degree - 1, myTurtle)
      sierpinski([points[2], mid3, mid2], degree - 1, myTurtle)


def drawTriangle(points, color, myTurtle):
   """Takes in a list of three points that form a triangle, and a color,
   and a turtle object. It draws a filled triangle with a black outline
   for those three points."""
   myTurtle.fillcolor(color)
   myTurtle.up()
   myTurtle.goto(points[0][0],points[0][1])
   myTurtle.down()
   myTurtle.begin_fill()
   myTurtle.goto(points[1][0],points[1][1])
   myTurtle.goto(points[2][0],points[2][1])
   myTurtle.goto(points[0][0],points[0][1])
   myTurtle.end_fill()


def getMid(p1,p2):
   """Takes two lists/tuples that describe (x, y) coordinates, and 
   computes the midpoint of the line between the two points"""
   return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)



if __name__ == '__main__':
   points1 = [[-200,-100], [0,200], [200,-100]]
   doSierpinski(points1, 1)
   doSierpinski(points1, 3)
   doSierpinski(points1, 5)
   points2 = [[-300, -300], [100, 150], [350, 0]]
   doSierpinski(points2, 1)
   doSierpinski(points2, 2)
   doSierpinski(points2, 4)
   points3 = [[ -300, 0], [150, 150], [150, -150]]
   doSierpinski(points3, 1)
   doSierpinski(points3, 3)
   doSierpinski(points3, 6)
