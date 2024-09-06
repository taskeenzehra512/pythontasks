import time
import asyncio

# Log start time of the script
script_start_time = time.time()

# Asynchronous function definition
async def async_find_divisibles(end_range, divisor):
    # Log the start of the function
    
    print(f"\nasync_find_divisibles called with range {end_range} and divisor {divisor}")
    
    # Create a list to store numbers divisible by the divisor
    numbers = []
    
    # Loop through numbers from 1 to number_range
    for i in range(1, end_range + 1):
        if i % divisor == 0:
            # Append divisible number to the list
            numbers.append(i)
            # Yield control back to the event loop to let other tasks run
            await asyncio.sleep(0)  # Yield control after finding each divisible number
    
    # Calculate time taken since the script started
    time_taken = time.time() - script_start_time

    # Log the end of the function with time taken
    print(f"\nasync_find_divisibles ended with range {end_range} and divisor {divisor}. It took {time_taken:.4f} seconds")
    print(f"\n")

    return numbers

# Main driver code
async def main():
    # Create three tasks for the async_find_divisibles function
    task1 = asyncio.create_task(async_find_divisibles(50800000, 34113))
    task2 = asyncio.create_task(async_find_divisibles(100052, 3210))
    task3 = asyncio.create_task(async_find_divisibles(500, 3))
    
    # Wait for all tasks to complete concurrently
    result1, result2, result3 = await asyncio.gather(task1, task2, task3)


    # Print the results of the second and third function calls
    print("\nSecond function call result:", result2)
    print("\nThird function call result:", result3)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
