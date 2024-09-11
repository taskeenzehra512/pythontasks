import argparse
import math
import sys

# Function to move in 2D space
def move_in_2d_space(args):
    # Initialize position
    x, y = 0, 0

    # Apply movements
    y += round(args.up)
    y -= round(args.down)
    x -= round(args.left)
    x += round(args.right)

    # Print final position
    print(f"Final position: ({x}, {y})")

    # Calculate and print the distance from origin
    distance = round(math.sqrt(x**2 + y**2))
    print(f"Distance from origin: {distance}")

# Main loop to handle input and ask if the user wants to quit or continue
while True:
    # Initialize the parser inside the loop to take new input each time
    parser = argparse.ArgumentParser(description="Move in 2D space")
    
    # Add arguments for each direction
    parser.add_argument('--up', type=float, default=0, help='Move up by a number of units')
    parser.add_argument('--down', type=float, default=0, help='Move down by a number of units')
    parser.add_argument('--left', type=float, default=0, help='Move left by a number of units')
    parser.add_argument('--right', type=float, default=0, help='Move right by a number of units')

    # Try to parse the arguments
    try:
        args = parser.parse_args(input("Enter the arguments (e.g., --up 5 --left 2  ): ").split())
        move_in_2d_space(args)  # Call the function with parsed arguments
    except:
        parser.print_help()
        continue  # Continue the loop if there is an error

    # Ask if the user wants to run again
    repeat = input("Do you want to run again? (yes/no): ").strip().lower()

    if repeat != 'yes':
        print("Exiting the program.")
        break
