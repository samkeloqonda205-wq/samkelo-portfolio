import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Samkelo Qonda | Data Analyst · Scientist · Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Styling
st.markdown("""
<style>
    :root {
        --bg: #080b12;
        --surface: #0e1320;
        --surface2: #141929;
        --accent: #00e5ff;
        --accent2: #7b61ff;
        --accent3: #ff6b6b;
        --gold: #ffd166;
        --green: #06d6a0;
        --text: #e8ecf4;
        --muted: #6b7592;
        --border: rgba(0,229,255,0.12);
        --glow: 0 0 40px rgba(0,229,255,0.15);
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html {
        scroll-behavior: smooth;
    }
    
    body, .main {
        background: var(--bg) !important;
        color: var(--text) !important;
        font-family: 'Outfit', sans-serif;
    }
    
    /* Hide Streamlit UI elements */
    .stDeployButton { display: none; }
    footer { display: none; }
    #MainMenu { display: none; }
    header { display: none; }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: rgba(0,229,255,0.2); border-radius: 3px; }
    
    /* Main container */
    .main {
        max-width: 100%;
        padding: 0 !important;
    }
    
    .stContainer {
        max-width: 100%;
        padding: 0 60px;
    }
    
    /* Text styling */
    h1, h2, h3 {
        color: var(--text) !important;
        font-family: 'Playfair Display', serif !important;
    }
    
    p, span, div {
        color: var(--text) !important;
    }
    
    /* Section styling */
    .section-header {
        display: flex;
        align-items: baseline;
        gap: 20px;
        margin-bottom: 60px;
        flex-wrap: wrap;
    }
    
    .section-num {
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: var(--accent);
        letter-spacing: 2px;
        flex-shrink: 0;
    }
    
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(30px, 4vw, 50px);
        font-weight: 700;
        line-height: 1.1;
        color: var(--text) !important;
    }
    
    .section-line {
        flex: 1;
        height: 1px;
        background: var(--border);
        margin-left: 20px;
        max-width: 200px;
    }
    
    /* Button styling */
    .btn-primary {
        display: inline-block;
        background: var(--accent);
        color: var(--bg) !important;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 14px;
        padding: 14px 28px;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.3s;
        box-shadow: 0 0 30px rgba(0,229,255,0.2);
        border: none;
    }
    
    .btn-primary:hover {
        background: #33eaff;
        transform: translateY(-2px);
        box-shadow: 0 0 50px rgba(0,229,255,0.4);
    }
    
    .btn-outline {
        display: inline-block;
        background: transparent;
        color: var(--text) !important;
        border: 1px solid rgba(232,236,244,0.18);
        font-family: 'Outfit', sans-serif;
        font-weight: 500;
        font-size: 14px;
        padding: 14px 28px;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.3s;
    }
    
    .btn-outline:hover {
        border-color: var(--accent);
        color: var(--accent) !important;
        transform: translateY(-2px);
    }
    
    /* Cards */
    .card {
        background: var(--surface2);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 36px;
        transition: all 0.4s;
        position: relative;
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-6px);
        border-color: rgba(0,229,255,0.25);
        box-shadow: 0 0 40px rgba(0,229,255,0.15);
    }
    
    .card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s;
    }
    
    .card:hover::after {
        transform: scaleX(1);
    }
    
    /* Skill chips */
    .skill-chip {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        padding: 4px 12px;
        border-radius: 5px;
        letter-spacing: 0.5px;
        border: 1px solid;
        display: inline-block;
        margin: 3px 3px;
        transition: all 0.2s;
    }
    
    .chip-c {
        color: var(--accent);
        border-color: rgba(0,229,255,0.2);
        background: rgba(0,229,255,0.05);
    }
    
    .chip-p {
        color: var(--accent2);
        border-color: rgba(123,97,255,0.2);
        background: rgba(123,97,255,0.05);
    }
    
    .chip-g {
        color: var(--green);
        border-color: rgba(6,214,160,0.2);
        background: rgba(6,214,160,0.05);
    }
    
    .chip-o {
        color: var(--gold);
        border-color: rgba(255,209,102,0.2);
        background: rgba(255,209,102,0.05);
    }
    
    /* Project tech badge */
    .tech-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        padding: 4px 11px;
        border-radius: 5px;
        letter-spacing: 0.5px;
        border: 1px solid;
        display: inline-block;
        margin: 3px 3px;
    }
    
    .t-blue {
        background: rgba(0,229,255,0.06);
        color: var(--accent);
        border-color: rgba(0,229,255,0.18);
    }
    
    .t-purple {
        background: rgba(123,97,255,0.06);
        color: var(--accent2);
        border-color: rgba(123,97,255,0.18);
    }
    
    .t-red {
        background: rgba(255,107,107,0.06);
        color: var(--accent3);
        border-color: rgba(255,107,107,0.18);
    }
    
    .t-gold {
        background: rgba(255,209,102,0.06);
        color: var(--gold);
        border-color: rgba(255,209,102,0.18);
    }
    
    .t-green {
        background: rgba(6,214,160,0.06);
        color: var(--green);
        border-color: rgba(6,214,160,0.18);
    }
    
    /* Contact items */
    .contact-item {
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: var(--muted);
        margin: 10px 0;
    }
    
    .contact-item a {
        color: var(--accent);
        text-decoration: none;
    }
    
    .contact-item a:hover {
        text-decoration: underline;
    }
    
    /* Certificate card */
    .cert-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 24px 26px;
        display: flex;
        gap: 18px;
        align-items: flex-start;
        transition: all 0.3s;
        margin: 10px 0;
    }
    
    .cert-card:hover {
        border-color: rgba(0,229,255,0.28);
        transform: translateX(4px);
        background: var(--surface2);
    }
    
    .cert-icon {
        width: 44px;
        height: 44px;
        border-radius: 10px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    
    .ci-datacamp {
        background: linear-gradient(135deg, rgba(3,190,150,0.2), rgba(3,190,150,0.08));
        border: 1px solid rgba(3,190,150,0.25);
    }
    
    .ci-forage {
        background: linear-gradient(135deg, rgba(123,97,255,0.2), rgba(123,97,255,0.08));
        border: 1px solid rgba(123,97,255,0.25);
    }
    
    .ci-hp {
        background: linear-gradient(135deg, rgba(0,100,255,0.2), rgba(0,100,255,0.08));
        border: 1px solid rgba(0,100,255,0.25);
    }
    
    .ci-mtn {
        background: linear-gradient(135deg, rgba(255,209,102,0.2), rgba(255,209,102,0.08));
        border: 1px solid rgba(255,209,102,0.25);
    }
    
    .ci-yes {
        background: linear-gradient(135deg, rgba(255,180,50,0.2), rgba(255,180,50,0.08));
        border: 1px solid rgba(255,180,50,0.25);
    }
    
    .cert-name {
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 3px;
        color: var(--text);
    }
    
    .cert-issuer {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        color: var(--accent);
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    .cert-date {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        color: var(--muted);
    }
    
    .badge-verified {
        background: rgba(6,214,160,0.1);
        color: var(--green);
        border: 1px solid rgba(6,214,160,0.25);
        font-family: 'JetBrains Mono', monospace;
        font-size: 9px;
        letter-spacing: 1px;
        padding: 2px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        display: inline-block;
    }
    
    .badge-sim {
        background: rgba(123,97,255,0.1);
        color: var(--accent2);
        border: 1px solid rgba(123,97,255,0.25);
        font-family: 'JetBrains Mono', monospace;
        font-size: 9px;
        letter-spacing: 1px;
        padding: 2px 8px;
        border-radius: 4px;
        text-transform: uppercase;
        display: inline-block;
    }
    
    /* Experience card */
    .exp-card {
        background: var(--surface2);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 36px;
        position: relative;
        overflow: hidden;
        margin: 20px 0;
    }
    
    .exp-card::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(180deg, var(--accent), var(--accent2));
        border-radius: 3px 0 0 3px;
    }
    
    .exp-company {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 700;
        color: var(--text);
    }
    
    .exp-role {
        font-size: 14px;
        color: var(--accent);
        font-weight: 600;
        margin-bottom: 4px;
    }
    
    .exp-period {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: var(--accent);
        background: rgba(0,229,255,0.07);
        border: 1px solid rgba(0,229,255,0.15);
        padding: 4px 12px;
        border-radius: 6px;
        white-space: nowrap;
    }
    
    .exp-location {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: var(--muted);
        margin-bottom: 20px;
    }
    
    .exp-bullet {
        font-size: 14px;
        color: rgba(232,236,244,0.62);
        line-height: 1.7;
        padding-left: 20px;
        position: relative;
        margin: 8px 0;
    }
    
    .exp-bullet::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: var(--accent);
        font-size: 10px;
    }
    
    /* Social buttons */
    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 9px;
        padding: 14px 22px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: var(--muted);
        text-decoration: none;
        transition: all 0.3s;
        letter-spacing: 0.5px;
        margin: 8px 8px;
    }
    
    .social-btn:hover {
        color: var(--accent);
        border-color: rgba(0,229,255,0.3);
        background: rgba(0,229,255,0.05);
        transform: translateY(-3px);
    }
    
    /* Responsive */
    @media (max-width: 900px) {
        .stContainer {
            padding: 0 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hide sidebar
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================

st.markdown("""
<div style="padding: 130px 60px 90px; position: relative; z-index: 1;">
    <h1 style="font-family: 'Playfair Display', serif; font-size: 80px; font-weight: 900; line-height: 0.95; margin-bottom: 16px; color: #e8ecf4;">Samkelo<br><em style="font-style: italic; color: transparent; -webkit-text-stroke: 1.5px #00e5ff;">Qonda</em></h1>
    <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 28px;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 6px; letter-spacing: 1px; text-transform: uppercase; background: rgba(0,229,255,0.08); color: #00e5ff; border: 1px solid rgba(0,229,255,0.2);">Data Analyst</span>
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 6px; letter-spacing: 1px; text-transform: uppercase; background: rgba(123,97,255,0.08); color: #7b61ff; border: 1px solid rgba(123,97,255,0.2);">Data Scientist</span>
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 6px; letter-spacing: 1px; text-transform: uppercase; background: rgba(6,214,160,0.08); color: #06d6a0; border: 1px solid rgba(6,214,160,0.2);">Data Engineer</span>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <p style="font-size: 17px; color: rgba(232,236,244,0.6); line-height: 1.8; max-width: 580px; margin-bottom: 44px;">
        Detail-oriented data professional with <strong style="color:#e8ecf4;">DataCamp Associate certifications</strong> in Data Analysis, Data Science & Data Engineering. I turn raw data into insights — from SQL pipelines and Python models to interactive Tableau dashboards that drive real decisions.
    </p>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.markdown("""
        <a href="#projects" style="display: inline-flex; align-items: center; gap: 10px; background: #00e5ff; color: #080b12; font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 14px; padding: 14px 28px; border-radius: 8px; text-decoration: none; box-shadow: 0 0 30px rgba(0,229,255,0.2);">View My Projects</a>
        """, unsafe_allow_html=True)
    
    with col_btn2:
        st.markdown("""
        <a href="https://www.linkedin.com/in/samkelo-qonda-b14738270" target="_blank" style="display: inline-flex; align-items: center; gap: 10px; background: transparent; color: #e8ecf4; border: 1px solid rgba(232,236,244,0.18); font-family: 'Outfit', sans-serif; font-weight: 500; font-size: 14px; padding: 14px 28px; border-radius: 8px; text-decoration: none;">LinkedIn Profile</a>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 700; color: #00e5ff; display: block; line-height: 1; margin-bottom: 4px;">6+</div>
        <div style="font-size: 11px; color: #6b7592; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 20px;">Projects Built</div>
        
        <div style="font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 700; color: #00e5ff; display: block; line-height: 1; margin-bottom: 4px;">11</div>
        <div style="font-size: 11px; color: #6b7592; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'JetBrains Mono', monospace; margin-bottom: 20px;">Certifications</div>
        
        <div style="font-family: 'Playfair Display', serif; font-size: 38px; font-weight: 700; color: #00e5ff; display: block; line-height: 1; margin-bottom: 4px;">3</div>
        <div style="font-size: 11px; color: #6b7592; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'JetBrains Mono', monospace;">Jobs Held</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# ABOUT SECTION
# ============================================================================

st.markdown("""
<div id="about" style="padding: 100px 60px; border-bottom: 1px solid rgba(0,229,255,0.12);">
    <div class="section-header">
        <span class="section-num">01 /</span>
        <h2 class="section-title">About <em style="font-style: italic; color: transparent; -webkit-text-stroke: 1px rgba(232,236,244,0.35);">Me</em></h2>
    </div>
</div>
""", unsafe_allow_html=True)

col_about1, col_about2 = st.columns(2, gap="large")

with col_about1:
    st.markdown("""
    <p style="font-size: 16px; color: rgba(232,236,244,0.65); line-height: 1.85; margin-bottom: 16px;">
        I am <strong>Samkelo Qonda</strong>, a driven and detail-oriented <strong>Operations & Data Analyst</strong> based in <strong>Kempton Park, Gauteng</strong>. I bring hands-on experience in warehouse operations, inventory control, and logistics, combined with a strong analytical mindset and growing technical skills in Excel, Tableau, Power BI, SQL, and Python.
    </p>
    <p style="font-size: 16px; color: rgba(232,236,244,0.65); line-height: 1.85; margin-bottom: 16px;">
        I hold <strong>DataCamp Associate certifications</strong> in Data Analysis, Data Science, and Data Engineering (2026), complemented by real-world job simulations from globally recognised firms including <strong>JPMorgan Chase, Deloitte, Mastercard, Standard Chartered, AIG, and DLA Piper</strong> via Forage — covering quantitative research, analytics, cybersecurity, credit analysis, and data privacy.
    </p>
    <p style="font-size: 16px; color: rgba(232,236,244,0.65); line-height: 1.85; margin-bottom: 16px;">
        I am ambitious about transitioning into data-driven and technical roles where I can continuously learn, apply my operational experience, and contribute to improving business efficiency and performance.
    </p>
    
    st.markdown("""
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:20px;margin-bottom:8px;">
        <span style="font-family:'JetBrains Mono',monospace;font-size:10px;padding:4px 12px;border-radius:5px;background:rgba(0,229,255,0.07);color:#00e5ff;border:1px solid rgba(0,229,255,0.2);">🇬🇧 English — Fluent</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:10px;padding:4px 12px;border-radius:5px;background:rgba(123,97,255,0.07);color:#7b61ff;border:1px solid rgba(123,97,255,0.2);">🇿🇦 IsiXhosa — Native</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:10px;padding:4px 12px;border-radius:5px;background:rgba(6,214,160,0.07);color:#06d6a0;border:1px solid rgba(6,214,160,0.2);">🇿🇦 Afrikaans — Basic</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-item">
        📧 <a href="mailto:samkeloqonda@gmail.com">samkeloqonda@gmail.com</a>
    </div>
    <div class="contact-item">
        📞 068 256 7468
    </div>
    <div class="contact-item">
        📍 Kempton Park, Gauteng, South Africa
    </div>
    <div class="contact-item">
        💼 <a href="https://www.linkedin.com/in/samkelo-qonda-b14738270" target="_blank">linkedin.com/in/samkelo-qonda-b14738270</a>
    </div>
    <div class="contact-item">
        💻 <a href="https://github.com/samkeloqonda205-wq" target="_blank">github.com/samkeloqonda205-wq</a>
    </div>
    """, unsafe_allow_html=True)

with col_about2:
    st.markdown("""
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #00e5ff; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px;">Technical Skills</div>
    """, unsafe_allow_html=True)
    
    # Data & Analytics
    st.markdown("""
    <div style="margin-bottom: 28px;">
        <div style="font-size: 13px; font-weight: 600; color: #e8ecf4; margin-bottom: 10px;">Data & Analytics</div>
        <span class="skill-chip chip-c">Python</span><span class="skill-chip chip-c">Pandas</span><span class="skill-chip chip-c">NumPy</span>
        <span class="skill-chip chip-c">Matplotlib</span><span class="skill-chip chip-c">Seaborn</span>
        <span class="skill-chip chip-c">SQL</span><span class="skill-chip chip-c">PostgreSQL</span>
        <span class="skill-chip chip-c">Tableau</span><span class="skill-chip chip-c">Power BI</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Engineering
    st.markdown("""
    <div style="margin-bottom: 28px;">
        <div style="font-size: 13px; font-weight: 600; color: #e8ecf4; margin-bottom: 10px;">Data Engineering</div>
        <span class="skill-chip chip-p">ETL Pipelines</span><span class="skill-chip chip-p">Data Modeling</span>
        <span class="skill-chip chip-p">Data Cleaning</span><span class="skill-chip chip-p">Data Warehousing</span>
        <span class="skill-chip chip-p">CTEs & Subqueries</span><span class="skill-chip chip-p">Joins & Aggregations</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Tools & Systems
    st.markdown("""
    <div style="margin-bottom: 28px;">
        <div style="font-size: 13px; font-weight: 600; color: #e8ecf4; margin-bottom: 10px;">Tools & Systems</div>
        <span class="skill-chip chip-g">Excel (Advanced)</span><span class="skill-chip chip-g">Microsoft 365</span>
        <span class="skill-chip chip-g">SAP / ERP</span><span class="skill-chip chip-g">Syspro ERP</span>
        <span class="skill-chip chip-g">Power BI</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Skills
    st.markdown("""
    <div style="margin-bottom: 28px;">
        <div style="font-size: 13px; font-weight: 600; color: #e8ecf4; margin-bottom: 10px;">Professional Skills</div>
        <span class="skill-chip chip-o">Statistical Analysis</span><span class="skill-chip chip-o">KPI Reporting</span>
        <span class="skill-chip chip-o">Hypothesis Testing</span><span class="skill-chip chip-o">Data Storytelling</span>
        <span class="skill-chip chip-o">Financial Analysis</span><span class="skill-chip chip-o">Credit Analysis</span>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PROJECTS SECTION
# ============================================================================

st.markdown("""
<div id="projects" style="padding: 100px 60px; background: #0e1320; border-top: 1px solid rgba(0,229,255,0.12); border-bottom: 1px solid rgba(0,229,255,0.12);">
    <div class="section-header">
        <span class="section-num">02 /</span>
        <h2 class="section-title">Featured <em style="font-style: italic; color: transparent; -webkit-text-stroke: 1px rgba(232,236,244,0.35);">Projects</em></h2>
    </div>
</div>
""", unsafe_allow_html=True)

# British Airways Project
st.markdown("""
<div class="card" style="margin: 20px 60px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">🟣 Tableau · Customer Analytics</div>
    <h3 style="font-family: 'Playfair Display', serif; font-size: 26px; font-weight: 700; margin-bottom: 12px; line-height: 1.2; color: #e8ecf4;">British Airways Customer Review Analysis Dashboard</h3>
    <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Built an interactive Tableau dashboard analyzing thousands of British Airways customer reviews. Identified key satisfaction drivers, route performance gaps, and sentiment trends — enabling data-driven service improvements across cabin classes and routes.</p>
    <div style="margin-bottom: 22px;">
        <span class="tech-badge t-purple">Tableau</span>
        <span class="tech-badge t-purple">Dashboard Design</span>
        <span class="tech-badge t-blue">Sentiment Analysis</span>
        <span class="tech-badge t-blue">Data Visualization</span>
        <span class="tech-badge t-green">Customer Analytics</span>
    </div>
    <a href="https://github.com/samkeloqonda205-wq/British-Airways-Customer-Review-Analysis-Dashboard" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
</div>
""", unsafe_allow_html=True)

# Other Projects in grid
col_p1, col_p2 = st.columns(2, gap="small")

with col_p1:
    st.markdown("""
    <div class="card">
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">🌍 Python · Data Analysis</div>
        <h3 style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.2;">Global Life Expectancy Analysis</h3>
        <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Explored global health trends and socioeconomic correlations affecting life expectancy across countries, using Python EDA and advanced visualizations to uncover meaningful patterns.</p>
        <div style="margin-bottom: 22px;">
            <span class="tech-badge t-gold">Python</span>
            <span class="tech-badge t-gold">Pandas</span>
            <span class="tech-badge t-gold">Seaborn</span>
            <span class="tech-badge t-blue">EDA</span>
        </div>
        <a href="https://github.com/samkeloqonda205-wq/global-life-expectancy-analysis" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">🗄️ SQL · Data Engineering</div>
        <h3 style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.2;">SQL Data Cleaning — Nashville Housing</h3>
        <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Comprehensive data cleaning and transformation on the Nashville Housing dataset using advanced SQL: standardized date formats, populated null property addresses, split columns, removed duplicates, and delivered an analytics-ready dataset.</p>
        <div style="margin-bottom: 22px;">
            <span class="tech-badge t-red">SQL</span>
            <span class="tech-badge t-red">Data Cleaning</span>
            <span class="tech-badge t-red">SQL Server</span>
            <span class="tech-badge t-purple">CTEs</span>
            <span class="tech-badge t-purple">Window Functions</span>
        </div>
        <a href="https://github.com/samkeloqonda205-wq/SQL---Data-Cleaning-Nashville-Housing" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

with col_p2:
    st.markdown("""
    <div class="card">
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">📈 Quantitative Research · Python</div>
        <h3 style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.2;">Quantitative Research Python Project</h3>
        <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Applied quantitative methods from the JPMorgan Chase job simulation: investigated and analyzed price data, priced commodity storage contracts, performed credit risk analysis, and bucketed FICO scores using Python statistical modelling.</p>
        <div style="margin-bottom: 22px;">
            <span class="tech-badge t-blue">Python</span>
            <span class="tech-badge t-blue">NumPy</span>
            <span class="tech-badge t-blue">Statistical Modelling</span>
            <span class="tech-badge t-purple">Credit Risk</span>
            <span class="tech-badge t-green">FICO Analysis</span>
        </div>
        <a href="https://github.com/samkeloqonda205-wq/quantative-research-python" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">🏙️ Tableau · Market Analysis</div>
        <h3 style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.2;">Airbnb Price Analysis Dashboard</h3>
        <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Interactive Tableau dashboard dissecting Airbnb pricing dynamics by location, property type, bedroom count, and seasonal demand patterns.</p>
        <div style="margin-bottom: 22px;">
            <span class="tech-badge t-gold">Tableau</span>
            <span class="tech-badge t-gold">Price Analytics</span>
            <span class="tech-badge t-blue">Market Research</span>
        </div>
        <a href="https://github.com/samkeloqonda205-wq/Airbnb-Price-Analysis-Tableau-Dashboard" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card" style="margin: 20px 60px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #6b7592; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">📞 Data Analytics · Dashboard</div>
    <h3 style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; margin-bottom: 12px; line-height: 1.2;">ConnectTel Call Center Analysis</h3>
    <p style="font-size: 14px; color: rgba(232,236,244,0.52); line-height: 1.75; margin-bottom: 22px;">Data analysis and visualization project examining call center performance, agent efficiency, resolution rates and customer satisfaction trends.</p>
    <div style="margin-bottom: 22px;">
        <span class="tech-badge t-green">Data Analysis</span>
        <span class="tech-badge t-green">KPI Tracking</span>
        <span class="tech-badge t-blue">Visualization</span>
    </div>
    <a href="https://github.com/samkeloqonda205-wq/ConnectTel-Call-Center-Analysis" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #00e5ff; text-decoration: none; font-family: 'JetBrains Mono', monospace; font-weight: 600; letter-spacing: 1px;">View on GitHub →</a>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# CERTIFICATES SECTION
# ============================================================================

st.markdown("""
<div id="certificates" style="padding: 100px 60px; border-bottom: 1px solid rgba(0,229,255,0.12);">
    <div class="section-header">
        <span class="section-num">03 /</span>
        <h2 class="section-title">Certificates & <em style="font-style: italic; color: transparent; -webkit-text-stroke: 1px rgba(232,236,244,0.35);">Credentials</em></h2>
    </div>
    <p style="font-size: 15px; color: #6b7592; margin-bottom: 40px; max-width: 600px;">Certifications from industry-leading platforms and top global firms, spanning data engineering, analytics, quantitative research, cybersecurity, and professional development.</p>
</div>
""", unsafe_allow_html=True)

# Certificates data
certs = [
    ("🏆", "Associate Data Scientist", "DataCamp", "Apr 2026", "Verified"),
    ("⚙️", "Associate Data Engineer", "DataCamp", "Apr 2026", "Verified"),
    ("📊", "Associate Data Analyst", "DataCamp", "Feb 2026", "Verified"),
    ("🏦", "Quantitative Research Job Simulation", "JPMorgan Chase · Forage", "Mar 2026", "Simulation"),
    ("📈", "Data Analytics Job Simulation", "Deloitte · Forage", "Mar 2026", "Simulation"),
    ("🔐", "Cybersecurity Job Simulation", "Mastercard · Forage", "Mar 2026", "Simulation"),
    ("💳", "Credit Analyst Job Simulation", "Standard Chartered · Forage", "Mar 2026", "Simulation"),
    ("🛡️", "Actuarial Analyst Virtual Job Simulation", "AIG · Forage", "Mar 2026", "Simulation"),
    ("🌐", "Global Cyber with Data Privacy Job Simulation", "DLA Piper · Forage", "Mar 2026", "Simulation"),
    ("💻", "Data Science & Analytics", "HP LIFE Foundation", "Mar 2026", "Verified"),
    ("📁", "Managing Data with Microsoft 365", "MTN Skills Academy · LinkedIn Learning", "Mar 2026", "Verified"),
    ("🚀", "Work Readiness & Entrepreneurship Modules", "YES — Youth Employment Service", "Jan 2025", "Verified"),
]

cols = st.columns(3, gap="small")
for idx, cert in enumerate(certs):
    emoji, name, issuer, date, badge_type = cert
    col_idx = idx % 3
    
    badge_class = "badge-verified" if badge_type == "Verified" else "badge-sim"
    icon_class = "ci-datacamp" if "DataCamp" in issuer else "ci-forage" if "Forage" in issuer else "ci-hp" if "HP" in issuer else "ci-mtn" if "MTN" in issuer else "ci-yes"
    
    with cols[col_idx]:
        st.markdown(f"""
        <div class="cert-card">
            <div class="cert-icon {icon_class}">{emoji}</div>
            <div class="cert-info">
                <div class="cert-name">{name}</div>
                <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
                    <span class="cert-issuer">{issuer}</span>
                    <span class="cert-date">•</span>
                    <span class="cert-date">{date}</span>
                </div>
                <span class="{badge_class}">{badge_type}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# EXPERIENCE SECTION
# ============================================================================

st.markdown("""
<div id="experience" style="padding: 100px 60px; background: #0e1320; border-top: 1px solid rgba(0,229,255,0.12); border-bottom: 1px solid rgba(0,229,255,0.12);">
    <div class="section-header">
        <span class="section-num">04 /</span>
        <h2 class="section-title">Work <em style="font-style: italic; color: transparent; -webkit-text-stroke: 1px rgba(232,236,244,0.35);">Experience</em></h2>
    </div>
</div>
""", unsafe_allow_html=True)

# Experience 1
st.markdown("""
<div class="exp-card" style="margin: 20px 60px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; gap: 20px; flex-wrap: wrap;">
        <div>
            <div class="exp-company">Econofoods</div>
            <div class="exp-role">Warehouse Operator — Bulk</div>
            <div class="exp-location">📍 Longmeadow, Edenvale, Gauteng</div>
        </div>
        <div class="exp-period">May 2025 – Jan 2026</div>
    </div>
    <div>
        <div class="exp-bullet">Managed end-to-end inventory operations including receiving, storage, relocation, and dispatch in a high-volume FMCG environment.</div>
        <div class="exp-bullet">Performed daily cycle counts and full stock takes, reconciling physical vs system records to improve stock accuracy and reduce shrinkage.</div>
        <div class="exp-bullet">Utilized RF scanners and Warehouse Management Systems (WMS) to capture real-time inventory data and ensure system accuracy.</div>
        <div class="exp-bullet">Applied FIFO principles to manage perishable goods across bulk, chiller, and freezer storage, reducing waste and expired stock.</div>
        <div class="exp-bullet">Compiled weekly inventory reports highlighting variances, slow-moving stock, and operational risks for management decision-making.</div>
        <div class="exp-bullet">Supported internal and external audits through accurate documentation and stock validation.</div>
        <div class="exp-bullet">Optimized warehouse layout and bin accuracy to improve picking efficiency and workflow.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Experience 2
st.markdown("""
<div class="exp-card" style="margin: 20px 60px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; gap: 20px; flex-wrap: wrap;">
        <div>
            <div class="exp-company">Bosch Rexroth / Tectra Automation</div>
            <div class="exp-role">Storeman</div>
            <div class="exp-location">📍 Kempton Park, Gauteng</div>
        </div>
        <div class="exp-period">May 2024 – May 2025</div>
    </div>
    <div>
        <div class="exp-bullet">Managed stock receiving, issuing, and storage while ensuring accuracy in inventory records using Syspro ERP system.</div>
        <div class="exp-bullet">Coordinated logistics operations across sea, air, and road freight for timely delivery of goods.</div>
        <div class="exp-bullet">Prepared and maintained documentation for inventory tracking and audit purposes.</div>
        <div class="exp-bullet">Conducted routine stock counts and supported inventory reconciliation processes.</div>
        <div class="exp-bullet">Ensured compliance with warehouse safety standards through regular inspections and hazard reporting.</div>
        <div class="exp-bullet">Maintained an organized warehouse layout to improve accessibility and operational efficiency.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Experience 3
st.markdown("""
<div class="exp-card" style="margin: 20px 60px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; gap: 20px; flex-wrap: wrap;">
        <div>
            <div class="exp-company">Makro SA</div>
            <div class="exp-role">Cashier</div>
            <div class="exp-location">📍 Gauteng</div>
        </div>
        <div class="exp-period">Sep 2023 – Nov 2023</div>
    </div>
    <div>
        <div class="exp-bullet">Processed high-volume transactions accurately using POS systems, handling cash, card, and digital payments.</div>
        <div class="exp-bullet">Maintained balanced cash drawers and completed daily financial reconciliations.</div>
        <div class="exp-bullet">Delivered excellent customer service by resolving queries, handling returns, and assisting with product information.</div>
        <div class="exp-bullet">Monitored stock levels at checkout points and communicated replenishment needs to the team.</div>
        <div class="exp-bullet">Collaborated with team members to maintain efficient service flow in a fast-paced retail environment.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# CONTACT SECTION
# ============================================================================

st.markdown("""
<div id="contact" style="padding: 120px 60px; text-align: center; border-top: 1px solid rgba(0,229,255,0.12);">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #00e5ff; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;">Let's connect</div>
    <h2 style="font-family: 'Playfair Display', serif; font-size: 76px; font-weight: 900; line-height: 1.05; margin-bottom: 18px; color: #e8ecf4;">Open to <em style="font-style: italic; color: transparent; -webkit-text-stroke: 1.5px #00e5ff;">Opportunities</em></h2>
    <p style="font-size: 16px; color: #6b7592; margin-bottom: 50px;">Data Analyst · Data Scientist · Data Engineer roles in Gauteng or remote. Let's talk.</p>
</div>
""", unsafe_allow_html=True)

# Contact buttons
col_c1, col_c2, col_c3, col_c4, col_c5 = st.columns(5, gap="small")

with col_c1:
    st.markdown("""
    <a href="mailto:samkeloqonda@gmail.com" class="social-btn" style="width: 100%; text-align: center;">
        📧 Email
    </a>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <a href="https://www.linkedin.com/in/samkelo-qonda-b14738270" target="_blank" class="social-btn" style="width: 100%; text-align: center;">
        💼 LinkedIn
    </a>
    """, unsafe_allow_html=True)

with col_c3:
    st.markdown("""
    <a href="https://github.com/samkeloqonda205-wq" target="_blank" class="social-btn" style="width: 100%; text-align: center;">
        💻 GitHub
    </a>
    """, unsafe_allow_html=True)

with col_c4:
    st.markdown("""
    <a href="tel:0682567468" class="social-btn" style="width: 100%; text-align: center;">
        📞 Call
    </a>
    """, unsafe_allow_html=True)

with col_c5:
    # Create a sample CV file for download
    cv_content = """
SAMKELO QONDA
Data Analyst · Data Scientist · Data Engineer

===============================================

CONTACT
Email: samkeloqonda@gmail.com
Phone: 068 256 7468
Location: Kempton Park, Gauteng, South Africa
LinkedIn: linkedin.com/in/samkelo-qonda-b14738270
GitHub: github.com/samkeloqonda205-wq

===============================================

PROFESSIONAL SUMMARY

Detail-oriented data professional with DataCamp Associate certifications in Data Analysis, Data Science & Data Engineering. Experienced in turning raw data into insights through SQL pipelines, Python models, and interactive Tableau dashboards that drive real business decisions.

===============================================

TECHNICAL SKILLS

Data & Analytics:
Python, Pandas, NumPy, Matplotlib, Seaborn, SQL, PostgreSQL, Tableau, Power BI

Data Engineering:
ETL Pipelines, Data Modeling, Data Cleaning, Data Warehousing, CTEs & Subqueries, Joins & Aggregations

Tools & Systems:
Excel (Advanced), Microsoft 365, SAP / ERP, Syspro ERP, Power BI

Professional Skills:
Statistical Analysis, KPI Reporting, Hypothesis Testing, Data Storytelling, Financial Analysis, Credit Analysis

===============================================

WORK EXPERIENCE

ECONOFOODS
Warehouse Operator — Bulk
May 2025 – Jan 2026 | Longmeadow, Edenvale, Gauteng

• Managed end-to-end inventory operations including receiving, storage, relocation, and dispatch in a high-volume FMCG environment
• Performed daily cycle counts and full stock takes, reconciling physical vs system records to improve stock accuracy
• Utilized RF scanners and Warehouse Management Systems (WMS) to capture real-time inventory data
• Applied FIFO principles to manage perishable goods across bulk, chiller, and freezer storage, reducing waste
• Compiled weekly inventory reports highlighting variances and operational risks for management decision-making
• Supported internal and external audits through accurate documentation and stock validation
• Optimized warehouse layout and bin accuracy to improve picking efficiency and workflow

BOSCH REXROTH / TECTRA AUTOMATION
Storeman
May 2024 – May 2025 | Kempton Park, Gauteng

• Managed stock receiving, issuing, and storage while ensuring accuracy in inventory records using Syspro ERP system
• Coordinated logistics operations across sea, air, and road freight for timely delivery of goods
• Prepared and maintained documentation for inventory tracking and audit purposes
• Conducted routine stock counts and supported inventory reconciliation processes
• Ensured compliance with warehouse safety standards through regular inspections and hazard reporting
• Maintained an organized warehouse layout to improve accessibility and operational efficiency

MAKRO SA
Cashier
Sep 2023 – Nov 2023 | Gauteng

• Processed high-volume transactions accurately using POS systems, handling cash, card, and digital payments
• Maintained balanced cash drawers and completed daily financial reconciliations
• Delivered excellent customer service by resolving queries, handling returns, and assisting with product information
• Monitored stock levels at checkout points and communicated replenishment needs to the team
• Collaborated with team members to maintain efficient service flow in a fast-paced retail environment

===============================================

FEATURED PROJECTS

BRITISH AIRWAYS CUSTOMER REVIEW ANALYSIS DASHBOARD
Tableau · Customer Analytics
Built an interactive Tableau dashboard analyzing thousands of British Airways customer reviews. Identified key satisfaction drivers, route performance gaps, and sentiment trends — enabling data-driven service improvements.
Tech: Tableau, Dashboard Design, Sentiment Analysis, Data Visualization, Customer Analytics
GitHub: github.com/samkeloqonda205-wq/British-Airways-Customer-Review-Analysis-Dashboard

QUANTITATIVE RESEARCH PYTHON PROJECT
Quantitative Research · Python
Applied quantitative methods from the JPMorgan Chase job simulation: investigated and analyzed price data, priced commodity storage contracts, performed credit risk analysis, and bucketed FICO scores using Python statistical modelling.
Tech: Python, NumPy, Statistical Modelling, Credit Risk, FICO Analysis
GitHub: github.com/samkeloqonda205-wq/quantative-research-python

SQL DATA CLEANING — NASHVILLE HOUSING DATASET
SQL · Data Engineering
Comprehensive data cleaning and transformation using advanced SQL: standardized date formats, populated null property addresses, split columns, removed duplicates, and delivered an analytics-ready dataset.
Tech: SQL, Data Cleaning, SQL Server, CTEs, Window Functions
GitHub: github.com/samkeloqonda205-wq/SQL---Data-Cleaning-Nashville-Housing

GLOBAL LIFE EXPECTANCY ANALYSIS
Python · Data Analysis
Explored global health trends and socioeconomic correlations affecting life expectancy across countries using Python EDA and advanced visualizations.
Tech: Python, Pandas, Seaborn, EDA
GitHub: github.com/samkeloqonda205-wq/global-life-expectancy-analysis

AIRBNB PRICE ANALYSIS DASHBOARD
Tableau · Market Analysis
Interactive Tableau dashboard dissecting Airbnb pricing dynamics by location, property type, bedroom count, and seasonal demand patterns.
Tech: Tableau, Price Analytics, Market Research
GitHub: github.com/samkeloqonda205-wq/Airbnb-Price-Analysis-Tableau-Dashboard

CONNECTTEL CALL CENTER ANALYSIS
Data Analytics · Dashboard
Data analysis and visualization project examining call center performance, agent efficiency, resolution rates and customer satisfaction trends.
Tech: Data Analysis, KPI Tracking, Visualization
GitHub: github.com/samkeloqonda205-wq/ConnectTel-Call-Center-Analysis

===============================================

CERTIFICATIONS & CREDENTIALS

DATACAMP CERTIFICATIONS
• Associate Data Scientist (Apr 2026) — Verified
• Associate Data Engineer (Apr 2026) — Verified
• Associate Data Analyst (Feb 2026) — Verified

JOB SIMULATIONS - FORAGE
• Quantitative Research Job Simulation — JPMorgan Chase (Mar 2026)
• Data Analytics Job Simulation — Deloitte (Mar 2026)
• Cybersecurity Job Simulation — Mastercard (Mar 2026)
• Credit Analyst Job Simulation — Standard Chartered (Mar 2026)
• Actuarial Analyst Virtual Job Simulation — AIG (Mar 2026)
• Global Cyber with Data Privacy Job Simulation — DLA Piper (Mar 2026)

OTHER CERTIFICATIONS
• Data Science & Analytics — HP LIFE Foundation (Mar 2026)
• Managing Data with Microsoft 365 — MTN Skills Academy · LinkedIn Learning (Mar 2026)
• Work Readiness & Entrepreneurship Modules — YES Youth Employment Service (Jan 2025)

===============================================


© 2026 Samkelo Qonda
    """
    
    st.download_button(
        label="📥 Download CV",
        data=cv_content,
        file_name="Samkelo_Qonda_CV.txt",
        mime="text/plain"
    )

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("""
<div style="border-top: 1px solid rgba(0,229,255,0.12); padding: 24px 60px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #6b7592;">© 2026 Samkelo Qonda — Data Portfolio</div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #6b7592; letter-spacing: 1px;">ANALYST · SCIENTIST · ENGINEER</div>
</div>
""", unsafe_allow_html=True)
