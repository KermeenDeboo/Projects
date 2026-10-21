import streamlit as st
import streamlit.components.v1 as components
import re
import csv
import io
from datetime import datetime

# ============================================================
# PHISHGUARD - single-file phishing email detection application
# ============================================================
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Session state ----------
if "scan_history" not in st.session_state:
    st.session_state.scan_history = []
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "email_text" not in st.session_state:
    st.session_state.email_text = ""
if "appearance" not in st.session_state:
    st.session_state.appearance = "Dark"
if "font_scale" not in st.session_state:
    st.session_state.font_scale = 100
if "read_aloud" not in st.session_state:
    st.session_state.read_aloud = False
if "speech_command" not in st.session_state:
    st.session_state.speech_command = "stop"

# ---------- Accessibility controls ----------
with st.sidebar:
    st.title("⚙️ Preferences")
    st.caption("Personalize your workspace")

    st.selectbox(
        "Appearance",
        ["Dark", "Light", "High Contrast"],
        key="appearance",
    )
    st.slider(
        "Text size",
        min_value=80,
        max_value=150,
        step=10,
        key="font_scale",
        format="%d%%",
    )

    st.toggle("Read instructions aloud", key="read_aloud")

    if st.session_state.read_aloud:
        if st.button("🔊 Read Instructions", use_container_width=True):
            st.session_state.speech_command = "speak"
        if st.button("⏹ Stop Speaking", use_container_width=True):
            st.session_state.speech_command = "stop"
    else:
        st.session_state.speech_command = "stop"

    st.divider()
    st.caption("PhishGuard • Email Threat Detection Tool")

# ---------- Theme colors ----------
appearance = st.session_state.appearance
if appearance == "Light":
    bg = "#f4f7fc"
    surface = "#ffffff"
    fg = "#182238"
    muted = "#53627a"
    accent = "#4f46e5"
    border = "#d7deea"
    field_bg = "#ffffff"
elif appearance == "High Contrast":
    bg = "#000000"
    surface = "#000000"
    fg = "#ffffff"
    muted = "#ffffff"
    accent = "#ffff00"
    border = "#ffffff"
    field_bg = "#000000"
else:
    bg = "#101827"
    surface = "#172338"
    fg = "#f1f5ff"
    muted = "#bdc9dc"
    accent = "#818cf8"
    border = "#35445e"
    field_bg = "#111827"

