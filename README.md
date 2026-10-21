🛡️ PhishGuard – Phishing Email Detection and Analysis Tool
1. Overview
PhishGuard is a Python-based cybersecurity application designed to identify potential phishing emails by analyzing their text for common warning signs. It uses a rule-based detection approach to identify suspicious phrases, URLs, and requests for sensitive information.

The application calculates a risk score, classifies the email as Low, Medium, or High risk, and explains the warning signs detected. It also includes a security dashboard, scan history, CSV export, accessibility controls, and a phishing safety guide.

PhishGuard is developed as a cybersecurity bootcamp project to demonstrate basic phishing analysis and promote email security awareness.

2. Features
Email Analysis: Analyze pasted email text for common phishing indicators.
Risk Scoring: Generate a risk score from 0 to 100.
Threat Classification: Categorize analyzed emails as Low, Medium, or High risk.
Warning Explanations: Display suspicious phrases, detected URLs, and references to sensitive information.
Sample Emails: Test the application using fictional suspicious and normal email examples.
Security Dashboard: View total scans, risk counts, average risk score, and recent scan results.
Scan History: Review previous analyses during the current application session.
CSV Export: Download scan history as a CSV file.
Accessibility Controls: Switch between Dark, Light, and High Contrast themes, adjust text size, and use read-aloud instructions.
Safety Guide: Learn practical ways to recognize and avoid phishing attacks.
3. Technologies Used
Python: Main programming language.
Streamlit: Web application interface and interactive dashboard.
Regular Expressions (re): Identify URLs and sensitive-information keywords.
CSV (csv): Export scan history.
Datetime (datetime): Record analysis timestamps.
String I/O (io): Prepare CSV data for download.
Streamlit Components: Support browser-based text-to-speech instructions.
IBM Bob: AI coding assistant used to support development, where applicable.
4. How It Works
PhishGuard follows a rule-based analysis process:

The user pastes an email or loads a sample email.
The application converts the text to lowercase for phrase matching.
It checks for predefined suspicious phrases such as "urgent", "account suspended", and "verify your account".
It searches for URLs and checks for references to sensitive information, such as passwords, OTPs, and bank details.
It assigns points for detected indicators and caps the total risk score at 100.
It classifies the result as Low, Medium, or High risk.
It displays the score, warning signs, timestamp, and recommended safety actions.
The result is added to the session's scan history and can be viewed on the Security Dashboard or exported as CSV.
Risk Classification
Risk Score	Risk Level
0–29	Low
30–59	Medium
60–100	High
The score is based on predefined rules, not a trained machine-learning model. It is an indicative score and does not represent a verified probability that an email is malicious.

5. Project Structure
PhishGuard/
├── app.py
├── requirements.txt
├── README.md
└── Project_Report.pdf

app.py — Contains the application interface, detection logic, dashboard, accessibility controls, and safety guide.
requirements.txt — Lists the Python packages required to run the application.
README.md — Provides project information and setup instructions.
6. Requirements
Python 3.9 or later recommended.
An internet browser.
Internet access to install the required packages.
The Python packages listed in requirements.txt.
7. Installation and Setup
Step 1: Download or clone the repository
Clone the repository after replacing the placeholder with your actual GitHub repository URL:

git clone <your-github-repository-url>

Alternatively, download the repository as a ZIP file and extract it.

Step 2: Open the project folder
Open a terminal or PowerShell window in the project directory.

Step 3: Create a virtual environment (recommended)
python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Step 4: Install dependencies
python -m pip install -r requirements.txt

Ensure that requirements.txt includes the packages actually used by the project, including Streamlit.

Step 5: Run the application
python -m streamlit run app.py

Streamlit will provide a local URL, usually http://localhost:8501. Open that address in your browser to use PhishGuard.

8. How to Use PhishGuard
Open the application in your browser.
Select Email Analyzer.
Paste an email or select a fictional example from the sample dropdown.
Click Load selected example if using a sample.
Click Analyze Email.
Review the risk score, risk level, warning signs, and recommended actions.
Open Security Dashboard to review scan statistics and download scan history as CSV.
Open Safety Guide to read phishing prevention tips.
Use the sidebar preferences to change the theme, adjust text size, or enable read-aloud instructions.
9. Testing
The application can be tested using the built-in fictional email examples:

Suspicious account email: Contains urgent language, an account suspension warning, a URL, and a request to verify a password.
Normal meeting email: Contains ordinary meeting-related information without the predefined phishing indicators.
Expected behavior is that the suspicious example receives a higher risk score than the normal example. Results depend on the predefined detection rules.

10. Limitations
PhishGuard uses basic rule-based checks rather than machine learning.
It analyzes the supplied email text and does not verify the sender's identity.
It does not visit URLs, inspect attachments, or verify a website's reputation.
It may miss sophisticated phishing emails or flag legitimate messages.
Its risk score is an indicator based on predefined rules, not a calibrated probability.
Scan history is stored in Streamlit session state and is not permanently saved to a database.
Text analysis alone cannot guarantee whether an email is safe or malicious.
Security note: Do not paste confidential emails or sensitive personal information into the application unless you are authorized to do so.

11. Future Scope
Possible future enhancements include:

Integrating a trained machine-learning model for phishing classification.
Adding sender-address and domain analysis.
Integrating trusted threat-intelligence services to check URL reputation.
Supporting email file uploads in a controlled and secure manner.
Adding persistent scan history with appropriate privacy protections.
Improving detection accuracy through a labelled dataset and systematic testing.
Adding automated test cases and more detailed analysis reports.
These are proposed improvements and are not features of the current implementation.

12. Conclusion
PhishGuard demonstrates how Python can be used to build a basic phishing email analysis application. It combines rule-based detection, risk scoring, warning explanations, scan history, CSV export, and accessibility features in an interactive Streamlit interface.

The project provides a practical introduction to phishing indicators and defensive cybersecurity concepts. Although it cannot detect every phishing attack, it can help users understand common warning signs and develop safer email habits.

13. Disclaimer
PhishGuard is an educational cybersecurity project. Its results should not be treated as a definitive security verdict. Always verify suspicious messages through trusted channels and follow your organization's security procedures.

14. Author and Project Information
Project Name: PhishGuard – Phishing Email Detection and Analysis Tool
Category: Cybersecurity / Email Security
Language: Python
Interface Framework: Streamlit
Project Type: Cybersecurity Bootcamp Project
GitHub Repository: https://github.com/KermeenDeboo/Projects/tree/BharatCares-Bootcamp-Oct-26
