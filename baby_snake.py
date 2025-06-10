
import tkinter as tk
import random
import time

# Constants
WINDOW_SIZE = 400
STEP = 20
DELAY = 0.2

# Direction mappings
DIRECTIONS = {
    'Right': (STEP, 0),
    'Left': (-STEP, 0),
    'Up': (0, -STEP),
    'Down': (0, STEP)
}

# Initial direction
direction = 'Right'

# Handle key press to change direction
def on_key_press(event):
    global direction
    if event.keysym in DIRECTIONS:
        direction = event.keysym

def move_goal():
    new_x = random.randint(0, (WINDOW_SIZE - STEP) // STEP) * STEP
    new_y = random.randint(0, (WINDOW_SIZE - STEP) // STEP) * STEP
    canvas.moveto(goal, new_x, new_y)

def detect_collision():
    player_x = canvas.coords(player)[0]
    player_y = canvas.coords(player)[1]

    # Out of bounds
    if player_x < 0 or player_x >= WINDOW_SIZE or player_y < 0 or player_y >= WINDOW_SIZE:
        print("Game Over!")
        return True

    goal_x = canvas.coords(goal)[0]
    goal_y = canvas.coords(goal)[1]

    # Collision with goal
    if player_x == goal_x and player_y == goal_y:
        move_goal()

    return False

def main_loop():
    dx, dy = DIRECTIONS[direction]
    canvas.move(player, dx, dy)

    if detect_collision():
        return  # End game on collision

    root.after(int(DELAY * 1000), main_loop)

# Set up window and canvas
root = tk.Tk()
root.title("Baby Snake")
canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="white")
canvas.pack()

# Create player and goal
player = canvas.create_rectangle(0, 0, STEP, STEP, fill="blue")
goal_x = 360
goal_y = 360
goal = canvas.create_rectangle(goal_x, goal_y, goal_x + STEP, goal_y + STEP, fill="red")

# Bind keys
root.bind("<KeyPress>", on_key_press)

# Start animation
root.after(100, main_loop)
root.mainloop()
