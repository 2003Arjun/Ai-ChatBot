# Ai-ChatBot
screenshot:
![chat bot screenshot](https://github.com/user-attachments/assets/86a42a88-b4cc-4b28-8f3c-10d6abb73780)


# ✅ Fullstack Todo App using Node.js, Express & MySQL

This is a **Fullstack Todo Application** that allows users to manage their daily tasks efficiently with features like authentication, task creation, updates, and completion tracking.  
It is powered by a **Node.js + Express** backend, a **MySQL** database, and a clean **HTML/CSS/JS** frontend.

---

## 🚀 Features

- 🔐 **User Authentication** (Register/Login with JWT)
- 🧾 **Add, Edit, Delete Tasks**
- ✅ **Mark Tasks as Completed**
- 💾 **Persistent Database Storage (MySQL)**
- 🌐 **RESTful API Endpoints for Task Management**
- 💻 **Simple, Responsive Frontend UI**

---

## 🧠 Tech Stack

| Layer           | Technology               |
|-----------------|--------------------------|
| Frontend        | HTML, CSS, JavaScript     |
| Backend         | Node.js, Express.js       |
| Database        | MySQL                    |
| Authentication  | JWT (JSON Web Token)      |
| Environment     | dotenv                    |

---

## 📁 Folder Structure

```

todo-app/
├── server/                  # Backend code (APIs)
│   ├── routes/              # API route definitions
│   ├── controllers/         # Business logic for routes
│   ├── models/              # Database models (MySQL tables)
│   ├── middleware/          # JWT auth middleware
│   ├── config/              # DB connection setup
│   ├── server.js            # Entry point
│
├── public/ or client/       # Frontend files
│   ├── index.html           # UI for Todo app
│   ├── style.css            # Styling
│   └── script.js            # API integration
│
├── .env                     # Environment variables
├── package.json             # Node.js dependencies
└── README.md

````

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Todo-App.git
cd Todo-App
````

### 2. Install Dependencies

```bash
cd server
npm install
```

### 3. Configure Environment Variables

Create a `.env` file inside the `server/` folder:

```bash
PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=todo_app
JWT_SECRET=your_jwt_secret
```

### 4. Setup MySQL Database

Run the following SQL command to create the database:

```sql
CREATE DATABASE todo_app;
```

The application will automatically create tables when started (if configured with Sequelize/Knex) or you can define your own schema.

### 5. Run the Backend Server

```bash
npm start
```

Server runs at 👉 [http://localhost:5000](http://localhost:5000)

### 6. Run the Frontend

Open `public/index.html` in your browser or host it on a simple server.

---

## 📡 API Endpoints

| Method | Endpoint             | Description             | Auth Required |
| ------ | -------------------- | ----------------------- | ------------- |
| POST   | `/api/auth/register` | Register a new user     | ❌             |
| POST   | `/api/auth/login`    | Login and get JWT token | ❌             |
| GET    | `/api/tasks`         | Get all tasks           | ✅             |
| POST   | `/api/tasks`         | Create a new task       | ✅             |
| PUT    | `/api/tasks/:id`     | Update a specific task  | ✅             |
| DELETE | `/api/tasks/:id`     | Delete a task           | ✅             |

---

## 🧪 Testing the App

1. Register a new user via frontend or Postman
2. Login to get the JWT token
3. Use the token to access `/api/tasks` routes
4. Add, edit, or delete your tasks dynamically

---

## 🔌 Optional: Add Email Notification (Nodemailer)

You can extend the app by adding **email reminders** for pending tasks.

```js
import nodemailer from "nodemailer";

const sendReminder = async (email, task) => {
  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: { user: "your_email@gmail.com", pass: "your_app_password" }
  });

  await transporter.sendMail({
    from: "Todo App",
    to: email,
    subject: "Task Reminder",
    text: `Don't forget to complete: ${task}`
  });
};
```

---

## 📈 Future Scope

* 📱 Responsive React frontend
* 🕓 Task scheduling & reminders
* ☁️ Deploy backend on Render or Railway
* 📊 Dashboard for completed vs pending tasks
* 💬 Notifications or email alerts

---

## 📬 Contact

Made by **Arjun Thakur**
💼 Backend Developer | 🌐 MERN Stack Enthusiast
🔗 [GitHub](https://github.com/2003Arjun)

---








