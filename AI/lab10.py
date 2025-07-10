from fuzzywuzzy import process

# Predefined Questions & Answers
qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language.",
    "What is AI?": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
    "what is ML" : "ML stands for machine learning."
}

def chatbot():
    print(" Chatbot: Ask me anything! (Type 'exit' to stop)")
    while True:
        user_input = input("You: ")  
        if user_input.lower() == "exit":
            print(" Chatbot: Goodbye! ")
            break
        
        # Find the best match from predefined questions
        best_match, score = process.extractOne(user_input, qa_pairs.keys())

        # If the match confidence is high, return the answer
        if score > 70:
            print(f" Chatbot: {qa_pairs[best_match]}")
        else:
            print(" sorry")

# Run the chatbot
chatbot()