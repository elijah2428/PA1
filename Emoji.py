def emotes(sentence):
    # Dictionary to map words to their corresponding emoticons
    emotes = {
        "smile": ":)",
        "grin": ":D",
        "sad": ":(",
        "mad": ">:("
    }

    # Split the sentence into words
    words = sentence.split()

    # Replace words with emoticons if they are in the dictionary
    replaced_words = [emotes[word.lower()] if word.lower() in emotes else word for word in words]

    # Join the words back into a sentence
    replaced_sentence = ' '.join(replaced_words)

    return replaced_sentence


# Ask the user to enter a sentence
user_input = input("Enter a sentence: ")

# Call the function with the user's input and print the result
result = emotes(user_input)
print("The modified sentence is:", result)
