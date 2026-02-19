import streamlit as st
import pandas as pd
from analysis import analyze_data, structure_dataset

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="DataSight | Investor Demo",
    layout="wide"
)

# ---------------- LOGIN STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
    <div style="
        max-width:420px;
        margin: 120px auto;
        padding: 2.8rem;
        background: rgba(10, 15, 30, 0.85);
        border-radius: 26px;
        box-shadow: 0 30px 80px rgba(0,0,0,0.8);
        animation: slideLogin 1.2s ease-out;
        ">
        <h1 style="text-align:center;">🔐 DataSight</h1>
        <p style="text-align:center;">Secure Enterprise Login</p>
    </div>

    <style>
    @keyframes slideLogin {
        from { opacity: 0; transform: translateY(80px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    email = st.text_input("Company Email")
    password = st.text_input("Password", type="password")

    if st.button("🚀 Continue to Dashboard"):
        st.session_state.logged_in = True
        st.rerun()

    st.stop()

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #020024, #090979, #000000);
    background-size: 400% 400%;
    animation: bgMove 18s ease infinite;
}
@keyframes bgMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.block-container {
    background: rgba(10,15,30,0.8);
    border-radius: 24px;
    padding: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<h1>🚀 DataSight</h1>
<h3>Enterprise Analytics. Reimagined.</h3>
<p>Upload messy data → get clean, structured insights in seconds.</p>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # -------- STRUCTURING --------
    st.markdown("## 🧹 Automatic Data Structuring")
    structured_df = structure_dataset(df)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ❌ Original Dataset")
        st.dataframe(df.head(10), use_container_width=True)

    with col2:
        st.markdown("### ✅ Structured Dataset")
        st.dataframe(structured_df.head(10), use_container_width=True)

    # -------- METRICS --------
    st.markdown("## 📊 Dataset Health")
    results = analyze_data(structured_df)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", results["rows"])
    c2.metric("Columns", results["columns"])
    c3.metric("Missing Values", results["missing"])
    c4.metric("Duplicates", results["duplicates"])

# ---------------- FOOTER ----------------
st.markdown("""
<hr>
<p style="text-align:center; font-size:14px;">
© 2026 DataSight · Investor Demo · Built by Vyshnav
</p>
""", unsafe_allow_html=True)
