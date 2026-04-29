print("Chatbot: Hi! I am a simple bot. (Type 'exit' to stop)")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help?")
    elif "how are you" in user:
        print("Chatbot: I am fine, thank you!")
    elif "your name" in user:
        print("Chatbot: I am CodeAlpha Bot.")
    elif "exit" in user or "bye" in user:
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: I don't understand, but sounds good!")