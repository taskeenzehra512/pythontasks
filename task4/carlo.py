import argparse
import json
import random
import os
import sys  # Add this to use sys.exit()

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        # randomly generates points in square 1x1
        x, y = random.random(), random.random()
        # check if the point is inside the unit circle (distance from origin < 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    # Estimate pi as 4 times the ratio of points inside the circle to total points
    return (4 * inside_circle) / num_samples


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Monte Carlo Pi Estimation Tool", 
        epilog="Example usage: python monte_carlo.py -i 1000000 or python monte_carlo.py -j"
    )

    # Adding arguments for -i, -j, and -h (help is automatic)
    parser.add_argument('-i', type=int, help="Number of iterations for Monte Carlo simulation")
    parser.add_argument('-j', help="Read number of iterations from a JSON file", action='store_true')
    
    # Parse the arguments
    args = parser.parse_args()

    # Case 1: If -j flag is passed, read iterations from config.json
    if args.j:
        json_file = 'config.json'  # Assuming the JSON file is named 'config.json'

        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                data = json.load(file)
                num_samples = data.get('iterations', 1000)  # Default to 1000 iterations if not found
        else:
            print(f"Error: {json_file} file not found.")
            sys.exit()  # Use sys.exit() to stop execution if the file is not found

    # Case 2: If -i flag is passed, take the number of iterations from the user input
    elif args.i:
        num_samples = args.i

    # Case 3: If neither flag is passed, show an error message
    else:
        print("Error: You must pass either '-i' for iterations or '-j' for JSON input.")
        sys.exit()  # Use sys.exit() to stop execution if no valid flag is passed

    # Running the Monte Carlo simulation
    pi_estimate = estimate_pi(num_samples)
    print(f"Estimated Pi after {num_samples} iterations: {pi_estimate}")
