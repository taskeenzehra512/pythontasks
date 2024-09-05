def find_divisible(start_range, end_range, divisor1, divisor2):
      
    # Create a list to store numbers that meet the criteria
    numbers = []
    
    # Loop through each number from 1 to end_range (inclusive)
    for i in range(start_range, end_range + 1):
        
        # Check if the number is divisible by 'divisor' 
        if i % divisor1 == 0  and i % divisor2 != 0:
            # Append the number to the list
            numbers.append(i)

    return numbers       


if __name__ == "__main__":
    # Call the function with three sets of arguments
    result = find_divisible(2000, 3201, 7, 5)
    print(f"Result is: ",result)

