# 🤖 AI ATS Resume Analyzer

An AI-powered ATS (Applicant Tracking System) Resume Analyzer built using Streamlit, Gemini AI, NLP, and Machine Learning.

This project analyzes resumes according to a given job description and provides:

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
✅ Interactive Pie Charts  
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

### 5️⃣ Add Gemini API Key

Inside `app.py`:

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

Get API key from:

https://ai.google.dev/

---

### 6️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📈 How It Works

1. Upload Resume  
2. Paste Job Description  
3. NLP extracts resume skills  
4. ATS system compares skills with JD  
5. Calculates ATS Match Score  
6. Detects missing skills  
7. Gemini AI generates intelligent feedback  
8. Download ATS analysis report  

---

## 🤖 Gemini AI Features

- Resume Strength Analysis
- Resume Weakness Detection
- ATS Compatibility Analysis
- Hiring Recommendations
- Smart Resume Suggestions

---

## 📊 Analytics Included

- Skill Match Pie Chart
- ATS Score Chart
- Resume Metrics Dashboard

---

## 🌟 Future Improvements

- AI Resume Rewriting
- Interview Question Generator
- Multi-Resume Comparison
- Authentication System
- Cloud Deployment
- Resume Keyword Highlighting
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
