import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Drawing a Circle")

# Set up the turtle
artist = turtle.Turtle()
artist.shape("turtle")
artist.color("blue")

# Draw a circle with radius 100
artist.circle(100)

# Complete drawing
turtle.done()
