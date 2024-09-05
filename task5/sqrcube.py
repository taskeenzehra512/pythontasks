import matplotlib.pyplot as plt

def square_list(numbers):
    # Function to square each number in the list
    return [x**2 for x in numbers]

def cube_list(numbers):
    # Function to cube each number in the list
    return [x**3 for x in numbers]

# List of numbers to be squared and cubed
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calling functions to get squared and cubed lists
squared_list = square_list(numbers)
cubed_list = cube_list(numbers)

# Printing the lists
print("Squared List:", squared_list)
print("Cubed List:", cubed_list)

# Plotting the graphs
plt.figure(figsize=(12, 6))

# Plot for squares
plt.subplot(1, 2, 1)
plt.plot(numbers, squared_list, marker='o', color='blue')
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.title('Square of Numbers')

# Plot for cubes
plt.subplot(1, 2, 2)
plt.plot(numbers, cubed_list, marker='o', color='red')
plt.xlabel('Numbers')
plt.ylabel('Cubes')
plt.title('Cube of Numbers')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
