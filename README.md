# 📚 SnapClass

### AI-Powered Smart Attendance System

> An AI-powered classroom attendance platform using **Face Recognition, Voice Recognition, and Cloud Database Integration**.

🔗 **Live Demo:** https://snapclass-gaurav.streamlit.app/
💻 **Source Code:** https://github.com/gauravmanjhi09/snapclass-main

---

SnapClass is an **AI-powered smart attendance system** designed to automate classroom attendance using **Face Recognition and Voice Recognition**.

Built with **Python, Streamlit, Computer Vision, Audio Processing, and Supabase**, SnapClass provides separate workflows for **teachers and students**, making classroom attendance faster, smarter, and easier to manage.

---

## ✨ Features

### 🤖 Face Recognition Attendance

SnapClass uses a face-recognition based pipeline to identify registered students and automate attendance.

**Workflow:**

```text
Student Image / Camera
        ↓
Face Detection
        ↓
Face Encoding
        ↓
Face Matching
        ↓
Student Identification
        ↓
Attendance Recorded
```

### 🎙️ Voice-Based Attendance

SnapClass also includes a dedicated **voice attendance pipeline** for audio-based identification.

The project uses:

* **Librosa** for audio processing
* **Resemblyzer** for speaker representation
* Audio feature extraction and matching

This provides an additional AI-based approach to classroom attendance.

---

## 👨‍🏫 Teacher Dashboard

Teachers have a dedicated dashboard to manage their classroom.

### Capabilities

* Create subjects
* Manage classroom subjects
* Enroll students
* Add student photos
* Start attendance sessions
* View attendance results
* Share subjects with students
* Generate/share classroom join codes

---

## 👨‍🎓 Student Dashboard

Students have a separate workflow for joining classrooms and participating in attendance.

### Capabilities

* Access student dashboard
* Join subjects using a join code
* Complete student enrollment
* Participate in attendance sessions
* Access subject-specific workflows

---

## 🔗 Join Code System

SnapClass provides a simple classroom joining mechanism.

```text
Teacher
   │
   ├── Create Subject
   │
   └── Generate Join Code
              │
              ▼
          Student
              │
              └── Enter Join Code
                       │
                       ▼
                  Join Subject
```

This makes it easier for teachers to share their subjects with students without manually configuring every student.

---

# 🧠 System Architecture

```text
                         ┌─────────────────────┐
                         │      SnapClass      │
                         │    Streamlit App    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
             ┌──────▼──────┐                 ┌──────▼──────┐
             │   Teacher   │                 │   Student   │
             │  Dashboard  │                 │  Dashboard  │
             └──────┬──────┘                 └──────┬──────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    │
                     ┌──────────────▼──────────────┐
                     │       AI Pipelines          │
                     ├─────────────────────────────┤
                     │  Face Recognition Pipeline  │
                     │  Voice Processing Pipeline  │
                     └──────────────┬──────────────┘
                                    │
                           ┌────────▼────────┐
                           │    Supabase     │
                           │    Database     │
                           └─────────────────┘
```

---

# 🛠️ Tech Stack

| Category                  | Technology             |
| ------------------------- | ---------------------- |
| Programming Language      | Python                 |
| Application Framework     | Streamlit              |
| Computer Vision           | Face Recognition, dlib |
| Machine Learning          | scikit-learn           |
| Data Processing           | NumPy, Pandas          |
| Database                  | Supabase               |
| Authentication / Security | bcrypt                 |
| Image Processing          | Pillow                 |
| Audio Processing          | Librosa                |
| Speaker Recognition       | Resemblyzer            |
| QR / Code Utilities       | Segno                  |

---

# 📂 Project Structure

```text
snapclass-main/
│
├── .streamlit/
│
├── src/
│   │
│   ├── components/
│   │   ├── dialog_add_photos.py
│   │   ├── dialog_attencence_result.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendence.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── piplines/
│   │   ├── face_pipline.py
│   │   └── voice_pipline.py
│   │
│   ├── screen/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui/
│
├── .gitignore
├── app.py
└── requirements.txt
```

