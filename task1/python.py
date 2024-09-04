# Create a list to store numbers that meet the criteria
numbers = []

# Loop through each number from 2000 to 3200 (inclusive)
for i in range(2000, 3201):
    
    # Check if the number is divisible by 7 and not divisible by 5
    if i % 7 == 0 and i % 5 != 0:
        
        # Append the number to the list
        numbers.append(i)

# Convert the list of numbers to a comma-separated string and print it
print(",".join(map(str, numbers)))
