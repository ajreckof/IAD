#!/usr/bin/env python
import turtle

# Olivier Georgeon, 2021.
# This code is used to teach Developmental AI.
#
# Inspired by Turtle Python tutorial:
#   * https://www.javatpoint.com/python-turtle-programming

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300


class TurtlePyEnacter:

    def __init__(self, step):
        """ Creating the Turtle window """
        turtle.bgcolor("gray")
        self.screen = turtle.getscreen()
        self.screen.setup(SCREEN_WIDTH + 60, SCREEN_HEIGHT + 60)

        pen = turtle.Turtle("classic")
        pen.speed(0)
        pen.pencolor("white")
        pen.hideturtle()
        pen.setpos(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
        pen.fillcolor("white")
        pen.begin_fill()
        for i in range(2):
            pen.fd(SCREEN_WIDTH)
            pen.rt(-90)
            pen.fd(SCREEN_HEIGHT)
            pen.rt(-90)
        pen.end_fill()

        self.turtle = turtle.Turtle("turtle")
        self.turtle.color("green")
        self.turtle.speed(1)
        self.step = step

    def outcome(self, action):
        """ Enacting an action and returning the outcome """
        for i in range(self.step):
            _outcome = 0
            if action == 0:
                # move forward
                self.turtle.speed(1)
                self.turtle.forward(5)
            elif action == 1:
                # rotate left
                self.turtle.speed(10)
                self.turtle.left(4)
                self.turtle.forward(2)
            elif action == 2:
                # rotate right
                self.turtle.speed(10)
                self.turtle.right(4)
                self.turtle.forward(2)

            # Bump on screen edge and return outcome 1
            (screen_x, screen_y) = self.screen.screensize()
            if self.turtle.xcor() < -SCREEN_WIDTH/2:
                self.turtle.goto(-SCREEN_WIDTH/2, self.turtle.ycor())
                _outcome = 1
            if self.turtle.xcor() > SCREEN_WIDTH/2:
                self.turtle.goto(SCREEN_WIDTH/2, self.turtle.ycor())
                _outcome = 1
            if self.turtle.ycor() < -SCREEN_HEIGHT/2:
                self.turtle.goto(self.turtle.xcor(), -SCREEN_HEIGHT/2)
                _outcome = 1
            if self.turtle.ycor() > SCREEN_HEIGHT/2:
                self.turtle.goto(self.turtle.xcor(), SCREEN_HEIGHT/2)
                _outcome = 1

            if _outcome == 0:
                self.turtle.color("green")
            else:
                self.turtle.color("red")

        return _outcome


if __name__ == '__main__':
    """ Main """
    x = TurtlePyEnacter()
    interaction_step = 0 # Prevents triggering a new interaction before the previous is finished

    def k1():
        global interaction_step
        if interaction_step == 0:
            interaction_step = 1
            print(x.outcome(0))
            interaction_step = 0

    def k2():
        global interaction_step
        if interaction_step == 0:
            interaction_step = 1
            print(x.outcome(1))
            interaction_step = 0

    def k3():
        global interaction_step
        if interaction_step == 0:
            interaction_step = 1
            print(x.outcome(2))
            interaction_step = 0

    x.screen.onkey(k1, "Up")  # Up arrow key: go forward
    x.screen.onkey(k2, "Left")  # Left arrow key: turn left
    x.screen.onkey(k3, "Right")  # Right arrow key: turn right

    x.screen.listen()
    x.screen.mainloop()
