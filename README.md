
# 🚀 Django + React Firebase Push Notifications

A **full-stack demo** showing how to send **Firebase Cloud Messaging (FCM)** push notifications from a **Django backend** to a **React frontend** (with service workers).  
This project is **ready-to-run** locally and can be adapted for production.

---

## 📂 Project Structure

```

firebase-push-demo/
│
├── backend/                  # Django backend (API + FCM)
│   ├── backend/               # Django project config
│   ├── notifications/         # FCM notification app
│   ├── requirements.txt       # Backend dependencies
│   └── .env                    # Backend environment variables
│
└── frontend/                  # React frontend
├── public/
│   └── firebase-messaging-sw\.js  # Service worker
├── src/
│   ├── firebase.js         # Firebase config + helpers
│   ├── NotificationHandler.js  # Token + in-app notifications
│   └── App.js
└── .env                    # Frontend environment variables

````

---

## 🛠 Prerequisites

Install before starting:

- **Python** 3.10+ → [python.org](https://www.python.org/)
- **Node.js** (LTS) + npm → [nodejs.org](https://nodejs.org/)
- **Git** (optional but recommended)
- **Firebase project** → [console.firebase.google.com](https://console.firebase.google.com/)

---

## 🔑 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/), create a project.
2. **Add Web App** → Copy the config keys (used in `frontend/.env`).
3. **Enable Cloud Messaging** in Project Settings → Cloud Messaging tab.
4. **Generate VAPID Key** in *Web Push certificates* → Copy the Public Key to `REACT_APP_FIREBASE_VAPID_KEY`.
5. **Create Service Account Key**  
   - Project Settings → Service accounts → Generate new private key  
   - Save JSON as `firebase-adminsdk.json` in the `backend/` folder.

---

## ⚙️ Installation

### 1️⃣ Backend (Django)

```bash
cd backend
python -m venv venv

# Activate venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

**backend/.env**

```ini
FIREBASE_CREDENTIALS_PATH=./firebase-adminsdk.json
DJANGO_SECRET_KEY=your_django_secret
DEBUG=True
```

---

### 2️⃣ Frontend (React)

```bash
cd frontend
npm install
npm start
```

**frontend/.env**

```ini
REACT_APP_FIREBASE_API_KEY=your_api_key
REACT_APP_FIREBASE_AUTH_DOMAIN=your_auth_domain
REACT_APP_FIREBASE_PROJECT_ID=your_project_id
REACT_APP_FIREBASE_STORAGE_BUCKET=your_storage_bucket
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
REACT_APP_FIREBASE_APP_ID=your_app_id
REACT_APP_FIREBASE_VAPID_KEY=your_vapid_public_key
```

**frontend/public/firebase-messaging-sw\.js**
Contains your Firebase config (for service worker). Must be placed in `public/` so it’s served at `/firebase-messaging-sw.js`.

---

## ▶️ Running Locally

**Start backend:**

```bash
cd backend
# Activate venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # macOS/Linux
python manage.py runserver
```

**Start frontend:**

```bash
cd frontend
npm start
```

Open browser at: [http://localhost:3000](http://localhost:3000)
Allow notifications when prompted.
Copy the FCM token displayed on the page.

---

## 📤 Sending Test Notification

**From React UI:**
Click **"Send test notification"** in the app → backend sends FCM → React receives.

**From Terminal:**

```bash
curl -X POST http://127.0.0.1:8000/api/send_notification/ \
  -H "Content-Type: application/json" \
  -d '{
    "token": "PASTE_FCM_TOKEN",
    "title": "Hello from cURL",
    "body": "This is a test push notification"
  }'
```

---

## 🧩 How It Works

1. React requests Notification permission, gets FCM token via `getToken()`.
2. Service Worker (`firebase-messaging-sw.js`) handles background notifications.
3. Django uses `firebase-admin` SDK to send pushes to given token(s).
4. In foreground, `onMessage()` shows alerts in the React app.

---

## 🚨 Troubleshooting

| Problem                        | Solution                                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| Token is null                  | Ensure notifications are allowed, correct VAPID key, service worker registered          |
| Service worker not registering | Must be in `public/` folder, path `/firebase-messaging-sw.js`                           |
| CORS errors                    | Add `http://localhost:3000` to `CORS_ALLOWED_ORIGINS` in Django settings                |
| No notification in background  | Check service worker console logs, ensure payload format includes `notification` object |
| firebase-admin error           | Ensure `.env` `FIREBASE_CREDENTIALS_PATH` points to valid service account JSON          |

---

```


