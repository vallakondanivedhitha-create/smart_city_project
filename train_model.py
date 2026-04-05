import pandas as pd
import random
from datetime import datetime
import numpy as np
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

# -------------------------
# FEATURE EXTRACTION
# -------------------------
def extract_features(img):
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    edges = cv2.Canny(gray, 50, 150)
    edge_density = np.sum(edges) / (gray.shape[0] * gray.shape[1])
    return [brightness, edge_density]

# -------------------------
# TRAIN MODEL
# -------------------------
def train_model():
    X = [
        [80, 30],   # pothole
        [90, 28],
        [160, 5],   # streetlight
        [170, 4],
        [70, 10],   # garbage
        [85, 12]
    ]
    y = [
        "Road Damage / Pothole",
        "Road Damage / Pothole",
        "Streetlight Issue",
        "Streetlight Issue",
        "Garbage Issue",
        "Garbage Issue"
    ]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

# -------------------------
# DETECT ISSUE
# -------------------------
def detect_issue(img):
    width, height = img.size
    if width < 200 or height < 200:
        return "Invalid"
    features = extract_features(img)
    result = model.predict([features])[0]
    return result

# -------------------------
# GET LOCATION (SIMULATED GPS)
# -------------------------
def get_location():
    # Replace with real GPS API if deploying on mobile
    return "Detected Location via GPS", [17.385, 78.486]  # demo coordinates

# -------------------------
# SAVE REPORT
# -------------------------
def save_report(issue, location, description, priority):
    data = {
        "Issue": issue,
        "Location": location,
        "Description": description,
        "Priority": priority,
        "Status": "Pending",
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Value": random.randint(1, 100)
    }
    df = pd.DataFrame([data])
    try:
        old = pd.read_csv("reports.csv")
        df = pd.concat([old, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv("reports.csv", index=False)

# -------------------------
# CLUSTER REPORTS
# -------------------------
def cluster_reports():
    try:
        df = pd.read_csv("reports.csv")
        if len(df) >= 2:
            kmeans = KMeans(n_clusters=min(3, len(df)), random_state=0)
            df['Cluster'] = kmeans.fit_predict(df[['Value']])
        else:
            df['Cluster'] = 0
        return df
    except FileNotFoundError:
        return None