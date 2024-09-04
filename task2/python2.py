import argparse  # Import the argparse library to handle command-line arguments
import math  # Import the math library for mathematical functions like square root

def parse_arguments():
    # Create the argument parser with a description of what the program does
    parser = argparse.ArgumentParser(description="Calculate the distance from the origin after a series of movements.")

    # Add an argument for UP, expecting a positive integer, and mark it as required
    parser.add_argument('--UP', type=int, required=True, help="Steps to move UP (positive integer).")
    
    parser.add_argument('--DOWN', type=int, required=True, help="Steps to move DOWN (positive integer).")

    parser.add_argument('--LEFT', type=int, required=True, help="Steps to move LEFT (positive integer).")

    parser.add_argument('--RIGHT', type=int, required=True, help="Steps to move RIGHT (positive integer).")

    # Parse the command-line arguments and store them in the 'args' object
    args = parser.parse_args()

    try:
        # Check if any of the parsed arguments are negative
        if args.UP < 0 or args.DOWN < 0 or args.LEFT < 0 or args.RIGHT < 0:
            # Raise a ValueError if a negative value is found
            raise ValueError("All steps must be non-negative integers.")

    except ValueError as e:
        # Print the error message if a ValueError is raised
        print(f"Error: {e}")
        # Exit the program with an error code (1) indicating something went wrong
        exit(1)

    # Return the parsed and validated arguments for use in the program
    return args

def main():
    # Parse the input arguments using the parse_arguments function
    args = parse_arguments()

    # Calculate the net vertical movement (UP - DOWN)
    vertical = args.UP - args.DOWN

    # Calculate the net horizontal movement (RIGHT - LEFT)
    horizontal = args.RIGHT - args.LEFT

    # Calculate the distance from the origin using the Pythagorean theorem
    distance = math.sqrt(vertical**2 + horizontal**2)

    # Print the distance, rounded to the nearest integer
    print(f"The distance from the origin is: {round(distance)}")

# This checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # If the script is run directly, execute the main function
    main()
