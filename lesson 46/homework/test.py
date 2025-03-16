import nltk
from nltk.chat.util import Chat, reflections
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Define basic chatbot responses using NLTK's Chat
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm just a bot, but I'm doing well!", "I'm great! What about you?"]),
    (r"what is your name?", ["I'm a chatbot.", "You can call me ChatGPT!"]),
    (r"who created you?", ["I was created by a programmer.", "I was made to chat with you!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]),
]

# Initialize the simple chatbot
nltk_chatbot = Chat(pairs, reflections)

# Advanced chatbot using ChatterBot
advanced_bot = ChatBot("SmartBot")
trainer = ChatterBotCorpusTrainer(advanced_bot)
trainer.train("chatterbot.corpus.english")

def chatbot_response(user_input):
    # Check simple responses first
    response = nltk_chatbot.respond(user_input)
    if response:
        return response
    
    # Use ChatterBot for more advanced responses
    return advanced_bot.get_response(user_input)

# Run the chatbot in a loop
print("Chatbot is ready! Type 'quit' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "quit":
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
