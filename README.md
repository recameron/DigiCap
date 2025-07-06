# 🕰️ Digital Time Capsule

A full-stack web app that lets users write and schedule digital messages to be delivered or unlocked in the future.

---

## ✨ Features

* 📬 Create a digital message (capsule) with:

  * Text message
  * Recipient email
  * Future unlock date
* ✅ Form validation (message length, email, date)
* 📎 Sends capsule data to an Express backend (stored in-memory for now)
* 🎨 Styled with Tailwind CSS
* ⚛️ Built with React + Vite frontend
* 🚀 Node.js + Express backend API

---

## 📁 Project Structure

```
digital-time-capsule/
├── client/        # React frontend (Vite)
├── server/        # Node.js + Express backend
└── README.md      # You are here
```

---

## 🧑‍💻 Getting Started

### 🔧 Prerequisites

* Node.js (v18+ recommended)
* npm

### 1. Clone the repo

```bash
git clone https://github.com/your-username/digital-time-capsule.git
cd digital-time-capsule
```

### 2. Install dependencies

#### Client (frontend)

```bash
cd client
npm install
```

#### Server (backend)

```bash
cd ../server
npm install
```

### 3. Start the app

#### Run the backend server

```bash
cd server
node index.js
```

Server will run at: `http://localhost:4000`

#### Run the frontend (in another terminal)

```bash
cd client
npm run dev
```

Frontend will open at: `http://localhost:5173`

---

## 🌐 API Endpoints

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| POST   | `/api/capsules` | Create new capsule |
| GET    | `/api/capsules` | List all capsules  |

---

## 📌 TODO

* [ ] Save capsules to a database (e.g. MongoDB or SQLite)
* [ ] Add authentication (login/signup)
* [ ] Schedule email delivery (e.g. with Nodemailer + cron)
* [ ] Unlock capsules based on date logic
* [ ] Deploy to Render / Netlify / Vercel

---

## 📄 License

[MIT](LICENSE)

---

## 🧑‍💻 Author
[GitHub: @recameron](https://github.com/recameron)
