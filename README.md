# 🤖 AI ATS Resume Analyzer

An AI-powered ATS (Applicant Tracking System) Resume Analyzer built using Streamlit, Gemini AI, NLP, and Machine Learning

This application analyzes resumes according to a specific job description and provides:

- ATS Match Score
- Matching Skills
- Missing Skills
- AI-Powered Resume Feedback
- Resume Analytics Charts
- Hiring Recommendations

---

## 🚀 Features

✅ Upload Resume (PDF/DOCX)  
✅ Job Description Based Analysis  
✅ ATS Resume Matching  
✅ Skill Extraction using NLP  
✅ Missing Skill Detection  
✅ Interactive Analytics Charts  
✅ Resume Score Analysis  
✅ Gemini AI Feedback  
✅ AI Hiring Recommendations  
✅ Download ATS Report  

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Gemini AI API
- Plotly
- Scikit-learn
- NLP
- PyPDF2
- python-docx

---

## 📁 Project Structure

```text
ai_ats_resume_analyzer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── utils/
│   ├── parser.py
│   ├── skills.py
│   ├── matcher.py
│
├── data/
│   ├── skills_list.txt
│
├── images/
│   ├── screenshot.png
│
├── .streamlit/
│   ├── secrets.toml
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-ats-resume-analyzer.git
```

---

### 2️⃣ Navigate to Project Folder

```bash
cd ai-ats-resume-analyzer
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Additional Packages

```bash
pip install plotly google-genai
```

---

## 🔐 Gemini API Setup

### Create `.streamlit/secrets.toml`

```toml
GEMINI_API_KEY = "AIzaxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Get Gemini API key from:

https://ai.google.dev/

---

## 🔒 Protect API Key

Create `.gitignore` file:

```text
.streamlit/secrets.toml
```

This prevents your secret API key from being uploaded to GitHub.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📈 How It Works

1. Upload Resume  
2. Paste Job Description  
3. NLP extracts resume skills  
4. ATS compares resume with job description  
5. Calculates ATS Match Score  
6. Detects missing skills  
7. Gemini AI generates intelligent feedback  
8. Download ATS analysis report  

---

## 🤖 Gemini AI Features

- ATS Compatibility Analysis
- Resume Strength Detection
- Resume Weakness Detection
- Missing Skill Suggestions
- Hiring Recommendations
- Smart Resume Feedback

---

## 📊 Analytics Included

- Skill Match Pie Chart
- ATS Score Chart
- Resume Metrics Dashboard

---

## 🌟 Future Improvements

- AI Resume Rewriting
- Interview Question Generator
- Resume Keyword Highlighting
- Multi-Resume Comparison
- Authentication System
- Cloud Deployment
- Dark/Light Mode Toggle

---

## 📬 Contact

If you like this project, consider giving it a ⭐ on GitHub.
Feel free to contribute or suggest improvements.

---

## ⭐ Support

If you found this project useful:
⭐ Star the repository  
🍴 Fork the project  
🚀 Share with others