# Explicitly style Streamlit's main app containers, not only .stApp.
st.markdown(
    f"""
    <style>
    :root {{
        color-scheme: {"light" if appearance == "Light" else "dark"};
    }}
    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    section[data-testid="stMain"],
    [data-testid="stHeader"] {{
        background-color: {bg} !important;
        color: {fg} !important;
    }}
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div {{
        background-color: {surface} !important;
        color: {fg} !important;
        border-right: 1px solid {border};
    }}
    [data-testid="stMain"] .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }}
    .stApp, .stApp p, .stApp label, .stApp li,
    .stApp h1, .stApp h2, .stApp h3,
    .stApp [data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {{
        color: {fg} !important;
    }}
    .stApp p, .stApp li, .stApp label {{
        font-size: {st.session_state.font_scale}% !important;
    }}
    [data-testid="stCaptionContainer"], .stCaption {{
        color: {muted} !important;
    }}
    [data-testid="stMetric"] {{
        background: {surface} !important;
        border: 1px solid {border} !important;
        border-radius: 14px !important;
        padding: 15px !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: {muted} !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {accent} !important;
    }}
    .stTextArea textarea, .stTextInput input {{
        background: {field_bg} !important;
        color: {fg} !important;
        border: 1px solid {border} !important;
        border-radius: 8px !important;
    }}
    [data-baseweb="select"] > div {{
        background: {field_bg} !important;
        color: {fg} !important;
        border-color: {border} !important;
    }}
    .stButton > button, .stDownloadButton > button {{
        background: {surface};
        color: {fg} !important;
        border: 1px solid {border} !important;
        border-radius: 9px !important;
        min-height: 42px;
        font-weight: 600;
    }}
    .stButton > button:hover, .stDownloadButton > button:hover {{
        border: 2px solid {accent} !important;
        color: {accent} !important;
    }}
    [data-testid="stExpander"] {{
        background: {surface} !important;
        border: 1px solid {border} !important;
        border-radius: 10px !important;
    }}
    [data-testid="stDataFrame"] {{
        border: 1px solid {border};
        border-radius: 10px;
    }}
    a {{ color: {accent} !important; }}
    :focus-visible {{
        outline: 3px solid {accent} !important;
        outline-offset: 2px !important;
    }}
    .pg-eyebrow {{
        color: {accent} !important;
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 0.4rem;
    }}
    .pg-subtitle {{
        color: {muted} !important;
        font-size: 1.05rem;
    }}
    .pg-panel {{
        background: {surface};
        border: 1px solid {border};
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

if appearance == "High Contrast":
    st.markdown(
        """
        <style>
        html, body, .stApp, [data-testid="stAppViewContainer"],
        [data-testid="stMain"], section[data-testid="stMain"],
        [data-testid="stHeader"], [data-testid="stSidebar"],
        [data-testid="stSidebar"] > div {
            background: #000000 !important;
            color: #ffffff !important;
        }
        .stApp p, .stApp label, .stApp li, .stApp h1, .stApp h2,
        .stApp h3, .stApp span, .stApp [data-testid="stMarkdownContainer"],
        [data-testid="stCaptionContainer"] {
            color: #ffffff !important;
        }
        .stButton > button, .stDownloadButton > button {
            background: #000000 !important;
            color: #ffff00 !important;
            border: 2px solid #ffff00 !important;
        }
        .stTextArea textarea, .stTextInput input,
        [data-baseweb="select"] > div {
            background: #000000 !important;
            color: #ffffff !important;
            border: 2px solid #ffffff !important;
        }
        [data-testid="stMetric"], [data-testid="stExpander"] {
            background: #000000 !important;
            border: 2px solid #ffffff !important;
        }
        a { color: #00ffff !important; text-decoration: underline !important; }
        :focus-visible {
            outline: 3px solid #00ffff !important;
            outline-offset: 3px !important;
        }
        ::selection { background: #ffff00 !important; color: #000000 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------- Speech control ----------
# Buttons are only in the sidebar. This iframe asks the parent page's
# speech engine to cancel first, then optionally starts a new utterance.
instructions = (
    "Welcome to PhishGuard, the phishing email detection tool. "
    "In Email Analyzer, paste an email or load a sample, then choose Analyze Email. "
    "Review the risk score and warning signs. A low score does not guarantee safety. "
    "Open Security Dashboard to review scans and export the CSV. "
    "Open Safety Guide for phishing prevention tips."
)
command = st.session_state.speech_command
enabled = st.session_state.read_aloud
components.html(
    f"""
    <script>
    (() => {{
      const parentWindow = window.parent;
      const command = {command!r};
      const enabled = {str(enabled).lower()};
      const message = {instructions!r};
      try {{
        if (parentWindow.speechSynthesis) {{
          parentWindow.speechSynthesis.cancel();
          if (enabled && command === "speak") {{
            const utterance = new parentWindow.SpeechSynthesisUtterance(message);
            utterance.rate = 0.95;
            parentWindow.speechSynthesis.speak(utterance);
          }}
        }}
      }} catch (error) {{}}
    }})();
    </script>
    """,
    height=0,
)

# ---------- Original rule-based detector ----------
def analyze_email(text):
    findings = []
    score = 0
    lower_text = text.lower()

    suspicious_phrases = [
        "urgent", "verify your account", "password",
        "account suspended", "click here", "limited time",
        "confirm your identity", "immediately"
    ]

    for phrase in suspicious_phrases:
        if phrase in lower_text:
            findings.append(f"Suspicious wording: '{phrase}'")
            score += 15

    urls = re.findall(r"https?://[^\s<>]+|www\.[^\s<>]+", text, re.I)
    if urls:
        findings.append(
            f"Contains {len(urls)} URL(s). Check destinations carefully."
        )
        score += 20

    if re.search(r"\b(password|otp|one-time code|bank details)\b", lower_text):
        findings.append("Mentions sensitive information.")
        score += 20

    score = min(score, 100)
    if score >= 60:
        risk = "High"
    elif score >= 30:
        risk = "Medium"
    else:
        risk = "Low"

    if not findings:
        findings.append("No warning signs detected by these basic checks.")
    return score, risk, findings

# ---------- Main page header ----------
st.markdown('<div class="pg-eyebrow">EMAIL THREAT ANALYSIS</div>', unsafe_allow_html=True)
st.title("🛡️ Phishing Email Detection Tool")
st.markdown(
    '<div class="pg-subtitle">Analyze email text for common phishing warning signs.</div>',
    unsafe_allow_html=True,
)
st.write("")
st.divider()

# ---------- Main navigation ----------
page = st.radio(
    "Main navigation",
    ["Email Analyzer", "Security Dashboard", "Safety Guide"],
    horizontal=True,
    label_visibility="collapsed",
    key="main_navigation",
)

# ---------- Email analyzer ----------
if page == "Email Analyzer":
    analyzer_col, tips_col = st.columns([1.65, 1], gap="large")

    with analyzer_col:
        st.subheader("Email Analyzer")
        st.write("Paste an email below, or load a fictional example.")

        sample_choice = st.selectbox(
            "Try a sample email",
            [
                "Choose an example...",
                "Suspicious account email",
                "Normal meeting email",
            ],
        )
        if st.button("Load selected example", use_container_width=True):
            if sample_choice == "Suspicious account email":
                st.session_state.email_text = (
                    "URGENT! Your account is suspended. Click here to verify "
                    "your account immediately: http://example.com/login. "
                    "Please confirm your password."
                )
            elif sample_choice == "Normal meeting email":
                st.session_state.email_text = (
                    "Hello team, our project meeting is scheduled for Thursday "
                    "at 10 AM. Please review the agenda before the meeting. Thank you."
                )
            else:
                st.info("Choose one of the sample emails first.")

        email_text = st.text_area(
            "Paste the email text here:",
            height=220,
            placeholder="Paste a sample email to analyze...",
            key="email_text",
        )

        if st.button("Analyze Email", type="primary", use_container_width=True):
            if not email_text.strip():
                st.warning("Please paste some email text first.")
            else:
                score, risk, findings = analyze_email(email_text)
                result = {
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Risk Score": score,
                    "Risk Level": risk,
                    "Warning Signs": "; ".join(findings) if findings else "None detected",
                    "Email Preview": email_text[:100].replace("\n", " "),
                }
                st.session_state.scan_history.insert(0, result)
                st.session_state.last_result = result

    with tips_col:
        st.subheader("Quick Safety Tips")
        st.info("🔐 Never share passwords or one-time codes in response to unexpected emails.")
        st.info("🔗 Check the destination of links before opening them.")
        st.info("☎️ Verify urgent requests through a trusted, separate channel.")
        with st.expander("What does the risk score mean?"):
            st.write("The score increases when the text contains suspicious phrases, URLs, or mentions of sensitive information.")
            st.write("High: 60–100 · Medium: 30–59 · Low: 0–29")
        st.caption("A low score does not guarantee that an email is safe.")

    if st.session_state.last_result:
        result = st.session_state.last_result
        st.divider()
        st.subheader("🔬 Latest Analysis")
        c1, c2, c3 = st.columns(3)
        c1.metric("Risk Score", f"{result['Risk Score']}/100")
        c2.metric("Risk Level", result["Risk Level"])
        c3.metric("Analysis Time", result["Timestamp"].split(" ")[1])

        score = result["Risk Score"]
        st.progress(score / 100, text=f"Risk score: {score}/100")

        if result["Risk Level"] == "High":
            st.error("High risk: do not click links or provide sensitive information.")
        elif result["Risk Level"] == "Medium":
            st.warning("Medium risk: verify the sender and links independently.")
        else:
            st.success("Low risk under these checks. Continue to use caution.")

        with st.expander("View warning signs", expanded=True):
            for item in result["Warning Signs"].split("; "):
                st.markdown(f"- {item}")

        with st.expander("Recommended next steps"):
            st.markdown(
                "- Check the sender's complete email address.\n"
                "- Do not open unexpected links or attachments.\n"
                "- Verify unusual requests using an official contact method.\n"
                "- Report suspicious messages to your security team."
            )

# ---------- Security dashboard ----------
elif page == "Security Dashboard":
    st.subheader("📊 Security Dashboard")
    history = st.session_state.scan_history

    if not history:
        st.info("No scans yet. Analyze an email to populate your dashboard.")
    else:
        total = len(history)
        high = sum(item["Risk Level"] == "High" for item in history)
        medium = sum(item["Risk Level"] == "Medium" for item in history)
        low = sum(item["Risk Level"] == "Low" for item in history)
        average = round(sum(item["Risk Score"] for item in history) / total)

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Scans", total)
        c2.metric("High Risk", high)
        c3.metric("Medium Risk", medium)
        c4.metric("Average Score", f"{average}/100")

        chart_col, recent_col = st.columns([1, 1], gap="large")
        with chart_col:
            st.markdown("**Risk Distribution**")
            st.bar_chart({
                "Number of emails": {
                    "High": high,
                    "Medium": medium,
                    "Low": low,
                }
            })
        with recent_col:
            st.markdown("**Recent Scans**")
            st.dataframe(
                [
                    {"Timestamp": item["Timestamp"], "Risk": item["Risk Level"], "Score": item["Risk Score"]}
                    for item in history[:10]
                ],
                use_container_width=True,
                hide_index=True,
            )

        with st.expander("View full scan history"):
            st.dataframe(history, use_container_width=True, hide_index=True)

        csv_buffer = io.StringIO()
        fields = list(history[0].keys())
        writer = csv.DictWriter(csv_buffer, fieldnames=fields)
        writer.writeheader()
        writer.writerows(history)
        st.download_button(
            "📥 Download Scan History (CSV)",
            data=csv_buffer.getvalue(),
            file_name="phishing_scan_history.csv",
            mime="text/csv",
            use_container_width=True,
        )

        if st.button("🗑️ Clear scan history", use_container_width=True):
            st.session_state.scan_history = []
            st.session_state.last_result = None
            st.rerun()

# ---------- Safety guide ----------
elif page == "Safety Guide":
    st.subheader("🧠 Phishing Safety Guide")
    tips = [
        ("Check the sender", "Inspect the full email address and look for misspelled domains."),
        ("Be careful with urgency", "Scammers may pressure you to act immediately or threaten account closure."),
        ("Inspect links", "Check a link's destination carefully before opening it."),
        ("Protect private information", "Never share passwords, OTPs, or banking details in response to unexpected requests."),
        ("Verify independently", "Contact the organization through its official website or a known phone number."),
        ("Report suspicious emails", "Follow your institution's or organization's reporting process."),
    ]
    for title, description in tips:
        with st.expander(title):
            st.write(description)

# ---------- Footer ----------
st.divider()
st.caption(
    "PhishGuard •  This is a basic rule-based detector and may miss phishing emails or flag legitimate ones. "
    "Scan history is stored only for the current Streamlit session."
)
