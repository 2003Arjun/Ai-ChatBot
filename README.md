# 🤖 AI ChatBot


<img width="1918" height="911" alt="image" src="https://github.com/user-attachments/assets/190a54c8-0d0a-4502-827f-5341c45d93f9" />


This is an **AI-powered ChatBot** that combines Google's Gemini AI with a custom neural network for intelligent conversations. It features a modern, responsive web interface with smooth animations and supports both AI responses and custom commands.

Powered by **Flask**, **Google Gemini AI**, and **PyTorch** with a beautiful **HTML/CSS/JS** frontend.

---

## 🚀 Features

- 🤖 **Google Gemini AI Integration** (Latest Gemini 2.0 Flash)
- 🧠 **Custom Neural Network Fallback** (PyTorch-based)
- 💬 **Smart Command System** (!info, !commands, !wiki, !weather)
- 🎨 **Modern Glass-morphism UI** with smooth animations
- 📱 **Fully Responsive Design** (Mobile & Desktop)
- ⚡ **Real-time Typing Indicators** and message bubbles
- 🔒 **Secure API Key Management** with environment variables

---

## 🧠 Tech Stack

| Layer           | Technology               |
|-----------------|--------------------------|
| Frontend        | HTML, CSS, JavaScript     |
| Backend         | Flask (Python)           |
| AI Engine       | Google Gemini AI         |
| ML Framework    | PyTorch                  |
| NLP             | NLTK                     |
| Environment     | python-dotenv            |

---

## 📁 Project Structure

```
AI-Chatbot/
├── templates/
│   └── index.html           # Modern UI interface
├── app.py                   # Flask application
├── gemini_chat.py          # Gemini AI integration
├── chatbot.py              # Custom neural network
├── model.py                # PyTorch model definition
├── nltk_utils.py           # NLP utilities
├── intents.json            # Training data
├── data.pth                # Trained model weights
├── .env                    # API keys (create this)
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Ai-ChatBot.git
cd Ai-ChatBot/AI-Chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy your API key

### 4. Configure Environment Variables
Create `.env` file:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

Server runs at 👉 [http://localhost:8000](http://localhost:8000)

---

## 🎯 How to Use

### **Regular Chat:**
- Type any message for AI-powered responses via Gemini
- Natural conversation with context understanding

### **Special Commands:**
| Command | Description |
|---------|-------------|
| `!info` | Learn about the creator |
| `!commands` | Show all available commands |
| `!wiki [topic]` | Get Wikipedia summary |
| `!weather [city]` | Get weather information |
| `!movie [title]` | Get movie information |

---

## 🔧 API Integration

The chatbot intelligently routes messages:
- **General messages** → Google Gemini AI
- **Special commands** → Custom neural network
- **Fallback** → Local model if API fails

---

## 🎨 UI Features

- **Glass-morphism design** with backdrop blur
- **Smooth animations** and transitions
- **Typing indicators** with animated dots
- **Message bubbles** with proper alignment
- **Responsive layout** for all devices
- **Custom scrollbars** and hover effects

---

## 📈 Future Enhancements

* 🎤 Voice input/output integration
* 🌍 Multi-language support
* 📊 Conversation analytics
* 🔄 Context memory across sessions
* 📱 Mobile app version
* ☁️ Cloud deployment

---

## 📬 Contact

Made by **Arjun Thakur**
💼 AI Developer | 🤖 Machine Learning Enthusiast
🔗 [GitHub](https://github.com/2003Arjun)

---
