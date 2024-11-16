import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why couldn’t the bicycle stand up by itself? It was two tired!",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "How does a penguin build its house? Igloos it together!",
    "Why don’t eggs tell jokes? They’d crack each other up!"
]

print("Welcome to the Random Joke Generator!")
print("Type 'joke' to get a random joke, or type 'quit' to exit.\n")

while True:
    command = input("Your choice (joke/quit): ").lower()

    if command == "joke":
        print("\nHere's a joke for you:")
        print(random.choice(jokes))
        print()
    elif command == "quit":
        print("Thanks for laughing with us! Goodbye!")
        break
    else:
        print("Invalid input. Please type 'joke' or 'quit'.\n")
