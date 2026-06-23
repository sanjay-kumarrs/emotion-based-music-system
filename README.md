# 🎵 Emo Player - Emotional Music Recommendation System

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Emo Player is a modern, AI-powered web application that detects user emotions from facial expressions in real-time and recommends tailored music playlists. Built on Django and integrated with a pre-trained Deep Learning CNN model for emotion recognition, Emo Player bridges the gap between human mood and music selection. It provides a robust Django Web Administration Panel for management and a set of REST APIs for mobile (Android) clients.

---

## 📐 System Architecture Flow

The workflow below illustrates the process from user image capture to targeted playlist recommendation:

```mermaid
graph TD
    A[User Face Capture / Upload] --> B[Face Detection via Haar Cascades]
    B --> C[Pre-processing: Rotate, Convert to Grayscale & Resize to 48x48]
    C --> D[Normalize Pixels [0, 1] & Run CNN Prediction]
    D --> E{Classify Emotion}
    E -->|Angry| F[Query 'angry' tagged songs]
    E -->|Disgust| G[Query 'disgust' tagged songs]
    E -->|Fear| H[Query 'fear' tagged songs]
    E -->|Happy| I[Query 'happy' tagged songs]
    E -->|Sad| J[Query 'sad' tagged songs]
    E -->|Surprise| K[Query 'surprise' tagged songs]
    E -->|Neutral| L[Query 'neutral' tagged songs]
    F & G & H & I & J & K & L --> M[Deliver Personalized Playlist to Mobile Client]
```

---

## ✨ Features

### 👤 Mobile Client (User Module)
*   **Aesthetic Registration & Authentication:** Secure profile creation and mobile logins.
*   **Face Emotion Capture:** Uploads a selfie camera snapshot to the backend to predict emotional states.
*   **Smart Music Recommendations:** Automatically displays playlists matching the predicted emotion (Happy, Sad, Angry, Neutral, Disgust, Fear, Surprise).
*   **Real-time Interactive Chat:** Chat with other platform users or administrators in real-time.
*   **Feedback & Complaints:** Submit feedback or complaints and track resolution replies.
*   **Service Rating:** Rate playlists and backend recommendation services.

### 🛡️ Admin Dashboard (Web-based Portal)
*   **Playlist Management:** Full CRUD operations on music files, genres, musicians, and their emotion categories.
*   **User Management:** View registered users, search profiles, and ban/remove accounts.
*   **Complaints Resolution:** Review user-submitted complaints and send replies.
*   **Ratings Analytics:** View ratings, statistics, and user feedback.
*   **Interactive Chat Center:** Connect with platform users.

---

## 🛠️ Technology Stack

*   **Backend Framework:** Django (v3.2.x)
*   **Database:** MySQL (Default) or SQLite (Local Development Fallback)
*   **Computer Vision & ML:** 
    *   **OpenCV** (Face detection using Haar Cascade frontal face classifier)
    *   **TensorFlow & Keras** (CNN model for emotion classification)
    *   **NumPy & SciPy** (Image matrix transformation, rotation, and processing)
*   **Python Version:** Python 3.10+

---

## 📁 Project Directory Layout

```text
emo_player/
├── db.sql                     # MySQL database schema and default dump
├── db.sqlite3                 # Local SQLite database fallback
├── manage.py                  # Django administrative entrypoint
├── requirements.txt           # Python package dependencies
├── templates/                 # Global HTML templates for Admin UI
├── static/                    # Custom CSS, JS, and image assets
├── media/                     # User-uploaded content (songs, emotion captures)
│   └── emotion/               # Camera snapshots for emotion detection
├── emo/                       # Core Django Application
│   ├── migrations/            # Database schema migrations
│   ├── model/                 # Facial Expression Recognition models & weights
│   │   ├── facial_expression_model_structure.json
│   │   ├── facial_expression_model_weights.h5
│   │   └── haarcascade_frontalface_default.xml
│   ├── emotion.py             # Preprocessing & test script for emotion prediction
│   ├── models.py              # Django ORM models (User, Playlist, Chat, etc.)
│   ├── views.py               # Main request handlers and business logic
│   └── urls.py                # App-level routing and REST endpoints
└── emo_player/                # Django Configuration Folder
    ├── settings.py            # Global settings (DB, apps, middleware)
    └── urls.py                # Project-level routing
```

---

## 💾 Database Schema Details

