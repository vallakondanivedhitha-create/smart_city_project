import streamlit as st
from PIL import Image
from train_model import detect_issue, get_location, save_report, cluster_reports
import matplotlib.pyplot as plt

def run_frontend():
    st.title("🏙 Smart City Issue Reporter")

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    if "detected_location" not in st.session_state:
        st.session_state.detected_location = ""

    # -------------------------
    # IMAGE UPLOAD
    # -------------------------
    file = st.file_uploader("📸 Upload Issue Image", type=["jpg", "png", "jpeg"])

    # -------------------------
    # LOCATION SELECTION
    # -------------------------
    st.subheader("📍 Location")
    location_option = st.radio("Choose location method:", ["GPS Detect", "Manual Entry"])

    if location_option == "GPS Detect":
        if st.button("📡 Detect Location via GPS"):
            loc, coords = get_location()
            st.session_state.detected_location = loc
            st.success(f"Detected: {loc}")
    else:
        manual_loc = st.text_input("Enter location manually")
        st.session_state.detected_location = manual_loc

    # -------------------------
    # ISSUE DETAILS
    # -------------------------
    st.subheader("📝 Issue Details")
    description = st.text_area("Describe the issue")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    # -------------------------
    # IMAGE PROCESSING
    # -------------------------
    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Image", width=400)

        issue = detect_issue(img)

        if issue == "Invalid":
            st.session_state.attempts += 1
            st.warning(f"⚠️ Invalid Image! Attempts left: {3 - st.session_state.attempts}")
            if st.session_state.attempts >= 3:
                st.error("🚫 Fraud detected! Upload blocked")
                st.stop()
        else:
            st.success(f"✅ Detected Issue: {issue}")

    # -------------------------
    # SUBMIT REPORT
    # -------------------------
    if st.button("📤 Submit Report"):
        if file is None:
            st.error("❗ Upload an image first")
        elif st.session_state.detected_location == "":
            st.error("❗ Provide location either by GPS or manually")
        else:
            save_report(issue, st.session_state.detected_location, description, priority)
            st.success("🚀 Report submitted successfully!")

    # -------------------------
    # SHOW REPORTS + CLUSTERING
    # -------------------------
    st.subheader("📊 All Reports & Clusters")
    df = cluster_reports()
    if df is not None:
        st.dataframe(df)

        # Cluster Visualization Graph
        fig, ax = plt.subplots(figsize=(6,4))
        for cluster in df['Cluster'].unique():
            temp = df[df['Cluster'] == cluster]
            ax.scatter(temp.index, temp['Value'], label=f"Cluster {cluster}")
        ax.set_xlabel("Report Index")
        ax.set_ylabel("Value")
        ax.set_title("Cluster Visualization")
        ax.legend()
        st.pyplot(fig)
    else:
        st.info("No reports yet")