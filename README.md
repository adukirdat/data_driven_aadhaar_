# data_driven_aadhaar_
# Aadhaar Trends Analysis
# Problem Statement
# Government administrators require a clear, data-driven view of Aadhaar enrolment, update health,
# migration impact, and biometric reliability across India. Existing data is fragmented across multiple datasets
# and difficult to interpret quickly for decision-making. This project aims to consolidate these datasets into a
# single monitoring dashboard to highlight risks, delays, and priority regions for governance action.
# Approach
# Collect Aadhaar-related datasets (enrolment, biometric updates, migration, and stress indicators) in
# CSV format.
# Process and aggregate data using a Python-based backend.
# Expose computed metrics through REST APIs.
# Visualize insights on an interactive frontend dashboard with charts, tables, and alerts.
# Auto-generate priority alerts based on backend-computed metrics.
# Features
# National Overview with key risk indicators.
# Aadhaar Stress Index (ASI) ranking states based on combined stress factors.
# Enrolment & Coverage analysis including delayed child enrolment and age-wise distribution.
# Updates & Biometric Health monitoring update neglect and biometric stress.
# Migration & Data Freshness insights showing enrolment vs update location mismatch.
# Alerts & Priority List auto-generated from backend APIs.
# Interactive filters for time period and state selection.
# Mockups / Screenshots
# This project uses actual application screenshots instead of design mockups.
# Included sections shown in screenshots: - National Overview dashboard - Aadhaar Stress Index (ASI)
# rankings - Enrolment & Coverage analysis - Updates & Biometric Health - Migration & Data Freshness -
# Alerts & Priority List
# (Screenshots are attached in the repository for reference.)
# Tech Stack
# Frontend - React - TypeScript - Recharts - Tailwind CSS
# Backend - FastAPI - Python - Pandas
•
•
•
•
•
•
•
•
•
•
•
•
1
Data - CSV-based datasets
Steps to Run Locally
Backend
Navigate to the backend folder:
cd backend
Create and activate a virtual environment.
Install dependencies:
pip install -r requirements.txt
Start the backend server:
uvicorn app.main:app --reload
Frontend
Navigate to the frontend folder:
cd frontend
Install dependencies:
npm install
Start the development server:
npm start
Open http://localhost:3000 in the browser.
Contributors
Manas Dhomane – manasdhomane04@gmail.com
Aditya Kirdat – kirdat.aditya1995@gmail.com
Ritesh Bakare – riteshbakare7241@gmail.com
1.
2.
3.
4.
1.
2.
3.
4.
•
•
•
2
