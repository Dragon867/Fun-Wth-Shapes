import turtle

# Function to draw a polygon
def draw_polygon(sides, length):
    angle = 360 / sides  # Calculate the angle between sides
    for _ in range(sides):
        turtle.forward(length)  # Move turtle forward
        turtle.left(angle)  # Turn the turtle left by the calculated angle

# Set up the screen
turtle.setup(500, 500)
turtle.bgcolor("white")
turtle.title("Polygon Drawer")

# Set up the turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.speed(5)  # Adjust speed (1 is slow, 10 is fast)

# Ask for user input to choose the polygon
sides = int(turtle.numinput("Polygon Sides", "Enter the number of sides: ", default=3, minval=3))
length = int(turtle.numinput("Side Length", "Enter the length of each side: ", default=100, minval=10))

# Draw the polygon
draw_polygon(sides, length)

# Finish drawing
turtle.done()