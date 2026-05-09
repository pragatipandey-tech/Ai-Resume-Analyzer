import streamlit as st
import plotly.express as px
from google import genai

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import match_resume

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI ATS Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
    margin-bottom: 0;
}

/* Subtitle */
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

/* Metric Cards */
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

/* Missing Skill Tags */
.missing-tag {
    display: inline-block;
    background: #ff4b4b;
    color: white;
    padding: 8px 15px;
    margin: 5px;
    border-radius: 20px;
    font-weight: bold;
}

/* Matching Skill Tags */
.match-tag {
    display: inline-block;
    background: #4ade80;
    color: black;
    padding: 8px 15px;
    margin: 5px;
    border-radius: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 class='main-title'>🤖 AI ATS Resume Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Analyze resumes according to job descriptions using AI-powered ATS logic</p>",
    unsafe_allow_html=True
)

# ---------------- LOAD SKILLS ----------------
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 About ATS Analyzer")

st.sidebar.info("""
This AI ATS system helps you:

✅ Analyze resume for a specific job  
✅ Detect matching skills  
✅ Detect missing skills  
✅ Calculate ATS match score  
✅ Improve resume quality  
""")

# ---------------- INPUTS ----------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

job_desc = st.text_area(
    "📝 Paste Job Description"
)

# ---------------- VALIDATION ----------------
if uploaded_file and not job_desc:
    st.warning("⚠️ Please paste the job description")

# ---------------- MAIN LOGIC ----------------
if uploaded_file and job_desc:

    # Extract Resume Text
    text = extract_text(uploaded_file)

    # Extract Resume Skills
    resume_skills = extract_skills(text, skills_list)

    # Extract Job Skills
    job_skills = extract_skills(job_desc, skills_list)

    # Matching Skills
    matching_skills = [
        skill for skill in resume_skills
        if skill in job_skills
    ]

    # Missing Skills
    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    # ATS Match Score
    match_score = match_resume(text, job_desc)

    # Resume Score
    score = len(matching_skills) * 10

    if score > 100:
        score = 100

    # ---------------- METRICS ----------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>📌 Resume Skills</h3>
            <h1>{len(resume_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>✅ Matching Skills</h3>
            <h1>{len(matching_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>❌ Missing Skills</h3>
            <h1>{len(missing_skills)}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>🎯 ATS Score</h3>
            <h1>{score}/100</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- PIE CHARTS ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Resume Analytics")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        pie_data = {
            "Category": ["Matching Skills", "Missing Skills"],
            "Count": [len(matching_skills), len(missing_skills)]
        }

        fig1 = px.pie(
            pie_data,
            names="Category",
            values="Count",
            title="Skill Match Analysis",
            hole=0.4
        )

        fig1.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with chart_col2:

        score_data = {
            "Category": ["ATS Score", "Remaining"],
            "Value": [score, 100-score]
        }

        fig2 = px.pie(
            score_data,
            names="Category",
            values="Value",
            title="ATS Score Analysis",
            hole=0.4
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SKILLS SECTION ----------------
    col1, col2 = st.columns(2)

    # Matching Skills
    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("✅ Matching Skills")

        if matching_skills:
            for skill in matching_skills:
                st.markdown(
                    f"<span class='match-tag'>{skill}</span>",
                    unsafe_allow_html=True
                )
        else:
            st.warning("No matching skills found")

        st.markdown("</div>", unsafe_allow_html=True)

    # Missing Skills
    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.markdown(
                    f"<span class='missing-tag'>{skill}</span>",
                    unsafe_allow_html=True
                )
        else:
            st.success("No missing skills")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- MATCH SCORE ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🎯 ATS Match Score")

    st.progress(int(match_score))

    st.markdown(
        f"<h2 style='text-align:center;'>{match_score}% Match</h2>",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SUGGESTIONS ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("💡 ATS Suggestions")

    suggestions = []

    if missing_skills:
        suggestions.append(
            f"Add these skills: {', '.join(missing_skills[:5])}"
        )

    if "project" not in text.lower():
        suggestions.append("Add project section")

    if "experience" not in text.lower():
        suggestions.append("Mention work experience")

    if len(resume_skills) < 5:
        suggestions.append("Add more technical skills")

    if suggestions:
        for suggestion in suggestions:
            st.warning(f"❗ {suggestion}")
    else:
        st.success("✅ Excellent ATS-compatible resume!")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- DOWNLOAD REPORT ----------------
    report = f"""
AI ATS Resume Analyzer Report

Resume Skills:
{resume_skills}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

ATS Match Score:
{match_score}%

Resume Score:
{score}/100
"""

    st.download_button(
        "📥 Download ATS Report",
        report,
        file_name="ATS_Report.txt"
    )