import streamlit as st
import base64
import os

st.set_page_config(page_title="Disaster Analysis Portal", layout="wide")

def get_img_as_base64(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_b64 = get_img_as_base64("logo.png")
upgov_b64 = get_img_as_base64("upgov.png")
mkb_b64 = get_img_as_base64("mkb.png")

st.markdown("""
    <style>
    /* Container for the logos - Aligned to Right, Transparent */
    .logo-header {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 25px;
        margin-bottom: 10px;
        padding-right: 10px;
    }
    .logo-header img {
        height: 80px; 
        object-fit: contain;
        transition: transform 0.3s ease;
        filter: drop_shadow(0px 2px 2px rgba(0,0,0,0.1)); 
    }
    .logo-header img:hover {
        transform: scale(1.05);
    }
    
    /* Card styling for the descriptions - ADAPTIVE THEME */
    .description-box {
        background-color: var(--secondary-background-color); /* Adapts to Dark/Light mode */
        color: var(--text-color); /* Adapts to Dark/Light mode */
        padding: 25px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2); /* Subtle border for both themes */
        
        /* Layout enforcement for equal sizing */
        height: 100%; 
        min-height: 420px; /* Forces both boxes to be at least this tall */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Style for the footer notice - ADAPTIVE THEME */
    .footer-notice {
        margin-top: 60px;
        padding: 25px;
        background-color: var(--secondary-background-color); /* Adapts to Dark/Light mode */
        border-radius: 10px;
        border-left: 6px solid #ff4b4b;
        font-size: 15px;
        line-height: 1.6;
        color: var(--text-color); /* Adapts to Dark/Light mode */
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .footer-title {
        font-weight: 700;
        color: #ff4b4b; /* Keeps the accent color consistent */
        margin-bottom: 8px;
        display: block;
        text-transform: uppercase;
        font-size: 12px;
        letter-spacing: 1px;
    }
    
    /* Strong tags need to force color inheritance to look good in dark mode */
    .description-box strong, .footer-notice strong {
        color: var(--text-color);
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

def show_home():
    st.markdown(f"""
        <div class="logo-header">
            <img src="data:image/png;base64,{logo_b64}" title="Project Logo">
            <img src="data:image/png;base64,{upgov_b64}" title="Government of UP">
            <img src="data:image/png;base64,{mkb_b64}" title="Partner Logo">
        </div>
    """, unsafe_allow_html=True)

    st.title("📊 Disaster & Hazard Analysis Portal")
    st.markdown("#### Comprehensive Data Visualization & Statistical Assessment Tool")
    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.subheader("Hazard-Wise Analysis")
        st.markdown("""
        <div class="description-box">
            This module focuses on the <strong>categorical breakdown of casualties</strong> caused by specific disaster types (e.g., Lightning, Fire, Floods). 
            <br><br>
            <strong>Key Features:</strong>
            <ul>
                <li><strong>Spatial Heatmaps:</strong> Visualize the intensity of specific hazards across all 75 districts.</li>
                <li><strong>Statistical Deep-Dive:</strong> View standard deviation, mean, and maximum casualty metrics for selected hazards.</li>
                <li><strong>Outlier Detection:</strong> Identify districts with critically high contributions to specific disaster types.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Launch Hazard Analysis", use_container_width=True):
            st.switch_page(page_1)

    with col2:
        st.subheader("Yearly Temporal Analysis")
        st.markdown("""
        <div class="description-box">
            This module tracks the <strong>temporal progression of data</strong> from the financial year 2018-19 to present, highlighting trends and fluctuations over time.
            <br><br>
            <strong>Key Features:</strong>
            <ul>
                <li><strong>Trend Identification:</strong> Analyze year-on-year increases or decreases in mortality rates.</li>
                <li><strong>Comparative Growth:</strong> Identify which districts are showing alarming growth rates in casualties vs. those showing improvement.</li>
                <li><strong>Annual Reporting:</strong> Generate year-specific breakdowns of district performance and state-wide totals.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        if st.button("Launch Yearly Analysis", use_container_width=True):
            st.switch_page(page_2)

    st.markdown("""
        <div class="footer-notice">
            <span class="footer-title">Development & Data Attribution</span>
            This analytical dashboard was architected and developed by <strong>Ayush Dwivedy</strong> as part of a strategic internship initiative spanning 
            <strong>August 2024 to May 2025</strong>. 
            <br><br>
            The visualizations, statistical models, and geographical insights presented herein are derived strictly from official casualty datasets 
            authorized and provided by the <strong>Uttar Pradesh State Disaster Management Authority (UP-SDMA)</strong>. 
            This tool is intended to aid in data-driven decision-making and hazard mitigation planning.
        </div>
    """, unsafe_allow_html=True)

home_page = st.Page(show_home, title="Home", default=True)
page_1 = st.Page("Main/main.py", title="- Hazard Analysis")
page_2 = st.Page("Probed/probed.py", title="- Yearly Analysis")

pg = st.navigation([home_page, page_1, page_2])
pg.run()