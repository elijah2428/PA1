def alphabet_soup(s):
    # Convert the string into a sorted list of characters
    sorted_characters = sorted(s)
    # Join the sorted characters back into a string
    sorted_string = ''.join(sorted_characters)
    return sorted_string

# Ask the user to enter a word
usr_input = input("Enter the word: ")

# Call the function with the user's input and print the result
result = alphabet_soup(usr_input)
print("the sorted form is:", result)