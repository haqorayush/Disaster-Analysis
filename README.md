# 📊 Disaster & Hazard Analysis Portal (UP-SDMA)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=for-the-badge&logo=geopandas&logoColor=white)

[**Live Demo**](https://upsdma-analysis.streamlit.app)

---

## Overview

The **Disaster & Hazard Analysis Portal** is a comprehensive data analytics and visualization platform designed to assess disaster-related casualties across the **75 districts of Uttar Pradesh, India**.  
The system supports **evidence-based disaster risk management** by integrating statistical analysis with geospatial intelligence.

The platform enables policymakers, researchers, and disaster management authorities to:
- Identify high-risk districts
- Track temporal trends in disaster impact
- Compare hazard-wise mortality
- Detect anomalies and emerging threats

---

## Objectives

- Provide district-wise vulnerability assessment  
- Visualize spatial and temporal disaster patterns  
- Enable early identification of abnormal risk growth  
- Support planning, mitigation, and response strategies  

---

## Core Analytical Modules

### 1. Hazard-Wise Analysis
Analyzes casualties by disaster category such as **Lightning, Floods, Fire, Drowning, and Heatwave**.

Features:
- **Geospatial Heatmaps** using GeoPandas and Folium  
- **Statistical summaries** (mean, standard deviation, max)  
- **Outlier detection** for districts with extreme casualties  
- **District-wise hazard contribution** via pie charts  

---

### 2. Yearly Temporal Analysis
Analyzes disaster trends across financial years from **2018-19 to present**.

Features:
- **Year-on-year mortality trends**
- **Growth and decline tracking**
- **Most affected vs least affected districts**
- **State-level yearly summaries**

---

## Analytical Methodology

| Component | Method |
|--------|--------|
| Outlier Detection | Z-Score (μ ± 2σ) |
| Trend Analysis | Year-on-year casualty growth |
| Comparative Risk | District-wise contribution to state totals |
| Heatmap Scaling | Normalized color intensity across districts |
| Temporal Ranking | Sorted by casualty growth and totals |

All calculations are performed using **NumPy and Pandas**, while spatial joins are handled via **GeoPandas**.

---

## 🛠️ Technology Stack

| Layer | Tools |
|------|------|
| Frontend | Streamlit (Multipage App) |
| Data Processing | Pandas, NumPy |
| Geospatial | GeoPandas, Folium, Streamlit-Folium |
| Visualization | Matplotlib, Folium |
| Deployment | Streamlit Cloud |

---

## 📂 Project Structure

```text
├── app_entry.py           # Main application entry point
├── requirements.txt      # Dependencies
├── logo.png
├── upgov.png
├── mkb.png
│
├── Main/                 # Hazard-Wise Analysis
│   ├── main.py
│   ├── data.csv
│   └── up_districts.geojson
│
└── Probed/               # Yearly Temporal Analysis
    ├── probed.py
    ├── data.csv
    └── up_districts.geojson
```
---
## ⚙️ Installation & Local Setup
To run this application locally on your machine, follow these steps:

Clone the repository:

```bash
git clone [https://github.com/your-username/disaster-analysis-portal.git](https://github.com/your-username/disaster-analysis-portal.git)
cd disaster-analysis-portal
```

## Create a virtual environment (Recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the application:

```bash
streamlit run app_entry.py
```

## Configuration & Customization
- Updating Data: To update the analysis, simply replace the data.csv file in either the Main/ or Probed/ directory. Ensure the column headers remain consistent (e.g., 'District', 'Year', 'Hazard Type').
- Changing Logos: Replace logo.png, upgov.png, or mkb.png in the root directory to update the branding on the landing page.
- Modifying Thresholds: Color scale thresholds can be adjusted in the color_scale function within main.py and probed.py to reflect different sensitivity levels.

## ❓ Troubleshooting
```bash
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
```
- *Cause:* Running the script from the wrong directory level.
- *Solution:* Always run the app using streamlit run app_entry.py from the root directory. The scripts use os.path to find relative files, but the entry point must be consistent.
```bash
ModuleNotFoundError: No module named 'geopandas'
```
- *Cause:* Missing dependencies.
- *Solution:* Ensure you have installed the requirements using pip install -r requirements.txt. If deploying to the cloud, ensure requirements.txt is present in the repo root.

## Future Roadmap
*Potential enhancements planned for future iterations:*

- Predictive Analytics: Integration of ARIMA models to forecast potential high-risk zones for the upcoming financial year.
- Real-Time API Integration: Connecting to live weather APIs for real-time flood and lightning alerts.
- PDF Report Generation: One-click download of district-specific disaster profiles for official reporting.

## Author & Attribution
- *Developer:* Ayush Dwivedy
- *Role:* Specialized AI-HPC Engineer / Programmer II - Intern
- *Duration:* August 2024 - May 2025

## Notice:
This application was created by Ayush Dwivedy during the internship period of Aug 2024 - May 2025 as per the data provided by the Uttar Pradesh State Disaster Management Authorities (UPSDMA). The visualizations and models presented herein are intended to support hazard mitigation planning.

## License & Data Privacy
The code in this repository is provided for educational and portfolio purposes.
Data Source: All casualty and district data is sourced from the Uttar Pradesh State Disaster Management Authority.
Note: Ensure sensitive government data is not exposed in public repositories unless authorized. 

<div align="center">
  <sub>Built with ❤️ by <a href="https://www.google.com/search?q=https://github.com/haqorayush">haqorayush</a></sub>
</div>
