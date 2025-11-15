import random
import json
import torch
import wikipedia
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load intents file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Load trained model
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Bot"
info_triggered = False  # This keeps state between calls


def get_weather(city):
    # Placeholder: Replace this with real API calls
    return f"The weather in {city} is warm and sunny with a high of 30°C."


def get_response(sentence):
    global info_triggered

    sentence_lower = sentence.lower()

    if sentence_lower == "!commands":
        return ("Use the command !movie followed by a movie title to receive a summarized description of your movie.\n"
                "Use the command !wiki followed by a query to receive a summarized description of your topic.\n"
                "Use the command !weather followed by a city in malaysia to receive a weather report of your city.")

    if sentence_lower == "!info":
        info_triggered = True
        return ("Greetings! I'm a personal chatbot created by Arjun to help answer questions about him. "
                "Refer below for ideas on what you can ask me :)\n"
                "1) Get to know Arjun by asking me about his background, education, work experiences, future plans, skills, hobbies, spoken languages, birthday, age.\n"
                "2) If you're not interested to know more about Arjun, I was built with some additional features that you might find interesting! Type !commands for more information.")

    if info_triggered:
        if sentence.strip() == "1":
            info_triggered = False
            return "Arjun is a software developer with experience in Python, machine learning, and backend systems. He enjoys working on AI projects and building useful applications."
        elif sentence.strip() == "2":
            info_triggered = False
            return "You can try !commands to explore features like movie lookup, Wikipedia info, and weather updates."

    if sentence_lower.startswith("!wiki"):
        query = sentence[6:].strip()
        if query:
            try:
                return wikipedia.summary(query, sentences=2)
            except:
                return f"Sorry, I couldn't find any information on '{query}'."
        else:
            return "Please enter a topic after !wiki."

    if sentence_lower.startswith("!movie"):
        movie_title = sentence[7:].strip()
        if movie_title:
            return f"Here's a summary of the movie '{movie_title}': [Placeholder summary] This movie is a thrilling adventure with great reviews!"
        else:
            return "Please enter a movie title after !movie."

    if sentence_lower.startswith("!weather"):
        city = sentence[9:].strip()
        if city:
            return get_weather(city)
        else:
            return "Please enter a city after !weather."

    # Intent classification
    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).float()

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "I'm not sure I understand. Try typing !commands or ask something else."
