# Predictive Maintenance on NASA CMAPSS (FD001)
End‑to‑end machine learning system for predicting Remaining Useful Life (RUL) of turbofan jet engines using the NASA CMAPSS dataset.  
This project includes data processing, model training, evaluation, and a fully deployed FastAPI inference service.

---

## 🚀 Project Overview
Modern aerospace systems rely on predictive maintenance to prevent unexpected failures, reduce downtime, and improve mission readiness.  
This project builds a complete RUL prediction pipeline using NASA’s CMAPSS FD001 dataset and deploys the trained model as a real‑time API.

You can send raw sensor readings to the API and receive an estimated RUL instantly.

---

## 📘 Dataset: NASA CMAPSS (FD001)
The CMAPSS dataset simulates degradation of turbofan jet engines under varying operational conditions.

**FD001 characteristics:**
- 100 engines
- Single operating condition
- One fault mode
- 21 sensor measurements per cycle
- RUL decreases until engine failure

This dataset is widely used in aerospace predictive maintenance research.

---

## 🧠 Problem Statement
**Goal:** Predict the Remaining Useful Life (RUL) of an engine at any given cycle using only raw sensor data.

RUL prediction enables:
- Early detection of degradation  
- Optimized maintenance scheduling  
- Reduced operational risk  
- Increased aircraft availability  

---

## 🏗️ System Architecture

┌────────────────────┐
│   Raw NASA Data    │
└─────────┬──────────┘
│
▼
┌──────────────────────────┐
│  Feature Engineering     │
│  (RUL labeling, cleaning)│
└─────────┬───────────────┘
│
▼
┌──────────────────────────┐
│     Model Training       │
│  RandomForest Regressor  │
└─────────┬───────────────┘
│
▼
┌──────────────────────────┐
│   Saved Model + Features │
└─────────┬───────────────┘
│
▼
┌──────────────────────────┐
│        FastAPI           │
│   /predict endpoint      │
└──────────────────────────┘

---

## 📁 Repository Structure

predictive-maintenance-cmapss/
│
├── api/
│   └── main.py
│
├── src/
│   └── predict.py
│
├── models/
│   ├── final_model.pkl
│   └── feature_columns.json
│
├── data/
│   ├── raw/
│   └── processed/
│       └── train_FD001_processed.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
│
├── diagrams/
│   └── system_architecture.png
│
├── requirements.txt
└── README.md

---

## 🧪 Modeling Approach

### **Features Used**
Only raw sensor values:
sensor_1 ... sensor_21

This ensures compatibility with the real‑time API.

### **Model**
- **RandomForestRegressor**
- 200 trees
- Trained on 80/20 split
- Predicts continuous RUL values

### **Why Random Forest?**
- Fast to train  
- Robust to noise  
- Works well with tabular sensor data  
- Easy to deploy  

---

## 📊 Evaluation Results

**Metrics:**
- RMSE: 40.89
- MAE: 28.73


**Predicted vs Actual Plot:**  
(Generated in `03_modeling.ipynb`)

Shows strong correlation between predicted and true RUL.

---

## 🌐 FastAPI Deployment
The model is deployed using FastAPI with a `/predict` endpoint.

### **Run the API**
python -m uvicorn api.main:app --reload

### **Interactive Docs**
Open in browser:
http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

---

## 📥 Example Prediction Request

```json
{
  "sensor_1": 518.67,
  "sensor_2": 642.12,
  "sensor_3": 1580.0,
  "sensor_4": 1400.0,
  "sensor_5": 14.62,
  "sensor_6": 21.61,
  "sensor_7": 554.36,
  "sensor_8": 2388.0,
  "sensor_9": 9046.0,
  "sensor_10": 1.30,
  "sensor_11": 47.00,
  "sensor_12": 521.00,
  "sensor_13": 2388.00,
  "sensor_14": 813.00,
  "sensor_15": 8.00,
  "sensor_16": 0.03,
  "sensor_17": 392.00,
  "sensor_18": 2388.00,
  "sensor_19": 100.00,
  "sensor_20": 39.00,
  "sensor_21": 23.00
}
Example Response
{
  "predicted_RUL": 202.45
}
```markdown
---

## 🛠️ How to Run the Project Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/predictive-maintenance-cmapss.git

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the API
python -m uvicorn api.main:app --reload
