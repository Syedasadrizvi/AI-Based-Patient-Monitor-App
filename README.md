# AI-Based-Patient-Monitor-App[README.md](https://github.com/user-attachments/files/25312280/README.md)
---

# 🏥 AI-Based Patient Monitor

An Agentic AI-powered ICU monitoring prototype that reads patient vital data from CSV files, detects abnormalities, and generates AI-driven clinical recommendations.

---

## 🚀 Features

* Reads ICU patient data (.CSV)
* Detects abnormal vitals (HR, BP, Temp, SpO₂)
* Uses LLM for diagnosis and suggested nurse actions
* Escalates to:

  * ⚠️ Rapid Response
  * 🚨 Code Blue
* Displays flashing emergency alerts
* Tracks AI telemetry (tokens + latency)

---

## 📂 Project Structure

```
.
├── app.py
├── data/
│   ├── patient1_sepsis.csv
│   ├── patient2_vtach.csv
│   ├── patient3_respiratory_failure.csv
├── requirements.txt
└── README.md
```

---

## 📊 CSV Format

Each file contains 60 minutes of 1-minute interval vitals:

* patient_id
* timestamp
* ECG
* heart_rate_bpm
* temperature_c
* bp_systolic_mmHg
* bp_diastolic_mmHg
* spo2_percent

---

## ▶️ Run the App

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your API key:

```bash
export OPENAI_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Load patient CSV
2. Detect abnormal vitals
3. Send recent data to LLM
4. LLM returns structured diagnosis
5. App displays severity + recommended actions
6. Shows AI telemetry (tokens & latency)

---

