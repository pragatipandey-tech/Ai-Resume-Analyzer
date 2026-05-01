import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import match_resume

# Load skills
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

st.title("🤖 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

job_desc = st.text_area("Paste Job Description")

if uploaded_file:
    text = extract_text(uploaded_file)

    skills = extract_skills(text, skills_list)
    st.subheader("📌 Extracted Skills")
    st.write(skills)

    missing_skills = [skill for skill in skills_list if skill not in skills]

    st.subheader("❌ Missing Skills")
    st.write(missing_skills[:10])  # limit output

    if job_desc:
        score = match_resume(text, job_desc)
        st.subheader("📊 Match Score")
        st.write(f"{score}%")

        if score < 50:
            st.warning("Improve your resume!")
        else:
            st.success("Good match!")