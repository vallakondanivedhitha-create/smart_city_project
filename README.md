# 🏙 Smart City Issue Reporter (AI + Geo-Tagging)

A citizen-focused web app to report city issues like **potholes, streetlights, and garbage** using AI/ML and geolocation.

---

## 🔹 Features

* Login / Register / Forgot Password / Google Login
* AI/ML issue detection from uploaded images
* Location via **GPS** or **Manual Entry**
* Add description & priority (Low / Medium / High)
* Submit reports → saved in CSV
* View all reports & **KMeans clustering** visualization
* Fraud detection for invalid images (max 3 attempts)

---

## 🔹 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python, Pandas, NumPy, scikit-learn
* **ML / AI:** RandomForestClassifier for image classification
* **Visualization:** Matplotlib

---

## 🔹 Installation

```bash
git clone <repo-link>
cd smart_city_project
python -m venv myenv
myenv\Scripts\activate  # Windows
pip install streamlit pandas matplotlib scikit-learn numpy Pillow opencv-python
```

---

## 🔹 Running

```bash
python -m streamlit run main.py
```

Open the link shown in terminal (`http://localhost:8501`).

---

## 🔹 Usage

1. **Login / Register** (or use Google login)
2. **Upload Image** → AI detects issue type
3. **Location**: choose GPS detect or manual entry
4. **Add Description & Priority**
5. **Submit Report** → saved in CSV
6. **View Reports & Clusters** → table + scatter graph

---

## 🔹 Code Structure

```text
smart_city_project/
├── backend.py
├── frontend.py
├── main.py
├── reports.csv
├── README.md
```


## 🔹 Future Improvements

* Real GPS tracking for mobile
* Interactive map for location selection
* More ML models for better detection
* Admin dashboard for report management