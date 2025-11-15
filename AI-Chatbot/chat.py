import random
import json
import torch
import wikipedia
import requests
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

# Bot name
bot_name = "Bot"

# Context state
info_triggered = False

def get_weather(city):
    # Example placeholder; you must replace with actual weather API if needed
    return f"The weather in {city} is warm and sunny with a high of 30°C."

print("Let's chat! Type '!quit' to exit.\n")

while True:
    sentence = input("You: ")

    if sentence.lower() == "!quit":
        break

    # Commands handling
    if sentence.lower() == "!commands":
        print(f"{bot_name}: Use the command !movie followed by a movie title to receive a summarized description of your movie. For example, !movie spiderman 3\n")
        print(f"{bot_name}: Use the command !wiki followed by a query to receive a summarized description of your topic. For example, !wiki tiger.\n")
        print(f"{bot_name}: Use the command !weather followed by a city in malaysia to receive a weather report of your city. For example, you can try !weather petaling jaya.")
        continue

    if sentence.lower() == "!info":
        info_triggered = True
        print(f"{bot_name}: Greetings! I'm a personal chatbot created by Arjun to help answer questions about him. Refer below for ideas on what you can ask me :)\n")
        print("1) Get to know Arjun by asking me about his background, education, work experiences, future plans, skills, hobbies, spoken languages, birthday, age.")
        print("2) If you're not interested to know more about Arjun, I was built with some additional features that you might find interesting! Type !commands for more information.")
        continue

    if info_triggered and sentence.strip() == "1":
        print(f"{bot_name}: Arjun is a software developer with experience in Python, machine learning, and backend systems. He enjoys working on AI projects and building useful applications.")
        info_triggered = False
        continue

    if info_triggered and sentence.strip() == "2":
        print(f"{bot_name}: You can try !commands to explore features like movie lookup, Wikipedia info, and weather updates.")
        info_triggered = False
        continue

    if sentence.lower().startswith("!wiki"):
        query = sentence[6:].strip()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2)
                print(f"{bot_name}: {summary}")
            except:
                print(f"{bot_name}: Sorry, I couldn't find any information on '{query}'.")
        else:
            print(f"{bot_name}: Please enter a topic after !wiki.")
        continue

    if sentence.lower().startswith("!movie"):
        movie_title = sentence[7:].strip()
        if movie_title:
            print(f"{bot_name}: Here's a summary of the movie '{movie_title}':")
            print(f"{bot_name}: [Placeholder summary] This movie is a thrilling adventure with great reviews!")  # Replace with real API if needed
        else:
            print(f"{bot_name}: Please enter a movie title after !movie.")
        continue

    if sentence.lower().startswith("!weather"):
        city = sentence[9:].strip()
        if city:
            weather_report = get_weather(city)
            print(f"{bot_name}: {weather_report}")
        else:
            print(f"{bot_name}: Please enter a city after !weather.")
        continue

    # Predict intent
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
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I'm not sure I understand. Try typing !commands or ask something else.")
    print()  # Print a new line for better readability
# End of chat loop
print("Goodbye! Thanks for chatting.")
# End of chat session
# Save the chat session