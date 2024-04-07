

print("**********Welcome to my Chatbot!*********")

while True:
    user_input = input("Enter your prompt: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Hello! How can I assist you today?")
    elif user_input == "how are you":
        print("I'm doing well, thanks for asking! What can I help you with?")
    elif user_input == "what's your name?":
        print("My name is Chatbot. What's yours?")
    elif user_input == "where are you from?":
        print("I exist in the digital world, so I don't have a physical location.")
    elif user_input == "thanks":
        print("You're welcome!")
    elif user_input in ["bye", "exit"]:
        print("Goodbye! Have a great day.")
        break
    else:
        print("Sorry, I couldn't understand that. Can you please ask something else?")
