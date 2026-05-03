import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page config - dark theme
st.set_page_config(
    page_title="Gold Price Prediction System",
    page_icon="🥇",
    layout="wide"
)

# Custom CSS to match Figma dark theme exactly
st.markdown("""
    <style>
    .stApp { background-color: #0a0e1a; }
    .metric-card {
        background-color: #111827;
        border-radius: 12px;
        padding: 30px;
        margin: 5px;
    }
    .metric-label {
        color: #9ca3af;
        font-size: 16px;
        margin-bottom: 10px;
    }
    .metric-value {
        color: #f59e0b;
        font-size: 36px;
        font-weight: bold;
    }
    .title-gold { color: #f59e0b; }
    .title-white { color: white; }
    </style>
""", unsafe_allow_html=True)

# Title - "Gold" in orange, rest in white like Figma
st.markdown("""
    <h1>
        <span class="title-gold">Gold</span>
        <span class="title-white"> Price Prediction System</span>
    </h1>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("final_dataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Get daily average close price (one row per date)
daily = df.groupby('Date')['Close'].mean().reset_index()

# --- 3 Metric Cards ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Records</div>
            <div class="metric-value">{len(daily)}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Number of Features</div>
            <div class="metric-value">{len(df.columns)}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    start_year = daily['Date'].dt.year.min()
    end_year = daily['Date'].dt.year.max()
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Date Range</div>
            <div class="metric-value">{start_year} - {end_year}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Gold Price Over Time Chart ---
st.markdown("""
    <div style="background-color:#111827; border-radius:12px; padding:25px;">
        <p style="color:white; font-size:18px; font-weight:600;">Gold Price Over Time</p>
    </div>
""", unsafe_allow_html=True)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=daily['Date'],
    y=daily['Close'],
    mode='lines',
    name='Gold Price',
    line=dict(color='#f59e0b', width=2)
))

fig.update_layout(
    paper_bgcolor='#111827',
    plot_bgcolor='#111827',
    font=dict(color='white'),
    xaxis=dict(
        title='Date',
        gridcolor='#1f2937',
        color='white'
    ),
    yaxis=dict(
        title='Price (USD)',
        gridcolor='#1f2937',
        color='white'
    ),
    margin=dict(l=20, r=20, t=20, b=20),
    height=400
)

st.plotly_chart(fig, use_container_width=True)