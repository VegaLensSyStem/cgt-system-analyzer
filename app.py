import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Page Configuration
st.set_page_config(
    page_title="CGT System Analyzer",
    page_icon="⏳",
    layout="wide"
)

# 2. Main Title and Description
st.title("⏳ CGT (TCE) System Analyzer")
st.markdown("""
**Cyclical Gradient Time (CGT) Simulation Dashboard.**
This tool visualizes the dynamic evolution of the system variables based on the `CGT_center_simulation 1.csv` data.
""")

# 3. Data Loading Function
@st.cache_data
def load_data(filename):
    if not os.path.exists(filename):
        return None
    return pd.read_csv(filename)

# Define the file path (Must match your uploaded file exactly)
FILE_PATH = 'CGT_center_simulation 1.csv'

# Load the data
df = load_data(FILE_PATH)

# 4. Main Logic
if df is not None:
    # --- Sidebar Controls ---
    st.sidebar.header("Plot Configuration")
    
    # Get all available columns
    all_columns = df.columns.tolist()
    
    # X-Axis Selection (Try to find 't' or 'time' automatically, otherwise use index 0)
    default_x = 't' if 't' in all_columns else all_columns[0]
    x_axis = st.sidebar.selectbox("Select X-Axis (Time Domain):", all_columns, index=all_columns.index(default_x))
    
    # Y-Axis Selection (Multi-select)
    # Default to the next two columns after X
    default_y = [col for col in all_columns if col != x_axis][:2]
    y_axis = st.sidebar.multiselect(
        "Select Y-Axis (System Variables):", 
        all_columns, 
        default=default_y
    )

    # --- Visualization ---
    st.subheader(f"System Dynamics: {', '.join(y_axis)}")
    
    if y_axis:
        # Create Plotly Line Chart
        fig = px.line(
            df, 
            x=x_axis, 
            y=y_axis, 
            title=f'CGT Simulation Analysis over {x_axis}',
            markers=False
        )
        
        # Customize Layout
        fig.update_layout(
            hovermode="x unified",
            height=600,
            xaxis_title=x_axis,
            yaxis_title="Value",
            template="plotly_dark"  # Dark theme for better contrast
        )
        
        # Display Chart
        st.plotly_chart(fig, use_container_width=True)
        
        # --- Statistics Section ---
        st.markdown("### 📊 Key Statistics")
        st.write(df[y_axis].describe())
        
    else:
        st.info("Please select at least one variable for the Y-Axis to visualize data.")

    # --- Raw Data Expander ---
    with st.expander("View Raw Simulation Data"):
        st.dataframe(df)

else:
    # Error Message if file is missing
    st.error(f"❌ File not found: `{FILE_PATH}`")
    st.warning("Please ensure the CSV file is in the same directory as this script.")
