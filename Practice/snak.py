import turtle
import random

# Constants
WIDTH = 800
HEIGHT = 600
FOOD_SIZE = 10
DELAY = 100
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
    global snake, snake_direction, food_pos, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"  # Initial direction
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    move_snake()

def move_snake():
    global snake_direction

    # Calculate next position for the head of the snake
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # Keep the snake the same length unless fed

        # Allow screen wrapping
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        # Clear previous snake stamps
        pen.clearstamps()

        # Draw the snake
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Refresh the screen
        screen.update()

        # Continue moving the snake
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(int(- WIDTH / 2 + FOOD_SIZE), int(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(int(- HEIGHT / 2 + FOOD_SIZE), int(HEIGHT / 2 - FOOD_SIZE))
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
    print("Direction:", snake_direction)

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
    print("Direction:", snake_direction)

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
    print("Direction:", snake_direction)

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"
    print("Direction:", snake_direction)

def mouse_click(x, y):
    global snake_direction
    if abs(x) > abs(y):
        if x > 0:
            if snake_direction != "left":
                snake_direction = "right"
        else:
            if snake_direction != "right":
                snake_direction = "left"
    else:
        if y > 0:
            if snake_direction != "down":
                snake_direction = "up"
        else:
            if snake_direction != "up":
                snake_direction = "down"
    print("Direction:", snake_direction)

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Pen setup
pen = turtle.Turtle("square")
pen.penup()
pen.pencolor("yellow")

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onclick(mouse_click)  # Bind mouse click event

# Start the game
reset()
turtle.done()