The project follows a modular architecture separating **UI components, database operations, AI pipelines, and user-specific screens**.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/gauravmanjhi09/snapclass-main.git

cd snapclass-main
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

SnapClass uses **Supabase** for cloud database functionality.

Configure the required Supabase credentials through Streamlit secrets.

Create:

```text
.streamlit/secrets.toml
```

Example:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

> ⚠️ **Never commit real API keys, passwords, or other sensitive credentials to GitHub.**

---

# ▶️ Run the Application

Start SnapClass using:

```bash
streamlit run app.py
```

The application will start locally and provide a Streamlit URL in the terminal.

---

# 🔄 Application Workflow

## 👨‍🏫 Teacher Workflow

```text
Login
  ↓
Teacher Dashboard
  ↓
Create Subject
  ↓
Share Join Code
  ↓
Enroll Students
  ↓
Start Attendance
  ↓
AI Recognition
  ↓
Attendance Result
```

## 👨‍🎓 Student Workflow

```text
Login
  ↓
Student Dashboard
  ↓
Join Subject
  ↓
Enrollment
  ↓
Attendance Session
  ↓
AI Identification
  ↓
Attendance Recorded
```

---

# 🧩 AI Pipelines

## 👁️ Face Recognition Pipeline

The face pipeline handles the computer-vision based attendance workflow.

```text
Input
  ↓
Face Detection
  ↓
Face Encoding
  ↓
Compare With Registered Faces
  ↓
Identify Student
  ↓
Record Attendance
```

Students can be enrolled using photos, which are then used as registered facial information during the attendance process.

---

## 🎤 Voice Pipeline

SnapClass also contains a dedicated voice-processing pipeline.

```text
Voice Input
     ↓
Audio Processing
     ↓
Feature Extraction
     ↓
Speaker Representation
     ↓
Matching / Identification
     ↓
Attendance Workflow
```

Having both visual and audio pipelines makes SnapClass a **multi-modal AI attendance project** rather than a traditional attendance management application.

---

# 💡 Why SnapClass?

Traditional classroom attendance can be:

* ⏳ Time-consuming
* 📝 Manual
* 🔁 Repetitive
* ❌ Prone to human error
* 📋 Difficult to manage for larger classrooms

SnapClass addresses this by combining:

**AI + Automation + Cloud Database + Classroom Management**

into one application.

### 🎯 Goal

> **Reduce the time spent taking attendance so teachers can focus more on teaching.**

---

# 🔮 Future Improvements

Potential improvements for future versions include:

* 📊 Advanced attendance analytics
* 📈 Attendance trends and visualizations
* 📤 CSV / Excel attendance export
* 📅 Automated attendance reports
* 🔔 Attendance notifications
* 🛡️ Face anti-spoofing / liveness detection
* 📱 Improved mobile responsiveness
* ☁️ Scalable cloud deployment
* 👥 Better support for large classrooms

---

# 🎓 What I Learned

Building SnapClass provided hands-on experience with:

* Building interactive applications using **Streamlit**
* Implementing **computer vision workflows**
* Working with **face recognition**
* Processing **audio data**
* Implementing **speaker recognition**
* Integrating **Supabase** as a cloud database
* Designing teacher and student workflows
* Implementing authentication and session management
* Structuring a modular Python application
* Connecting AI pipelines with a real-world problem

---

# 🚀 Future Vision

SnapClass can be extended beyond attendance into a broader **AI-powered classroom management platform**, with features such as analytics, automated reports, student insights, and intelligent classroom assistance.

---

# 👨‍💻 Author

### Gaurav Manjhi

**BSc Computer Science | AI/ML Developer**

GitHub:
https://github.com/gauravmanjhi09

---

# ⭐ Support

If you find SnapClass interesting, consider giving the repository a ⭐.

It helps support the project and encourages further development.

---

## 📄 License

This project is developed for **educational and portfolio purposes**.
