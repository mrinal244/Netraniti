# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

- Netraniti – Automated Social Media Forensics Tool
🔍 Overview
Netraniti is an advanced cyber forensics tool designed to automate the collection, parsing, and documentation of social media data for investigative agencies. It helps law enforcement and intelligence units gather crucial digital evidence efficiently from suspects' or accused individuals’ social media accounts across multiple platforms.

The tool generates well-structured, court-admissible reports that include messages, posts, follower lists, screenshots, geolocation activity, and AI-generated summaries, streamlining the entire investigation process.

⚙️ How It Works
Data Collection

Automatically scrapes data from social media accounts (e.g., Facebook, Instagram, Telegram, WhatsApp, Twitter, Google).

Captures posts, timelines, followers, comments, messages, and metadata.

Automation of Screenshots

Captures relevant sections (posts, messages, profiles) as screenshots for documentation and evidence.

AI-Powered Summarization

Applies AI models to summarize long chats, posts, or profiles and highlight suspicious behavior.

Geolocation Tracking

If available, extracts and maps location-based data from user activity.

Report Generation

Compiles all extracted data and screenshots into a downloadable, organized PDF report (Panchnama format), ready for legal use.

🎯 Key Features
✅ Multi-platform data parsing

✅ Automated evidence screenshot capture

✅ AI-generated summaries and sentiment analysis

✅ Organized, court-ready PDF reports

✅ Works on both Android and Windows versions

✅ Investigator-friendly interface

👮‍♂️ Why Netraniti is Helpful
Reduces manual errors in digital evidence collection.

Saves time for officers during time-sensitive investigations.

Enables consistent documentation of online data in legal formats.

Helps identify digital trails, suspicious connections, or behavioral patterns.

Especially useful for agencies like NIA, Police Departments, and Cyber Crime Units.

🛠️ Tech Stack Used
Technology	Purpose
Python	Backend scripting, automation
Selenium / Puppeteer	Web scraping & screenshot automation
TensorFlow / HuggingFace Transformers	AI summarization, NLP
Flask / FastAPI	API for Windows/Android bridge  // on work
React Native / Kotlin	Android app version   // on work
PyMuPDF / ReportLab	PDF report generation
SQLite / Firebase	Local/Cloud storage        // on work
Google Maps API	Geolocation tracking and mapping  // on worki
