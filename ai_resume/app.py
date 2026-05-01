import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import match_resume

# ✅ Page Config (must be at top)
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ✅ UI Header
st.markdown(
    "<h1 style='text-align: center;'>🤖 AI Resume Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Upload your resume and get smart insights instantly</p>",
    unsafe_allow_html=True
)

# ✅ Load skills list
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

# ✅ File Upload
uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])

# ✅ Job Description (optional)
job_desc = st.text_area("📌 Paste Job Description (optional)")

# ✅ Main Logic
if uploaded_file:
    text = extract_text(uploaded_file)

    # 🔍 Extract Skills
    skills = extract_skills(text, skills_list)

    st.subheader("📌 Extracted Skills")
    st.write(skills)

    # ❌ Missing Skills
    missing_skills = [skill for skill in skills_list if skill not in skills]

    st.subheader("❌ Missing Skills")
    st.write(missing_skills[:10])

    # 📊 Resume Score (basic logic)
    score = len(skills) * 5
    if score > 100:
        score = 100

    st.subheader("📊 Resume Score")
    st.write(f"{score}/100")

    # 🎯 Job Matching (if provided)
    if job_desc:
        match_score = match_resume(text, job_desc)

        st.subheader("🎯 Job Match Score")
        st.write(f"{match_score}%")

    # 💡 Suggestions
    st.subheader("💡 Suggestions")

    if "project" not in text.lower():
        st.write("❗ Add project section")

    if len(skills) < 5:
        st.write("❗ Add more skills")

    if "experience" not in text.lower():
        st.write("❗ Mention work experience")

    # 📥 Download Report
    report = f"""
Extracted Skills: {skills}

Missing Skills: {missing_skills}

Resume Score: {score}/100
"""

    st.download_button("📥 Download Report", report, file_name="resume_report.txt")