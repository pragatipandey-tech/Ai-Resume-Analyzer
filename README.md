# 🤖 AI ATS Resume Analyzer

An advanced AI-powered ATS (Applicant Tracking System) Resume Analyzer built using Streamlit, Gemini AI, NLP, and Machine Learning.

This application analyzes resumes according to a specific job description and provides intelligent ATS insights with a modern interactive dashboard UI.

---

# 🚀 Features

✅ Upload Resume (PDF/DOCX)  
✅ Job Description Based Analysis  
✅ ATS Resume Matching  
✅ Skill Extraction using NLP  
✅ Missing Skill Detection  
✅ Skill Gap Analysis  
✅ Interactive Analytics Charts  
✅ Resume Score Analysis  
✅ Gemini AI Feedback  
✅ AI Hiring Recommendations  
✅ Download ATS Report  
✅ Modern Animated Dashboard UI  
✅ Glassmorphism Design  
✅ Animated Gradient Background  
✅ Hover Animation Effects  
✅ Responsive Layout  

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Gemini AI API
- Plotly
- Scikit-learn
- NLP
- PyPDF2
- python-docx
- HTML/CSS
- Machine Learning

---

# 📁 Project Structure

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
│   ├── dashboard.png
│   ├── analytics.png
│   ├── skill_gap.png
│   ├── ai_feedback.png
│
├── .streamlit/
│   ├── secrets.toml
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-ats-resume-analyzer.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd ai-ats-resume-analyzer
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Additional Packages

```bash
pip install plotly google-genai
```

---

# 🔐 Gemini API Setup

Create a file:

```text
.streamlit/secrets.toml
```

Add this inside:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Get Gemini API key from:

https://ai.google.dev/

---

# 🔒 Protect API Key

Create `.gitignore` file:

```text
.streamlit/secrets.toml
```

This prevents your secret API key from being uploaded to GitHub.

---

# ▶️ Run Application

```bash
streamlit run app.py
```

OR

```bash
python -m streamlit run app.py
```

---

# 📈 How It Works

1. Upload Resume  
2. Paste Job Description  
3. NLP extracts resume skills  
4. ATS compares resume with job description  
5. Calculates ATS Match Score  
6. Detects missing skills  
7. Performs Skill Gap Analysis  
8. Generates analytics charts  
9. Gemini AI generates intelligent feedback  
10. Download ATS analysis report  

---

# 🤖 Gemini AI Features

- ATS Compatibility Analysis
- Resume Strength Detection
- Resume Weakness Detection
- Missing Skill Suggestions
- Hiring Recommendations
- Smart Resume Feedback
- Resume Improvement Suggestions

---

# 📊 Analytics Included

- Skill Match Pie Chart
- ATS Score Analysis
- Resume Metrics Dashboard
- Skill Gap Analysis
- Progress Indicators
- Interactive Visualizations

---

# 🎨 UI Features

- Animated Gradient Background
- Glassmorphism Cards
- Neon AI Theme
- Hover Animation Effects
- Responsive Dashboard
- Interactive UI Components
- Modern Sidebar Design
- Smooth Visual Experience

---

# 📸 Dashboard Preview

## 🏠 Main Dashboard

![Dashboard](images/dashboard.png)

---

## 📊 ATS Analytics

![Analytics](images/analytics.png)

---

## 🧠 Skill Gap Analysis

![Skill Gap](images/skill_gap.png)

---

## 🤖 Gemini AI Feedback

![AI Feedback](images/ai_feedback.png)

---

# 🌟 Future Improvements

- AI Resume Rewriting
- AI Interview Question Generator
- Resume Keyword Highlighting
- Multi-Resume Comparison
- Authentication System
- Cloud Deployment
- Dark/Light Mode Toggle
- Circular ATS Score Meter
- AI Career Recommendations

---

# 📬 Contact

If you like this project, consider giving it a ⭐ on GitHub.

Feel free to contribute or suggest improvements.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
🚀 Share with others  

---

# 🔥 Project Highlights

- Real AI Integration using Gemini API
- ATS Resume Scoring System
- NLP-based Skill Extraction
- Interactive Data Visualization
- Modern AI Dashboard UI
- Real-time Resume Analysis
- Professional Portfolio Project

