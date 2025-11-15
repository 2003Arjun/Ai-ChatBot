# 🤖 AI ChatBot
A clean, modern AI chatbot powered by Google Gemini AI with neural network fallback and smart markdown formatting.


<img width="781" height="873" alt="image" src="https://github.com/user-attachments/assets/3724be9f-8f81-4052-b0c9-1610c4e8317d" />


## ✨ Features

- **Google Gemini AI Integration** - Latest Gemini 2.0 Flash model
- **Neural Network Fallback** - Custom PyTorch model for offline use
- **Smart Commands** - `!info`, `!commands`, `!wiki`, `!weather`
- **Clean UI** - Minimal, responsive design
- **Markdown Support** - Auto-converts bullet points and formatting
- **Real-time Weather** - OpenWeatherMap API integration

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/2003Arjun/Ai-ChatBot.git
cd Ai-ChatBot
```

### 2. Install Dependencies
```bash
pip install -r AI-Chatbot/requirements.txt
```

### 3. Setup API Keys
Create `AI-Chatbot/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_openweather_api_key
```

### 4. Run Application
```bash
cd AI-Chatbot
python app.py
```

Visit: http://localhost:8000

## 🔑 API Keys

- **Gemini API**: [Google AI Studio](https://aistudio.google.com/app/apikey)
- **Weather API**: [OpenWeatherMap](https://openweathermap.org/api) (Free)

## 💬 Commands

| Command | Description |
|---------|-------------|
| `!info` | About the creator |
| `!commands` | Show all commands |
| `!wiki [topic]` | Wikipedia summary |
| `!weather [city]` | Weather information |

## 🛠️ Tech Stack

- **Backend**: Flask, Python
- **AI**: Google Gemini AI, PyTorch
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenWeatherMap, Wikipedia

## 📁 Project Structure

```
AI-Chatbot/
├── templates/index.html    # Frontend UI
├── app.py                  # Flask server
├── gemini_chat.py         # Gemini AI integration
├── chatbot.py             # Neural network fallback
├── weather_api.py         # Weather service
├── model.py               # PyTorch model
├── requirements.txt       # Dependencies
└── .env                   # API keys
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - see LICENSE file for details.

## 👨‍💻 Author

**Arjun Thakur**
- GitHub: [@2003Arjun](https://github.com/2003Arjun)
- AI Developer & ML Enthusiast

---

⭐ Star this repo if you found it helpful!
