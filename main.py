import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
import os
import sys

# --- DYNAMIC PATH FIX ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.data_loader import load_employee_data
from src.engine.ga_optimizer import TeamOptimizer
from src.analysis.sna_generator import generate_sna
from src.engine.management_logic import calculate_team_metrics, get_belbin_role, prepare_heatmap_data

# --- MODERN SaaS THEME CONFIG ---
st.set_page_config(page_title="TeamSync AI Enterprise", page_icon="🧬", layout="wide")

COLOR_PRIMARY = "#4F46E5"  # Indigo
COLOR_ACCENT = "#1E3A8A"   # Deep Blue
COLOR_BG = "#F8FAFC"       # Off-white
COLOR_SIDEBAR = "#E2E8F0"  # Cool Gray
COLOR_TEXT = "#0F172A"     # Dark Slate

st.markdown(f"""
    <style>
    .main {{ background-color: {COLOR_BG}; color: {COLOR_TEXT}; }}
    [data-testid="stSidebar"] {{ background-color: {COLOR_SIDEBAR}; }}
    
    div.stButton > button {{
        background-color: {COLOR_PRIMARY};
        color: white;
        border-radius: 6px;
        font-weight: 600;
        width: 100%;
        border: none;
    }}
    div.stButton > button:hover {{ background-color: #4338CA; }}
    
    .graph-card {{
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 30px;
        background: white;
        margin-bottom: 35px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    
    [data-testid="stMetric"] {{
        background-color: white;
        border: 1px solid #E2E8F0;
        padding: 15px;
        border_radius: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING ---
df = load_employee_data()

# --- BRANDING HEADER ---
st.markdown(f"""
    <div style="text-align: center; padding: 10px 0px 30px 0px;">
        <h1 style="color: {COLOR_TEXT}; font-family: 'Inter', sans-serif; font-size: 3.2rem; font-weight: 800; letter-spacing: -1.5px; margin-bottom: 0;">
            TeamSync-AI
        </h1>
        <p style="color: #64748B; font-size: 1.1rem; font-weight: 400;">
            Strategic Human Capital Optimization & Network Analytics
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR: STRATEGIC CONFIG ---
with st.sidebar:
    st.title("⚙️ Strategic Config")
    budget = st.number_input("Portfolio Budget ($)", 100000, 1000000, 500000)
    all_skills = sorted(df['Primary_Skill'].unique().tolist())
    required_skills = st.multiselect("Critical Tech Stack:", all_skills)
    team_size = st.slider("Target Team Capacity", 3, 6, 4)
    
    st.markdown("---")
    if st.button("🚀 EXECUTE AI OPTIMIZATION"):
        optimizer = TeamOptimizer(df, team_size)
        optimized_team = optimizer.run()
        # FIX: Ensure Belbin_Role exists before any graph renders
        optimized_team['Belbin_Role'] = optimized_team.apply(get_belbin_role, axis=1)
        st.session_state['current_team'] = optimized_team

    all_names = df['Name'].tolist()
    manual_selection = st.multiselect("Manual Team Interchange:", options=all_names)
    if st.button("🔄 APPLY MANUAL SELECTION"):
        if manual_selection:
            manual_team = df[df['Name'].isin(manual_selection)].copy()
            manual_team['Belbin_Role'] = manual_team.apply(get_belbin_role, axis=1)
            st.session_state['current_team'] = manual_team

# --- MAIN DASHBOARD FLOW ---
if 'current_team' in st.session_state:
    team = st.session_state['current_team']
    safety = calculate_team_metrics(team)
    total_cost = team['Annual_Salary'].sum()

    # --- ROW 1: KPIs ---
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("SAFETY INDEX", f"{safety}/10")
    m2.metric("BUDGET UTIL", f"{(total_cost/budget)*100:.1f}%")
    m3.metric("TENURE AVG", f"{team['Years_Exp'].mean():.1f} YRS")
    m4.metric("ROI SCORE", f"{team['Past_Performance'].mean():.1f}/5.0")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- SECTION 1: Strategic Competency Matrix ---
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Strategic Competency Matrix")
    
    h_df = prepare_heatmap_data(team, required_skills).set_index('Name')
    fig_heat = px.imshow(h_df, color_continuous_scale=["#EFF6FF", "#3B82F6", "#1E3A8A"], text_auto=True)
    st.plotly_chart(fig_heat, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION 2: Cohesion Index ---
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    st.subheader("🧬 Cohesion Index")
    
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=safety,
        title={'text': "Psychological Safety Score", 'font': {'size': 18, 'color': COLOR_TEXT}},
        gauge={
            'axis': {'range': [0, 10]},
            'bar': {'color': COLOR_PRIMARY},
            'steps': [
                {'range': [0, 4], 'color': "#FEE2E2"},
                {'range': [4, 7], 'color': "#FEF3C7"},
                {'range': [7, 10], 'color': "#D1FAE5"}
            ],
            'threshold': {'line': {'color': COLOR_ACCENT, 'width': 4}, 'value': 8.5}
        }))
    fig_gauge.update_layout(height=400, margin=dict(t=80, b=20), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION 3: Communication Flux ---
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    st.subheader("🕸️ Communication Flux")
    
    # Analytical Metrics Header
    c1, c2, c3 = st.columns(3)
    c1.write(f"**Network Leader:** ⭐ {team.iloc[0]['Name']}")
    c2.write(f"**Network Density:** 📊 {(safety/10):.2f}")
    c3.write(f"**Strategic Bridge:** 🔗 {team.iloc[-1]['Name']}")
    
    st.markdown("---")
    
    generate_sna(team)
    if os.path.exists("team_network.html"):
        with open("team_network.html", 'r', encoding='utf-8') as f:
            components.html(f.read(), height=500)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION 4: Executive Roster ---
    st.markdown('<div class="graph-card">', unsafe_allow_html=True)
    st.subheader("📋 Executive Strategic Roster")
    display_df = team[['Name', 'Belbin_Role', 'Primary_Skill', 'Annual_Salary']].copy()
    display_df['Annual_Salary'] = display_df['Annual_Salary'].apply(lambda x: f"${x:,}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👈 Initialize the AI Optimization or Manual Selection from the sidebar.")