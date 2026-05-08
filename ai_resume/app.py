import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import match_resume

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: white;
    text-align: center;
}

h3 {
    color: #00ADB5;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #00ADB5;
    color: white;
    font-size: 18px;
    border: none;
}

.stDownloadButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #222831;
    color: white;
    font-size: 16px;
}

.css-1d391kg {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>🤖 AI Resume Analyzer</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:gray;'>Upload your resume and get AI-powered insights instantly</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- LOAD SKILLS ----------------
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 About")
st.sidebar.info(
    """
    AI Resume Analyzer helps you:
    
    ✅ Extract Skills  
    ✅ Detect Missing Skills  
    ✅ Calculate Resume Score  
    ✅ Match with Job Description  
    """
)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📄 Upload Your Resume",
    type=["pdf", "docx"]
)

job_desc = st.text_area(
    "📝 Paste Job Description (Optional)"
)

# ---------------- MAIN LOGIC ----------------
if uploaded_file:

    text = extract_text(uploaded_file)

    # Extract skills
    skills = extract_skills(text, skills_list)

    # Missing skills
    missing_skills = [
        skill for skill in skills_list if skill not in skills
    ]

    # Resume score
    score = len(skills) * 5
    if score > 100:
        score = 100

    # ---------------- METRICS ----------------
    col1, col2, col3 = st.columns(3)

    col1.metric("✅ Skills Found", len(skills))
    col2.metric("❌ Missing Skills", len(missing_skills))
    col3.metric("📊 Resume Score", f"{score}/100")

    st.divider()

    # ---------------- SKILLS ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Extracted Skills")
        st.success(", ".join(skills))

    with col2:
        st.subheader("❌ Missing Skills")
        st.error(", ".join(missing_skills[:10]))

    st.divider()

    # ---------------- JOB MATCHING ----------------
    if job_desc:
        match_score = match_resume(text, job_desc)

        st.subheader("🎯 Job Match Score")

        st.progress(int(match_score))

        st.write(f"### {match_score}% Match")

    st.divider()

    # ---------------- SUGGESTIONS ----------------
    st.subheader("💡 Suggestions")

    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add project section")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    if "experience" not in text.lower():
        suggestions.append("Mention work experience")

    if suggestions:
        for suggestion in suggestions:
            st.warning(f"❗ {suggestion}")
    else:
        st.success("Your resume looks strong!")

    st.divider()

    # ---------------- DOWNLOAD REPORT ----------------
    report = f"""
AI Resume Analyzer Report

Skills Found:
{skills}

Missing Skills:
{missing_skills}

Resume Score:
{score}/100
"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="resume_report.txt"
    )