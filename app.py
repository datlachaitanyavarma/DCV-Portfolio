import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Datla Chaitanya Varma | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; color: #1E88E5; margin-bottom: 0px; }
    .sub-header { font-size: 1.5rem; font-style: italic; color: #555555; margin-top: 0px;}
    .section-header { font-size: 1.8rem; font-weight: bold; color: #0D47A1; border-bottom: 2px solid #0D47A1; padding-bottom: 5px; margin-top: 30px;}
    .contact-info { font-size: 1.1rem; }
    .skill-tag { display: inline-block; background-color: #E3F2FD; color: #0D47A1; padding: 5px 12px; border-radius: 15px; margin: 4px; font-weight: 500;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (CONTACT & LINKS) ---
with st.sidebar:
    st.image("Profile.png", width=150) # Placeholder profile icon
    st.markdown("### Contact Me")
    st.markdown("📍 **Location:** Visakhapatnam, India")
    st.markdown("📞 **Phone:** +91 8331936129")
    st.markdown("📧 **Email:** [chaitanyavarma6129@gmail.com](mailto:chaitanyavarma6129@gmail.com)")
    
    st.markdown("### Languages")
    st.write("🗣️ English, Telugu, Hindi")
    
    st.markdown("### Interests")
    st.write("🎨 Graphic Designing")
    st.write("✍️ Story Writing")
    st.write("🤝 Volunteering")
    st.write("💻 Exploring Digital Tools")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">DATLA CHAITANYA VARMA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Digital Marketer & Social Media Manager</p>', unsafe_allow_html=True)

# --- OBJECTIVE ---
st.markdown('<p class="section-header">Objective</p>', unsafe_allow_html=True)
st.write("""
Creative Digital Marketing professional skilled in social media management, Canva designing, SEO fundamentals, 
and digital storytelling. Seeking to contribute practical marketing skills and creative strategies to a growth-oriented organization.
""")

# --- EXPERIENCE ---
st.markdown('<p class="section-header">Professional Experience</p>', unsafe_allow_html=True)

with st.container():
    st.subheader("Social Media Manager - Entertainment Pages")
    st.markdown("*Freelance | 3+ Years*")
    st.write("- Handled entertainment-based & Education Consultancy social media pages and gained strong understanding of platform algorithms.")
    st.write("- Practiced Google Ads and Meta Ads campaign execution for reach and engagement growth.")

with st.container():
    st.subheader("Digital Marketing Executive (Part-Time) & Trainer")
    st.markdown("*GloLED | 3 Months*")
    st.write("- Managed SEO audits, keyword research, Canva designing, posters, thumbnails, and social media posting.")
    st.write("- Delivered practical digital marketing training for 30+ students through live campaigns.")

with st.container():
    st.subheader("Digital Marketing Intern")
    st.markdown("*Lomaa IT Solutions Pvt. Ltd.*")
    st.write("- Learnt SEO, keyword research, competitor analysis, and social media strategy.")

with st.container():
    st.subheader("Cybersecurity Intern")
    st.markdown("*Palo Alto Networks*")
    st.write("- Understood cyber threats, hacking types, and data security measures.")

# --- SKILLS ---
st.markdown('<p class="section-header">Key Skills</p>', unsafe_allow_html=True)

st.markdown("#### Technical & Marketing")
tech_skills = ["SEO", "Social Media Management (SMM)", "Canva & Thumbnail Designing", "Content Creation", "Keyword Research", "MS Office"]
for skill in tech_skills:
    st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

st.markdown("#### Professional Skills")
prof_skills = ["Digital Storytelling", "Communication", "Team Coordination", "Leadership"]
for skill in prof_skills:
    st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# --- EDUCATION ---
st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("🎓 **MCA (Pursuing)**")
    st.write("*Noble Institute of Science & Technology, Visakhapatnam*")
    st.write("*(Affiliated to Andhra University)* | 2024-2026")
with col2:
    st.markdown("🎓 **B.Com**")
    st.write("*Adarsh Degree College, Visakhapatnam*")
    st.write("*(Affiliated to Andhra University)* | 2021-2024")

# --- VOLUNTEER EXPERIENCE ---
st.markdown('<p class="section-header">Volunteer Experience</p>', unsafe_allow_html=True)
st.write("**Vizag Volunteers Association (NGO)** | *Visakhapatnam (2022-Present)*")
st.write("- Supported Beach Clean-up, Giri Pradakshina, Navy Marathon's & Blood Donation Drives.")
st.write("- Served as a **Zone Lead**, managing and guiding large volunteer groups.")
st.write("- 🏆 Received **All-Rounder Award** for contribution in major events.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>Built with Python & Streamlit by Datla Chaitanya Varma</p>", unsafe_allow_html=True)
