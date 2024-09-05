def count_distinct_words():
    # Ask user to input the number of words
    n = int(input("Enter the number of words: "))
    
    # Create a dictionary to store word counts
    word_count = {}
    
    # Loop to collect words and count occurrences
    for _ in range(n):
        word = input("Enter word: ").strip()  # Get the word from user
        if word in word_count:
            word_count[word] += 1  # If word already exists, increment count
        else:
            word_count[word] = 1  # If new word, add it to dictionary with count 1
    
    # Output the number of distinct words
    print(f"\nNumber of distinct words: {len(word_count)}")
    
    # Output the counts of each word
    for word, count in word_count.items():
        print(f"{word}: {count}")



# Call the function
if __name__ == "__main__":
    count_distinct_words()
