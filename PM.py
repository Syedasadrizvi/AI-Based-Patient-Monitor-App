import streamlit as st
import pandas as pd
import time
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Based ICU Patient Monitor")

uploaded_file = st.file_uploader("Upload Patient CSV", type=["csv"])

def local_abnormality_detection(df):
    latest = df.iloc[-1]

    alerts = []

    if latest["temperature_c"] > 39:
        alerts.append("High Fever")

    if latest["heart_rate_bpm"] > 130:
        alerts.append("Severe Tachycardia")

    if latest["bp_systolic_mmHg"] < 90:
        alerts.append("Hypotension")

    if latest["spo2_percent"] < 90:
        alerts.append("Hypoxemia")

    if latest["ECG"] == "V-Tach":
        alerts.append("Ventricular Tachycardia")

    return alerts

def ai_diagnosis(summary):
    start_time = time.time()

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an ICU clinical decision support AI."},
            {"role": "user", "content": summary}
        ]
    )

    latency = time.time() - start_time

    return response, latency

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.line_chart(df[["heart_rate_bpm", "temperature_c", "spo2_percent"]])

    alerts = local_abnormality_detection(df)

    if alerts:
        st.markdown(
            "<h1 style='color:red;'>🚨 EMERGENCY ALERT 🚨</h1>",
            unsafe_allow_html=True
        )

        summary = f"""
        Patient vitals summary:
        {df.tail(5).to_string()}
        Abnormal findings: {alerts}
        Provide:
        - Diagnosis
        - Severity level
        - Immediate Nurse Actions
        """

        response, latency = ai_diagnosis(summary)

        st.write(response["choices"][0]["message"]["content"])

        st.subheader("AI Telemetry")
        st.write("Latency:", latency)
        st.write("Input Tokens:", response["usage"]["prompt_tokens"])
        st.write("Output Tokens:", response["usage"]["completion_tokens"])
