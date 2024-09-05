import argparse
import math

# Initialize the parser
parser = argparse.ArgumentParser(description="Move in 2D space")

# Add arguments for each direction
parser.add_argument('--up', type=int, default=0, help='Move up by a number of units')
parser.add_argument('--down', type=int, default=0, help='Move down by a number of units')
parser.add_argument('--left', type=int, default=0, help='Move left by a number of units')
parser.add_argument('--right', type=int, default=0, help='Move right by a number of units')

# Parse the arguments
args = parser.parse_args()

# Initialize position
x, y = 0, 0

# Apply movements
y += args.up
y -= args.down
x -= args.left
x += args.right

# Print final position
print(f"Final position: ({x}, {y})")

# Distance formula
distance = math.sqrt(x**2+y**2)
print(f"Distance from origin: {distance}")