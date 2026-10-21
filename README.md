# Phishing Email Detection and Analysis Tool

## Project Overview
A beginner-friendly cybersecurity application built with Python and Streamlit. It analyzes email text for common phishing warning signs and displays a risk score with explanations.

## Features
- Analyze pasted email text.
- Detect suspicious phrases and URLs.
- Display a risk score and risk level.
- Explain detected warning signs.
- Show the analysis timestamp.

## Technologies Used
- Python
- Streamlit
- Regular Expressions (`re`)
- Date and Time (`datetime`)

## Installation
1. Install Python.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Install the required library:

   `python -m pip install -r requirements.txt`

## Run the Application

`python -m streamlit run app.py`

Open the local URL displayed in the terminal.

## Limitations
This project uses basic rule-based checks. It may miss phishing emails or flag legitimate emails. A low risk score does not guarantee that an email is safe.

## Future Improvements
- Maintain scan history.
- Export results to CSV.
- Improve risk scoring and URL analysis.
- Add more testing and detection rules.

## Disclaimer
Use this tool for educational purposes. Do not open suspicious links or submit confidential email content.
