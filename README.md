# 🤖 AI Resume Generator

An AI-powered resume generation tool that creates professional, tailored resumes based on user input — built with pure HTML, CSS, and JavaScript, with an AI backend for smart resume writing.

---

## ✨ Features

- 🎨 Modern dark UI with animated gradient background
- 🌀 Smooth scroll-triggered section reveal animations
- 🎯 Color-coded form sections for intuitive data entry
- 📊 Reading progress bar
- 📱 Fully responsive (mobile-friendly)
- ⚡ No external dependencies (no Bootstrap, no frameworks)
- 🤖 AI-generated professional resume content
- 📄 Clean, structured resume output ready to copy or export

---

## 📁 Project Structure

```
ai-resume-generator/
│
├── resume_writer_input.html    # Main input form (UI)
├── resume_output.html          # AI-generated resume display page
├── app.py                      # Flask backend — routes & AI API call (if applicable)
├── requirements.txt            # Python dependencies (if applicable)
└── README.md                   # Project documentation
```

---

## 📋 Form Sections

| Section | Fields |
|--------|--------|
| 👤 Personal Info | Full Name, Location, Email, Phone |
| 🔗 Online Presence | LinkedIn, GitHub, Portfolio |
| 🎯 Career Focus | Target Role, Years of Experience, Education |
| ⚡ Skills & Tools | Core Skills, Tools & Technologies |
| 🏆 Projects & Achievements | Projects, Certifications, Achievements |

---

## 🚀 Getting Started

### Prerequisites

No installations required for the frontend. Just a modern web browser.

### Run Locally (Frontend Only)

```bash
git clone https://github.com/your-username/ai-resume-generator.git
cd ai-resume-generator
open resume_writer_input.html
```

Or simply double-click the `resume_writer_input.html` file in your file explorer.

### Run with AI Backend (Flask)

#### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Set your API key

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key_here
```

#### 4. Run the app

```bash
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

---

## 🔑 Getting an API Key

- **Google Gemini:** https://aistudio.google.com/app/apikey
- **OpenAI:** https://platform.openai.com/api-keys
- **DeepSeek:** https://platform.deepseek.com/api_keys

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python, Flask *(optional)* |
| AI | Google Gemini / OpenAI / DeepSeek API |
| Fonts | Google Fonts — Syne (display) + DM Sans (body) |
| Animations | CSS Keyframes, IntersectionObserver API |

---

## 🧠 How It Works

1. User fills in their details across color-coded form sections
2. On submit, the data is sent to the AI backend as a structured prompt
3. The AI generates a professional, tailored resume
4. The output is displayed on the resume output page
5. User can copy, download, or generate again

---



## 🔮 Roadmap

- [x] Beautiful input UI with animations
- [x] AI-generated resume content
- [ ] PDF export of generated resume
- [ ] Multiple resume templates
- [ ] Live preview panel
- [ ] Save & load draft functionality
- [ ] Connect to LinkedIn for auto-fill
- [ ] ATS (Applicant Tracking System) score checker

---



> ⭐ If you found this project helpful, consider giving it a star on GitHub!
