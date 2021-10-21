"""
Gunnar Bachmann
9/25/2019
songs.py

Reads lyrics of a song from a text file and uses the turtle package to
draw a picture of a song with a colorful square for each letter. The shape of
text (length of each line) shall be preserved.
"""
import turtle as t


def init():
    """
    Initialize function to bring the turtle to the correct start position.
    :return:
    """
    t.up()
    t.goto(-300,300)
    t.down()


def square(color):
    """
    Draws a square and fills it with a color.

    pre-conditions: pendown facing east

    :param color: color of the square being drawn which is passed in.
    :return:
    """
    t.fillcolor(color)
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.end_fill()


def paint_line(st):
    """
    For in loop which decides the color based on the ASCII value, then calls
    square(color) to pass the color into the square function. Then move forward
    10 units to draw the next square.

    :param st: represents line from text file.
    :return:
    """
    for ch in st:
        if ord(ch) < 70:
            color = "red"
        elif 70 <= ord(ch) < 100:
            color = "blue"
        elif 100 <= ord(ch) < 110:
            color = "yellow"
        elif 110 <= ord(ch) < 122:
            color = "green"
        else:
            color = "purple"
        square(color)
        t.forward(10)


def picture(filename):
    """
    Opens the file inputted by user and stores it.
    Then a for in loop calls paint_line(line) and then moves the turtle to the
    next line once the previous one is complete. When done, the program will jump out
    of the for in loop and close the file.

    :param filename: file inputted by user in main function
    :return:
    """
    file = open(filename)

    x = -300
    y = 300

    for line in file:
        paint_line(line)
        y -= 10
        t.up()
        t.goto(x, y)
        t.down()

    file.close()


def main():
    """
    Asks the user to input a filename and it gets stored in the variable "filename"
    Turtle speed is changed to 0, and turtle tracer called with (100,30)
    Then, init() is called, followed by picture(filename) which does all the work.
    Then turtle.done() is called in order for the user to keep the turtle canvas open / close it on their own.
    :return:
    """
    filename = input("Enter a filename: ")

    t.speed(0)
    t.tracer(100,30)

    init()
    picture(filename)
    t.done()


if __name__ == '__main__':
    main()