#First EVERRRR actual 2d game that I've EVERRRR MADEEEE😆😆😆😆 and also the longest game I've made so far!!! # Project #10
import turtle, time, random

# Track game state
game_started = False #Tracks whether the player has started

# Set up the Screen
win = turtle.Screen()
win.title("🐍🐍🐍Watch For The Walls🐍🐍🐍")
win.bgcolor('dark gray')
win.setup(width=600, height=600)
win.tracer(0)

# The Snake's Head
snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.color('blue')
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = 'stop' #✔ Initial direction

#The FOOOOD
food = turtle.Turtle()
food.shape("circle")
food.color('red')
food.penup()
food.speed(0)
food.goto(0, 100)

#Snake's body
segments = []

#The Score
score = 0

#The Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

#Ready set GoOOOOOO😆
start_text = turtle.Turtle()
start_text.color("white")
start_text.hideturtle()
start_text.penup()
start_text.goto(0, 0)
start_text.write("Press an arrow key to start!", align="center", font=("Courier", 18, "normal"))

#Game Over message
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("White")
game_over_pen.penup()
game_over_pen.hideturtle()

#Game Over Function
def game_over():
    game_over_pen.goto(0,0)
    game_over_pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

#Directional input
def go_up():
    global game_started
    if snake_head.direction != 'down':
        snake_head.direction = 'up'
        if not game_started:
            start_text.clear()
            game_started = True
            start_game_loop()

def go_down():
    global game_started
    if snake_head.direction != 'up':
        snake_head.direction = 'down'
        if not game_started:
            start_text.clear()
            game_started = True
            start_game_loop()

def go_left():
    global game_started
    if snake_head.direction != 'right':
        snake_head.direction = 'left'
        if not game_started:
            start_text.clear()
            game_started = True
            start_game_loop()

def go_right():
    global game_started
    if snake_head.direction != 'left':
        snake_head.direction = 'right'
        if not game_started:
            start_text.clear()
            game_started= True
            start_game_loop()

#Snake movement logic
def move():
    if snake_head.direction == 'up':
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == 'down':
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == 'left':
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == 'right':
        x = snake_head.xcor()
        snake_head.setx(x + 20)

#Game loop that ties everthing together
def start_game_loop():
    global game_running, score
    game_running = True
    score = 0
    pen.clear()
    pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    while game_running:
        win.update()

        # Move body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # More segment code
        if len(segments) > 0:
            x = snake_head.xcor()
            y = snake_head.ycor()
            segments[0].goto(x, y)
    
        move()

        # Collision with Fooooddd
        if snake_head.distance(food) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            food.goto(x, y)

            #New segments of the Snake's body
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("light blue")
            new_segment.penup()
            segments.append(new_segment)

            #Adding to the score
            score += 10 
            pen.clear()
            pen.write(f"Score {score}", align="center", font=("Courier", 24, "normal"))

        # Wall Colision Code
        if (
            snake_head.xcor() > 290 or snake_head.xcor() < -290 or
            snake_head.ycor() > 290 or snake_head.ycor() < -290
        ):
            game_over()
            game_running = False

        # Body Collision Code
        for segment in segments:
            if segment.distance(snake_head) < 20:
                game_over()
                game_running = False
    
        time.sleep(0.1) # slows down the loop

#Restart game function
def restart_game():
    global game_running, segments, game_started

    # Reset snake
    snake_head.goto(0, 0)
    snake_head.direction = 'stop'

    # Hide and clear segments
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    # Reset Food and text
    food.goto(0, 100)
    game_over_pen.clear()

    # Show start text again
    game_started = False
    start_text.write("Press an arrow key to start!", align="center", font=("Courier", 18, "normal"))

# Keyboard bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")
win.onkey(restart_game, "r")

#  Game runs when user presses a key
turtle.done()