import streamlit as st
import yaml
from pathlib import Path

# ===== LOAD DATA =====
with open("data.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

RESUME_FILE = data.get("resume", "resume.pdf")

# ===== PAGE CONFIG =====
st.set_page_config(page_title=data["name"], layout="wide")

# ===== CUSTOM CSS =====
st.markdown("""
    <style>
    .section-header {
        background-color: #008080;  /* teal banner */
        color: white;
        padding: 10px 15px;
        border-radius: 8px;
        font-size: 20px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }
        /* General text spacing */
    h1, h2, h3, h4, h5, h6 {
        margin-top: 5px !important;
        margin-bottom: 5px !important;
    }

    p, li {
        margin-top: 0px !important;
        margin-bottom: 4px !important;
        font-size: 16px !important;
        line-height: 1.4em !important;
    }

    /* Section headers */
    .section-header {
        background-color: #008080;
        color: white;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    /* Divider lines */
    hr {
        margin: 4px 0 !important;
        border-top: 1px solid #ddd;
    }

    </style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
if "profile_image" in data:
    st.sidebar.image(data["profile_image"], width=180)

st.sidebar.title(data["name"])
st.sidebar.markdown(data["title"])
st.sidebar.markdown(f"📧 {data['email']}")
st.sidebar.markdown(f"📞 {data['phone']}")
st.sidebar.markdown(f"📍 {data['location']}")


# Resume download
if Path(RESUME_FILE).exists():
    with open(RESUME_FILE, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.sidebar.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=f"{data['name']} Resume.pdf",
        mime="application/pdf",
    )

# ===== ABOUT =====
st.markdown("<div class='section-header'>👋 About Me</div>", unsafe_allow_html=True)
st.write(data["about"])

# ===== WORK EXPERIENCE =====
if "employment" in data:
    st.markdown("<div class='section-header'>💼 Work Experience</div>", unsafe_allow_html=True)
    for job in data["employment"]:
        st.write(f"**{job['role']}** {job['company']} ({job['years']})")
        st.write(job["details"])
        st.markdown("---")

# ===== SKILLS =====
if "skills" in data:
    st.markdown("<div class='section-header'>🛠 Skills</div>", unsafe_allow_html=True)
    for skill in data["skills"]:
        st.write(f"**{skill['name']}**")
        st.progress(int(skill["level"]))

# ===== EDUCATION =====
if "education" in data:
    st.markdown("<div class='section-header'>🎓 Education</div>", unsafe_allow_html=True)
    for edu in data["education"]:
        st.write(f"**{edu['degree']}** {edu['school']} ({edu['years']})")

# ===== KEY ACHIEVEMENTS  =====
if "achievements" in data:
    st.markdown("<div class='section-header'>🚀 achievements</div>", unsafe_allow_html=True)
    for achievement in data["achievements"]:
        st.write(f"**{achievement['name']}** ({achievement['description']})")

# ===== CERTIFICATIONS =====
if "certifications" in data:
    st.markdown("<div class='section-header'>📜 Certifications</div>", unsafe_allow_html=True)
    for cert in data["certifications"]:
        st.write(f"- {cert['name']}")

# ============ TRAININGS ============
if "trainings" in data:
    st.markdown("<div class='section-header'>📚 Trainings</div>", unsafe_allow_html=True)
    for t in data["trainings"]:
        st.write(f"{t['name']} ({t['year']})")
    st.markdown("<hr>", unsafe_allow_html=True)

# ============ STRENGTHS ============
if "strengths" in data:
    st.markdown("<div class='section-header'>💡 Strengths</div>", unsafe_allow_html=True)
    for s in data["strengths"]:
        st.write(f"- {s}")
    st.markdown("<hr>", unsafe_allow_html=True)

# ============ AWARDS ============
if "awards" in data:
    st.markdown("<div class='section-header'>🏆 Awards</div>", unsafe_allow_html=True)
    for a in data["awards"]:
        st.write(f"**{a['name']}** ({a['year']})")
    st.markdown("<hr>", unsafe_allow_html=True)

# ============ FIND ME ONLINE ============
if "find_me_online" in data:
    st.markdown("<div class='section-header'>🌍 Find Me Online</div>", unsafe_allow_html=True)

    logos = {
        "LinkedIn": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
        "GitHub": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
        "Twitter": "https://cdn-icons-png.flaticon.com/512/733/733579.png",
        "Personal Website": "https://cdn-icons-png.flaticon.com/512/841/841364.png",
        "Facebook": "https://cdn-icons-png.flaticon.com/512/733/733547.png",
        "Instagram": "https://cdn-icons-png.flaticon.com/512/2111/2111463.png",
         "TikTok": "https://cdn-icons-png.flaticon.com/512/3046/3046121.png",
        "YouTube": "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"
    }

    cols = st.columns(len(data["find_me_online"]))  # arrange logos in one row

    for idx, link in enumerate(data["find_me_online"]):
        logo_url = logos.get(link["platform"], "https://cdn-icons-png.flaticon.com/512/25/25231.png")
        with cols[idx]:
            st.markdown(
                f"""
                <a href="{link['url']}" target="_blank">
                    <img src="{logo_url}" width="40">
                </a>
                """,
                unsafe_allow_html=True,
            )

# ===== PROJECTS =====
# if "projects" in data:
#     st.markdown("<div class='section-header'>🚀 Projects</div>", unsafe_allow_html=True)
#     for project in data["projects"]:
#         st.subheader(project["title"])
#         st.write(project["description"])
#         st.markdown("---")



# ===== FOOTER =====
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #008080;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #e5e7eb;
    }
    </style>
    <div class="footer">
        © 2025 Alex Daireck Banda
    </div>
""", unsafe_allow_html=True)
