# 🎵 Emo Player - Emotional Music Recommendation System

Emo Player is a modern, AI-powered web application that detects user emotions from facial expressions in real-time and recommends tailored music playlists. Built on Django and integrated with a pre-trained Deep Learning CNN model for emotion recognition, Emo Player bridges the gap between human mood and music selection.

---

## ✨ Features

### 👤 User Module
*   **Aesthetic Registration & Authentication:** Secure login and profile creation.
*   **Face Emotion Capture:** Real-time camera integration using OpenCV to capture facial expressions.
*   **Smart Playlists:** Automated retrieval of playlists that match the predicted emotion (e.g., Happy, Sad, Angry, Neutral).
*   **Interactive Chat:** Direct communication channel between users and the administrator.
*   **Complaints & Feedback:** Submit complaints and review responses.
*   **Rating System:** Rate the service and playlists to help improve recommendation quality.

### 🛡️ Admin Dashboard
*   **Playlist Management:** Full CRUD operations on music files, genres, and associated emotion categories.
*   **User Management:** View registered users, search profiles, and ban/remove accounts.
*   **Complaints Resolution:** View complaints submitted by users and send feedback/replies.
*   **Ratings Analytics:** View ratings and feedback with search filters.
*   **Chat Center:** Send and receive real-time messages with users.

---

## 🛠️ Technology Stack

*   **Backend Framework:** Django (v3.2.x)
*   **Database:** MySQL (Default) / SQLite (Fallback)
*   **Computer Vision & ML:** 
    *   **OpenCV** (Face detection using Haar Cascade classifier)
    *   **TensorFlow & Keras** (CNN model for emotion class prediction: angry, disgust, fear, happy, sad, surprise, neutral)
    *   **NumPy & SciPy** (Image matrix transformation and rotation)
*   **Python Version:** Python 3.10+

---

## 📁 Directory Structure

```text
emo_player/
├── db.sql                     # MySQL database schema and default dump
├── db.sqlite3                 # Local SQLite database fallback
├── manage.py                  # Django administrative entrypoint
├── requirements.txt           # Python package dependencies
├── venv/                      # Python virtual environment (to be created)
├── templates/                 # Global HTML templates
├── static/                    # Custom CSS, JS, and image assets
├── media/                     # User-uploaded content (songs, emotion captures)
│   └── emotion/               # Camera snapshots for emotion detection
├── emo/                       # Core Django Application
│   ├── migrations/            # Database schema migrations
│   ├── model/                 # Facial Expression Recognition models & weights
│   │   ├── facial_expression_model_structure.json
│   │   ├── facial_expression_model_weights.h5
│   │   └── haarcascade_frontalface_default.xml
│   ├── emotion.py             # Image preprocessing and model prediction script
│   ├── models.py              # Django ORM models (User, Playlist, Chat, etc.)
│   ├── views.py               # Request handlers and business logic
│   └── urls.py                # App-level routing
└── emo_player/                # Django Configuration Folder
    ├── settings.py            # Global settings (DB, apps, middleware)
    └── urls.py                # Project-level routing
```

---

## 🚀 Setup & Installation

Follow these steps to set up and run Emo Player locally on your system:

### 1. Create and Activate Virtual Environment
Create a localized Python environment to install dependencies without polluting your global packages.

```powershell
# Create the virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Windows (CMD)
.\venv\Scripts\activate.bat
```

### 2. Install Dependencies
Install Django, OpenCV, TensorFlow, and all other required libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> If you encounter SSL verification issues during installation, you can bypass them by using:
> `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

### 3. Database Setup (MySQL)
1. Ensure you have a MySQL server running (e.g., via XAMPP, WampServer, or a native MySQL installation).
2. Create a database named `emoplayer`:
   ```sql
   CREATE DATABASE emoplayer;
   ```
3. Import the `db.sql` database file into your server:
   ```bash
   mysql -u root -p emoplayer < db.sql
   ```
4. Verify setting credentials in [settings.py](file:///e:/project/25-03-2024/Web/emo_player/emo_player/settings.py):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'emoplayer',
           'PASSWORD': '',  # Add your MySQL password here
           'PORT': '3306',
           'USER': 'root',
           'HOST': 'localhost',
       }
   }
   ```

### 4. Run Django Migrations & Launch Server
After the database is configured, apply the Django migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open your browser and navigate to: **`http://127.0.0.1:8000/`**

---

## 🧠 How Emotion Detection Works

1. **Face Capture:** When the user clicks the capture button, the webcam or client app captures an image.
2. **Face Extraction:** The backend reads the image, rotates it if necessary, converts it to grayscale, and locates the face region using the Haar Cascade Classifier (`haarcascade_frontalface_default.xml`).
3. **Model Prediction:** The cropped face image is resized to `48x48` pixels, normalized to `[0, 1]`, and fed into the CNN architecture (`facial_expression_model_structure.json` with weights `facial_expression_model_weights.h5`).
4. **Music Mapping:** The model outputs probabilities for the 7 standard emotions. The highest probability emotion is selected and matched against playlists configured with the same emotion tag.
