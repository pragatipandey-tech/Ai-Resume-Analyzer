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

/* Main Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Hide Streamlit Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Title */
.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #d1d5db;
    font-size: 20px;
    margin-top: 0;
    margin-bottom: 40px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Metrics */
.metric-card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #00C9FF, #92FE9D);
    color: black;
    font-size: 18px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
    padding: 12px;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
}

/* Download Button */
.stDownloadButton>button {
    width: 100%;
    background: linear-gradient(to right, #FC466B, #3F5EFB);
    color: white;
    font-size: 18px;
    border-radius: 15px;
    border: none;
    padding: 12px;
}

/* Skill Tags */
.skill-tag {
    display: inline-block;
    background: #00C9FF;
    color: black;
    padding: 8px 15px;
    margin: 5px;
    border-radius: 20px;
    font-weight: bold;
}

.missing-tag {
    display: inline-block;
    background: #ff4b4b;
    color: white;
    padding: 8px 15px;
    margin: 5px;
    border-radius: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 class='main-title'>🤖 AI Resume Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Analyze resumes with AI-powered insights</p>",
    unsafe_allow_html=True
)

# ---------------- LOAD SKILLS ----------------
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 About Project")

st.sidebar.info("""
This AI-powered system helps you:

✅ Extract resume skills  
✅ Find missing skills  
✅ Calculate resume score  
✅ Match with job descriptions  
✅ Improve resume quality  
""")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume",
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

    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h2>✅ Skills</h2>
            <h1>{len(skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h2>❌ Missing</h2>
            <h1>{len(missing_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h2>📊 Score</h2>
            <h1>{score}/100</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- SKILLS ----------------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("📌 Extracted Skills")

        for skill in skills:
            st.markdown(
                f"<span class='skill-tag'>{skill}</span>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("❌ Missing Skills")

        for skill in missing_skills[:10]:
            st.markdown(
                f"<span class='missing-tag'>{skill}</span>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- JOB MATCH ----------------
    if job_desc:
        match_score = match_resume(text, job_desc)

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🎯 Job Match Score")

        st.progress(int(match_score))

        st.markdown(
            f"<h2 style='text-align:center;'>{match_score}% Match</h2>",
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SUGGESTIONS ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

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
        st.success("✅ Your resume looks strong!")

    st.markdown("</div>", unsafe_allow_html=True)

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