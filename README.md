# 🛡️ PhishGuard — Phishing Email Detection and Analysis Tool

**PhishGuard** is a Python-based cybersecurity application that analyzes email text for common phishing warning signs. It uses rule-based detection to identify suspicious phrases, URLs, and references to sensitive information, then generates a risk score and explains the findings.

Built with Python and Streamlit, PhishGuard provides an interactive interface for learning about phishing threats and improving email security awareness.

## ✨ Features

- **Email Analysis:** Analyze pasted email text for common phishing indicators.
- **Risk Scoring:** Generate a risk score from 0 to 100.
- **Risk Classification:** Categorize results as Low, Medium, or High risk.
- **Warning Signs:** Explain detected suspicious phrases, URLs, and sensitive-information references.
- **Sample Emails:** Test the application using fictional suspicious and normal email examples.
- **Security Dashboard:** View scan statistics, risk distribution, average score, and recent scans.
- **Scan History:** Review previous results during the current Streamlit session.
- **CSV Export:** Download scan history for further review.
- **Accessibility Controls:** Switch between Dark, Light, and High Contrast themes, adjust text size, and use read-aloud instructions.
- **Safety Guide:** Learn practical tips for recognizing and avoiding phishing attacks.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and detection rules |
| Streamlit | Interactive web interface and dashboard |
| Regular Expressions (`re`) | URL and keyword detection |
| CSV (`csv`) | Exporting scan history |
| Datetime (`datetime`) | Recording analysis timestamps |
| Streamlit Components | Browser-based read-aloud functionality |

## ⚙️ How It Works

1. The user pastes an email or loads a sample.
2. PhishGuard checks the text against predefined suspicious phrases.
3. It identifies URLs and references to sensitive information, such as passwords and OTPs.
4. Points are added for detected indicators, and the score is capped at 100.
5. The application assigns a risk level and displays the warning signs.
6. The result is added to the current session's scan history.
7. Users can review results on the Security Dashboard and export the history as a CSV file.

### Risk Classification

| Score | Classification |
|---|---|
| 0–29 | 🟢 Low Risk |
| 30–59 | 🟠 Medium Risk |
| 60–100 | 🔴 High Risk |

*The risk score is based on predefined rules. It is not a probability that an email is malicious.*

## 📁 Project Structure

```text
PhishGuard/
├── app.py
├── requirements.txt
├── README.md
└── Project_Report.pdf
```

- `app.py` — Main application and phishing analysis logic.
- `requirements.txt` — Required Python packages.
- `README.md` — Project overview, setup, and usage instructions.
- `Project_Report.pdf` — Detailed project documentation.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.9 or later recommended.
- A modern web browser.
- Internet access for installing dependencies.

### 1. Clone the repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd PhishGuard
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 🧪 How to Use

1. Open **Email Analyzer**.
2. Paste email text or select a built-in example.
3. Click **Load selected example** if you selected a sample.
4. Click **Analyze Email**.
5. Review the risk score, classification, warning signs, and recommended actions.
6. Open **Security Dashboard** to view scan statistics and export results.
7. Open **Safety Guide** for phishing prevention tips.
8. Customize the interface through the sidebar accessibility controls.

## 🔍 Testing

PhishGuard includes two fictional examples:

- **Suspicious account email:** Contains urgency, account suspension language, a URL, and a password request.
- **Normal meeting email:** Contains routine meeting information without the predefined warning signs.

The suspicious example should generally receive a higher score than the normal example. Actual results depend on the implemented rules.

## ⚠️ Limitations

- Uses rule-based detection rather than a trained machine-learning model.
- Does not verify sender identity or authenticate email domains.
- Does not visit URLs, inspect attachments, or check external threat-intelligence databases.
- May miss sophisticated phishing emails or flag legitimate emails.
- Scan history is held in Streamlit session state and is not permanently stored in a database.
- A Low Risk result does not guarantee that an email is safe.

## 🔮 Future Enhancements

- Machine-learning-based phishing classification.
- Sender and domain reputation checks.
- Integration with trusted threat-intelligence APIs.
- Secure email-file analysis.
- Persistent scan history with privacy protections.
- Automated tests and evaluation using labelled email datasets.
- Detailed downloadable analysis reports.

*These are planned enhancements and are not included in the current version unless implemented separately.*

## 🎯 Project Objective

The objective of PhishGuard is to demonstrate basic email threat analysis, raise awareness of phishing techniques, and provide a simple educational tool for understanding common email security indicators.

## 🔐 Disclaimer

PhishGuard is an educational cybersecurity project. Its findings are indicative and should not be treated as a definitive security verdict. Avoid submitting confidential emails or sensitive personal information. Verify suspicious messages through trusted channels.

## 👩‍💻 Project Information

- **Project:** PhishGuard — Phishing Email Detection and Analysis Tool
- **Category:** Cybersecurity / Email Security
- **Language:** Python
- **Framework:** Streamlit
- **Approach:** Rule-based analysis
- **Purpose:** Cybersecurity Bootcamp Project

---

⭐ If you find this project useful for learning about phishing awareness and defensive cybersecurity, consider starring the repository.
