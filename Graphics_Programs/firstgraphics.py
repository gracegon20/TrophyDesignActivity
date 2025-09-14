from graphics import *  

win = GraphWin("My Circle", 400, 400)

circle = Circle(Point(200, 200), Point(300, 300).getX() - 200)
circle.setFill("blue")
circle.draw(win)

rectangle = Rectangle(Point(150, 150), Point(250, 250))
rectangle.setFill("red")
rectangle.draw(win)

win.getMouse()  # Pause to view result

win.close()  # Close window when done