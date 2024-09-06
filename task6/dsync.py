import time

# Log start time of the script
script_start_time = time.time()




def find_divisible(end_range, divisor):
      # Log the start of the function
    print(f"find_divisibles called with range {end_range} and divisor {divisor}")

    # Create a list to store numbers that meet the criteria
    numbers = []
    
    # Loop through each number from 1 to end_range (inclusive)
    for i in range(1, end_range + 1):
        
        # Check if the number is divisible by 'divisor' 
        if i % divisor == 0:
            # Append the number to the list
            numbers.append(i)
            
    # Calculate the total time taken for the function call
    time_taken = time.time() - script_start_time

    # Log the end of the function with the time taken
    print(f"find_divisibles ended with range {end_range} and divisor {divisor}. It took {time_taken:.4f} seconds")
    print(f"\n")

    
    # Return the list of numbers
    return numbers





if __name__ == "__main__":
    # Call the function with three sets of arguments
    result1 = find_divisible(50800000, 34113)
    result2 = find_divisible(100052, 3210)
    result3 = find_divisible(500, 3)
      
    print("\nSecond function call result:", result2)
    print("\nThird function call result:", result3)
