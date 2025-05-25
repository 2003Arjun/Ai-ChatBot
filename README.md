# Ai-ChatBot
screenshot:
![chat bot screenshot](https://github.com/user-attachments/assets/86a42a88-b4cc-4b28-8f3c-10d6abb73780)






## 📘 README.md (GitHub-ready)

Here is a **detailed README** you can include in your GitHub repository:

```markdown
# 🤖 AI Chatbot using Django, scikit-learn & NLTK

This is an intelligent chatbot system built using Django (Python Web Framework), trained with `scikit-learn`, and enhanced using NLTK for natural language processing. It allows users to interact through a web-based chat interface and receive intelligent responses based on predefined intents.

---

## 🚀 Features

- Train your own intent classification model with `scikit-learn`
- Use NLTK for tokenization and stemming
- Django backend to handle chat communication
- Dynamic web interface (HTML/JS)
- Persistent model files for fast loading

---

## 🧠 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Frontend     | HTML, JavaScript |
| Backend      | Django (Python) |
| ML Model     | scikit-learn (Logistic Regression / SVM) |
| NLP          | NLTK (tokenize, stem) |
| Storage      | `pickle` for model, vectorizer, label encoder |

---

## 📁 Folder Structure

```

AI-Chatbot/
├── templates/              # HTML templates for chatbot UI
├── app.py / manage.py      # Entry point (Flask or Django)
├── train.py                # Model training script
├── model.py                # Model architecture (optional)
├── chat.py                 # Model inference logic
├── intents.json            # Intent classification data
├── chatbot\_model.pkl       # Trained ML model
├── vectorizer.pkl          # Text vectorizer
├── label\_encoder.pkl       # Label encoder for tags
├── nltk\_utils.py           # NLP preprocessing (tokenize, stem)
├── venv/                   # Python virtual environment (optional)

````

---

## ⚙️ Installation & Setup

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/AI-Chatbot.git
cd AI-Chatbot
````

### 2. Create & activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install requirements:

```bash
pip install -r requirements.txt
```

(If `requirements.txt` doesn’t exist, manually install these:)

```bash
pip install django scikit-learn nltk
```

### 4. Download NLTK data (if needed):

```bash
python download_nltk_data.py
```

### 5. Train the model (optional):

```bash
python train.py
```

### 6. Run the server:

```bash
python manage.py runserver
```

Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Testing the Chatbot

1. Open the home page
2. Enter inputs like:

   * "Hi"
   * "What can you do?"
   * "Tell me about Arjun"
   * "What is your name?"
3. Get a response based on intent classification.

---

## 🛠 Customization

* Update `intents.json` to modify questions/responses
* Re-train the model via `train.py`
* Modify views in Django to add new pages

---

## 📬 Contact

Made by **Arjun** – feel free to contribute, fork, or submit PRs!

---

Perfect! Here's an updated version of your **README** section with added support for **Weather and Movie APIs** so users know they can extend the chatbot functionality.

---

## 🧠 Tech Stack

| Layer           | Technology                                     |
| --------------- | ---------------------------------------------- |
| Frontend        | HTML, JavaScript                               |
| Backend         | Django (Python)                                |
| ML Model        | scikit-learn (e.g., Logistic Regression / SVM) |
| NLP             | NLTK (tokenization, stemming)                  |
| Storage         | Pickled `.pkl` files                           |
| Extensible APIs | OpenWeatherMap, TMDB (Movie API) ✅             |

---

## 🔌 Optional: Add Weather & Movie APIs

You can enhance the chatbot by integrating third-party APIs. For example:

### 🌦 Weather API (OpenWeatherMap)

* **Use case**: Allow users to ask, *“What’s the weather in Delhi?”*
* **How**:

  * Sign up at [https://openweathermap.org/api](https://openweathermap.org/api)
  * Use Python's `requests` module to fetch live weather data
  * Add an intent like `"weather"` in `intents.json`
  * Create a response handler in `chat.py`

```python
import requests

def get_weather(city="Delhi"):
    API_KEY = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    temp = response["main"]["temp"]
    return f"The temperature in {city} is {temp}°C."
```

---

### 🎬 Movie Info API (TMDB)

* **Use case**: Ask *“Tell me about the movie Inception”*
* **How**:

  * Get an API key at [https://www.themoviedb.org/documentation/api](https://www.themoviedb.org/documentation/api)
  * Add an `"movie_info"` intent and respond by fetching movie metadata

```python
def get_movie_info(title="Inception"):
    API_KEY = "your_tmdb_api_key"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url).json()
    if response["results"]:
        movie = response["results"][0]
        return f"{movie['title']} - {movie['overview']}"
    return "Movie not found."
```

---

## 📈 Future Scope

* Add chatbot memory using session storage
* Deploy on cloud (Render/Heroku)
* Use LLMs like GPT-3.5 or Rasa for better understanding
* Integrate voice-to-text and text-to-speech
* Enable database logging of chats

---

Let me know when you’re ready for the final `.zip` package or want help coding the weather/movie integration!
