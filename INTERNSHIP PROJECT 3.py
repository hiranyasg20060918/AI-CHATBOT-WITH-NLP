import nltk
import numpy as np
import random
import string

# Download necessary nltk packages (only run once)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

# Sample knowledge base (you can expand later)
knowledge_base = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am an AI Chatbot built using Python and NLTK.",
    "bye": "Goodbye! Have a great day!",
}

lemmatizer = WordNetLemmatizer()

# Function to clean and preprocess user input
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Function to generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key]
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Main loop
print("🤖 AI Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 AI Chatbot:", knowledge_base["bye"])
        break
    response = chatbot_response(user_input)
    print("🤖 AI Chatbot:", response)
