import random

class SimpleBot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
            "how are you": ["I'm doing well, thanks!", "I'm great! How about you?"],
            "bye": ["Goodbye!", "See you later!", "Have a great day!"],
            "name": ["I'm ChatBot, nice to meet you!", "You can call me ChatBot!"],
            "help": ["I can chat with you! Try saying hello, asking how I am, or asking my name."]
        }

    def get_response(self, user_input):
        # Convert input to lowercase for better matching
        user_input = user_input.lower()

        # Check for matching keywords
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])

        # Default response if no keywords match
        return "I'm not sure how to respond to that. Try asking for 'help'."

def main():
    bot = SimpleBot()
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot:", bot.get_response(user_input))
            break
        
        response = bot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()




































































































































































































































    