# ⏳ CGT (TCE) System Analyzer

This is a lightweight, interactive web application built with Python and Streamlit to visualize simulation data from the **Cyclical Gradient Time (CGT)** system.

## 🚀 Features
- **Data Ingestion**: Automatically loads `CGT_center_simulation 1.csv`.
- **Interactive Charts**: Powered by Plotly for zooming, panning, and detailed inspection.
- **Dynamic Controls**: Sidebar for selecting X-axis and multiple Y-axis variables.
- **Statistics**: Instant summary statistics for all selected system variables.

## 🛠️ Local Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/VegaLensSyStem/cgt-system-analyzer.git
   cd cgt-system-analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment
This app is ready to be deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). Simply connect your GitHub account and point to this repository!