The application maps data entities to a MySQL / SQLite database using the Django ORM. Below is an overview of the custom database models defined in [models.py](file:///e:/project/25-03-2024/Web/emo_player/emo/models.py):

### 1. `Login` (Authentication System)
Represents credentials and access roles for the system.
*   `username` (CharField): Login handle.
*   `password` (CharField): Login password.
*   `type` (CharField): Role categorization (`admin`, `user`).

### 2. `User` (User Profiles)
Stores user biographical information.
*   `LOGIN` (ForeignKey): Link to `Login` credentials.
*   `fname` (CharField): First name.
*   `lname` (CharField): Last name.
*   `gender` (CharField): User gender.
*   `place` (CharField): Geographical place of residence.
*   `phone` (BigIntegerField): User contact phone number.
*   `email` (CharField): Email address.

### 3. `Manageplaylist` (Songs & Recommendation Playlists)
Stores songs uploaded by the administrator, categorizing them by emotion.
*   `LOGIN` (ForeignKey): Link to administrator login.
*   `song` (CharField): Title of the song.
*   `genre` (CharField): Genre details (e.g., Pop, Classical, Rock).
*   `musician` (CharField): Musician / Band name.
*   `details` (CharField): Short notes or descriptions.
*   `file` (FileField): Upload path to the audio file in media directory.
*   `emotion` (CharField): Mapped emotion (`happy`, `sad`, `angry`, `neutral`, `fear`, `disgust`, `surprise`).

### 4. `Chat` (Messaging Exchange)
Handles user-to-user and user-to-admin messages.
*   `Fromid` (ForeignKey): Sender's `Login` ID.
*   `Toid` (ForeignKey): Receiver's `Login` ID.
*   `message` (CharField): Text payload.
*   `date` (DateField): Date of message transmission.

### 5. `Complaints` (Support Management)
Allows users to flag issues to the administrator.
*   `user` (ForeignKey): Submitting `User`.
*   `Complaints` (CharField): Complaint text.
*   `date` (DateField): Date submitted or replied.
*   `reply` (CharField): Admin response (`waiting` by default).

### 6. `Rating` (Feedback Analysis)
Tracks platform ratings and written reviews.
*   `user` (ForeignKey): Submitting `User`.
*   `rating` (FloatField): Numerical score (e.g., 1.0 to 5.0).
*   `feedback` (CharField): Narrative feedback.
*   `date` (DateField): Date submitted.

---

## 🔌 REST API Documentation (Mobile App Integration)

The mobile client (Android application) interacts with the Django backend through a set of dedicated REST routes defined in [urls.py](file:///e:/project/25-03-2024/Web/emo_player/emo/urls.py). Below is the comprehensive endpoints catalogue:

| Endpoint | Method | Payload Parameters | Description |
| :--- | :---: | :--- | :--- |
| `/registration` | `POST` | `firstname`, `lastname`, `place`, `phone`, `email`, `username`, `password`, `Gender` | Registers a new user account. |
| `/login_code1` | `POST` | `uname`, `pass` | Authenticates user credentials. Returns `{"task": "valid", "id": <login_id>}`. |
| `/view_profile` | `POST` | `lid` | Fetches the user profile details (first name, email, phone, etc.). |
| `/edit_profile` | `POST` | `lid`, `fname`, `lname`, `email`, `phone`, `place` | Updates biographical info for the profile. |
| `/capture` | `POST` | `files` (Multipart File) | Accepts an image, processes face detection, runs CNN, and returns the predicted emotion, e.g., `{"task": "happy"}`. |
| `/viewplaylist_emo` | `POST` | `lid`, `emo` | Retrieves all audio files tagged with the given emotion (e.g., `sad`, `happy`). |
| `/send_complaint_app` | `POST` | `Complaint`, `lid` | Creates a new complaint ticket. Default reply is set to `waiting`. |
| `/reply_app` | `POST` | `lid` | Retrieves the list of user complaints and their replies. |
| `/delete_comp` | `POST` | `mid` | Deletes a complaint ticket. |
| `/send_Rating_app` | `POST` | `Ratings`, `feedback`, `lid` | Submits feedback rating for the recommendation engine. |
| `/in_message2` | `POST` | `fid`, `toid`, `msg` | Sends a message from user `fid` to user `toid`. |
| `/view_message2` | `POST` | `fid`, `toid`, `lastmsgid` | Queries messages between two users since `lastmsgid`. |
| `/chatwithuser` | `POST` | `lid` | Lists other registered system users for initiating chats. |
| `/viewplaylist` | `POST` | `lid` | Retrieves playlists uploaded or managed under login ID `lid`. |
| `/rplaylist` | `POST` | `mid` | Deletes an uploaded playlist record by its record ID. |

---

## 🧠 How Emotion Detection Works

1.  **Face Capture:** When the mobile application sends an image to `/capture`, it is temporarily stored in `media/emotion/`.
2.  **Preprocessing Pipeline:**
    *   The image is rotated 90 degrees clockwise (for default mobile portrait captures) using `scipy.ndimage.rotate`.
    *   It is converted to grayscale (`cv2.cvtColor`).
    *   Faces are located utilizing Haar Cascade classifier models (`haarcascade_frontalface_default.xml`).
3.  **Model Inference:**
    *   The detected face bounding box is cropped.
    *   The crop is resized to exactly `48x48` pixels.
    *   Image pixel values are normalized to a `[0, 1]` float range.
    *   The input is fed into a 7-layer Convolutional Neural Network (CNN) structural configuration loaded from [facial_expression_model_structure.json](file:///e:/project/25-03-2024/Web/emo_player/emo/model/facial_expression_model_structure.json) using weights stored in [facial_expression_model_weights.h5](file:///e:/project/25-03-2024/Web/emo_player/emo/model/facial_expression_model_weights.h5).
4.  **Recommendation Mapping:**
    *   The model returns probability scores across 7 classes: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, and `neutral`.
    *   The emotion corresponding to the maximum probability score is selected.
    *   The server queries `Manageplaylist` songs tagged with the predicted emotion and returns them to the client.

---

## 🚀 Setup & Installation

Follow these steps to run Emo Player locally on your machine:

### 1. Create and Activate Virtual Environment
It is highly recommended to isolate your dependencies inside a Python virtual environment:

```powershell
# Create the virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Windows (CMD)
.\venv\Scripts\activate.bat

# Activate on Unix/macOS
source venv/bin/activate
```

### 2. Install Project Dependencies
Use `pip` to install the requirements compiled in [requirements.txt](file:///e:/project/25-03-2024/Web/emo_player/requirements.txt):

```bash
pip install -r requirements.txt
```

> [!NOTE]
> If you encounter network timeouts or SSL verification issues, bypass them by using:
> `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

### 3. Database Initialization (MySQL Setup)
1.  Verify that your MySQL Server is active (e.g., via XAMPP, WAMP, or standalone MySQL).
2.  Open your MySQL Client shell and run:
    ```sql
    CREATE DATABASE emoplayer;
    ```
3.  Import the preconfigured SQL schema and initial seed data from [db.sql](file:///e:/project/25-03-2024/Web/emo_player/db.sql):
    ```bash
    mysql -u root -p emoplayer < db.sql
    ```
4.  Ensure that database credentials match your environment configuration in [settings.py](file:///e:/project/25-03-2024/Web/emo_player/emo_player/settings.py):
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'emoplayer',
            'PASSWORD': 'your_mysql_password_here',
            'PORT': '3306',
            'USER': 'root',
            'HOST': 'localhost',
        }
    }
    ```

### 4. Apply Migrations & Launch
Apply database schema migrations and boot up the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Once running, access the Admin Web Dashboard at: **`http://127.0.0.1:8000/`** (Default Administrator Login: username `admin`, password `123`).

---

## ⚠️ Crucial Configuration Alert

> [!CAUTION]
> ### Hardcoded Absolute Paths Warning
> The code in [views.py](file:///e:/project/25-03-2024/Web/emo_player/emo/views.py#L535-L622) and [emotion.py](file:///e:/project/25-03-2024/Web/emo_player/emo/emotion.py#L22-L87) contains hardcoded absolute Windows directory paths pointing to `E:\25-03-2024\Web\emo_player\`. 
> 
> To prevent `FileNotFoundError` crashes when capturing faces or predicting emotions, search for these paths in [views.py](file:///e:/project/25-03-2024/Web/emo_player/emo/views.py) and [emotion.py](file:///e:/project/25-03-2024/Web/emo_player/emo/emotion.py) and update them:
> 
> *   Replace absolute strings with paths relative to `settings.BASE_DIR`, or
> *   Update them to match your local repository's directory path (e.g., `e:\project\25-03-2024\Web\emo_player\`).
