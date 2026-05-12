import streamlit as st
import plotly.express as px
from google import genai

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import match_resume

# ---------------- GEMINI API ----------------
GEMINI_API_KEY = "AIzaSyA32022lwlplavYMdT-Ctes4pOdWsAwwuI"

client = genai.Client(api_key=GEMINI_API_KEY)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI ATS Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #00f5d4;
    margin-bottom: 0;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #d1d5db;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Metric Cards */
.metric-card {
    background: rgba(0, 245, 212, 0.08);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 15px;
    border: none;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(to right, #00f5d4, #00bbf9);
    color: black;
}

/* Download Button */
.stDownloadButton>button {
    width: 100%;
    border-radius: 15px;
    border: none;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(to right, #ff006e, #8338ec);
    color: white;
}

/* Matching Skill Tags */
.match-tag {
    display: inline-block;
    background: #00f5d4;
    color: black;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-weight: bold;
}

/* Missing Skill Tags */
.missing-tag {
    display: inline-block;
    background: #ff006e;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.3);
}

/* Progress Bar */
.stProgress > div > div > div > div {
    background-color: #00f5d4;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 class='main-title'>🤖 AI ATS Resume Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Analyze resumes according to job descriptions using Gemini AI</p>",
    unsafe_allow_html=True
)

# ---------------- LOAD SKILLS ----------------
with open("data/skills_list.txt") as f:
    skills_list = f.read().splitlines()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 About Project")

st.sidebar.info("""
✅ ATS Resume Analysis  
✅ AI Feedback using Gemini  
✅ Skill Matching  
✅ Missing Skill Detection  
✅ Resume Score Analysis  
✅ Interactive Charts  
""")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

# ---------------- JOB DESCRIPTION ----------------
job_desc = st.text_area(
    "📝 Paste Job Description"
)

# ---------------- WARNING ----------------
if uploaded_file and not job_desc:
    st.warning("⚠️ Please paste the job description")

# ---------------- MAIN LOGIC ----------------
if uploaded_file and job_desc:

    # Extract resume text
    text = extract_text(uploaded_file)

    # Resume skills
    resume_skills = extract_skills(text, skills_list)

    # Job description skills
    job_skills = extract_skills(job_desc, skills_list)

    # Matching skills
    matching_skills = [
        skill for skill in resume_skills
        if skill in job_skills
    ]

    # Missing skills
    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    # ATS Match Score
    match_score = match_resume(text, job_desc)

    # Resume score
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

    # Skill Match Chart
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

    # ATS Score Chart
    with chart_col2:

        score_data = {
            "Category": ["ATS Score", "Remaining"],
            "Value": [score, 100 - score]
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

    # ---------------- SKILL DISPLAY ----------------
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


    # ---------------- SKILL GAP ANALYSIS ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Skill Gap Analysis")

    if job_skills:

        for skill in job_skills:

            # Skill present in resume
            if skill in resume_skills:

                st.write(f"✅ {skill}")
                st.progress(100)

            # Skill missing
            else:

                st.write(f"❌ {skill}")
                st.progress(15)

    else:
        st.warning("No job-related skills detected.")

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

    # ---------------- GEMINI AI FEEDBACK ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🤖 Gemini AI Feedback")

    with st.spinner("Analyzing Resume with Gemini AI..."):

        prompt = f"""
        You are an expert ATS Resume Analyzer and Hiring Assistant.

        Analyze the following resume according to the given job description.

        Resume:
        {text}

        Job Description:
        {job_desc}

        Provide:
        1. ATS compatibility analysis
        2. Missing important skills
        3. Resume strengths
        4. Resume weaknesses
        5. Suggestions to improve ATS score
        6. Final hiring recommendation

        Keep the response professional and easy to read.
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_feedback = response.text

        st.write(ai_feedback)

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

AI Feedback:
{ai_feedback}
"""

    st.download_button(
        "📥 Download ATS Report",
        report,
        file_name="ATS_Report.txt"
    )