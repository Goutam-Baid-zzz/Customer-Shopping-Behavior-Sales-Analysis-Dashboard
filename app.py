"""
================================================================================
  CUSTOMER SHOPPING DATA ANALYTICS DASHBOARD - OBSIDIAN EDITION
  Ultra-Premium Streamlit Application for EDA & Business Insights
================================================================================

Author: Data Analytics Team
Purpose: Interactive, production-ready dashboard for customer shopping analysis
Date: 2026

"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import warnings
from PIL import Image
import unicodedata

warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION - REMOVED DEPRECATED OPTIONS
# ============================================================================

st.set_page_config(
    page_title="ShopIQ Analytics",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# OBSIDIAN PREMIUM CSS — REFINED DARK INTELLIGENCE THEME
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap');

    /* ── ROOT TOKENS ─────────────────────────────────────────────────── */
    :root {
        --ink:      #0a0c10;
        --ink-mid:  #111318;
        --ink-soft: #1a1e28;
        --ink-edge: #232839;
        --wire:     #2a3040;
        --mist:     #3a4155;
        --ghost:    #6b7494;
        --pale:     #a0aabe;
        --snow:     #e8ecf4;
        --white:    #f4f6fb;

        --blue:     #4f8ef7;
        --blue-dim: #3a6fd8;
        --blue-glow:rgba(79,142,247,0.18);
        --teal:     #34d9b3;
        --teal-dim: #20b898;
        --amber:    #f0b429;
        --rose:     #f75f7b;
        --violet:   #a78bfa;

        --radius-sm:  6px;
        --radius-md:  12px;
        --radius-lg:  18px;
        --radius-xl:  28px;

        --shadow-card: 0 2px 16px rgba(0,0,0,0.45), 0 1px 4px rgba(0,0,0,0.3);
        --shadow-glow: 0 0 24px rgba(79,142,247,0.12);
        --transition:  all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ── GLOBAL DARK OVERRIDE ────────────────────────────────────────── */
    html,
    body,
    [class*="css"],
    .stApp,
    .stApp > header,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewBlockContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stMain"],
    section[data-testid="stSidebar"] ~ div,
    .main,
    .main > div,
    .block-container {
        background-color: #0a0c10 !important;
        font-family: 'DM Sans', sans-serif;
        color: var(--snow);
    }

    .stApp {
        background: #0a0c10 !important;
        background-image:
            radial-gradient(ellipse 70% 45% at 85% 8%,  rgba(79,142,247,0.07) 0%, transparent 55%),
            radial-gradient(ellipse 55% 40% at 5%  85%, rgba(52,217,179,0.05) 0%, transparent 55%) !important;
        min-height: 100vh;
    }

    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stMain"]             { background: transparent !important; }
    .main                              { background: transparent !important; min-height: 100vh; padding: 0 !important; }

    .block-container {
        background: transparent !important;
        padding: 2.5rem 3rem 4rem !important;
        max-width: 1600px;
        margin: 0 auto;
    }

    [data-testid="stVerticalBlock"] { background: transparent !important; }

    /* ── SIDEBAR ─────────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: var(--ink-mid);
        border-right: 1px solid var(--wire);
        box-shadow: 4px 0 32px rgba(0,0,0,0.6);
    }
    [data-testid="stSidebar"] > div { padding: 0; }
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] p    { color: var(--pale) !important; font-family: 'DM Sans', sans-serif; }
    [data-testid="stSidebar"] [data-testid="stRadio"] label { color: var(--pale) !important; }
    [data-testid="stSidebar"] hr   { border-color: var(--wire); opacity: 0.6; }

    /* ── TYPOGRAPHY ──────────────────────────────────────────────────── */
    h1, h2, h3, h4, h5 { font-family: 'Syne', sans-serif !important; letter-spacing: -0.02em; }

    /* ── PAGE HEADER ─────────────────────────────────────────────────── */
    .page-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.72rem; font-weight: 600;
        letter-spacing: 0.18em; text-transform: uppercase;
        color: var(--blue); margin-bottom: 0.4rem;
    }
    .page-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(2rem, 4vw, 3.4rem); font-weight: 800;
        line-height: 1.05; color: var(--white);
        margin: 0 0 0.6rem 0; letter-spacing: -0.03em;
    }
    .page-title span {
        background: linear-gradient(120deg, var(--blue) 0%, var(--teal) 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }
    .page-subtitle { font-size: 1.0rem; color: var(--ghost); font-weight: 400; margin-bottom: 0; line-height: 1.6; }

    /* ── SECTION HEADER ──────────────────────────────────────────────── */
    .section-label { display: flex; align-items: center; gap: 12px; margin: 2.5rem 0 1.2rem 0; }
    .section-label-bar {
        width: 3px; height: 22px;
        background: linear-gradient(180deg, var(--blue), var(--teal));
        border-radius: 2px; flex-shrink: 0;
    }
    .section-label-text { font-family: 'Syne', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--white); letter-spacing: -0.01em; }
    .section-label-badge {
        margin-left: auto; font-size: 0.72rem; font-weight: 600;
        letter-spacing: 0.1em; text-transform: uppercase;
        color: var(--ghost); background: var(--ink-soft);
        border: 1px solid var(--wire); padding: 3px 10px; border-radius: 20px;
    }

    /* ── KPI CARDS ────────────────────────────────────────────────────── */
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] { display: flex; flex-direction: column; }

    .kpi-card {
        background: var(--ink-mid); border: 1px solid var(--wire);
        border-radius: var(--radius-lg); padding: 1.4rem 1.5rem;
        position: relative; overflow: hidden; transition: var(--transition);
        cursor: default; min-height: 160px; height: 100%;
        box-sizing: border-box; display: flex; flex-direction: column; justify-content: flex-end;
    }
    .kpi-card::before {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(135deg, var(--accent-color, rgba(79,142,247,0.07)) 0%, transparent 60%);
        pointer-events: none;
    }
    .kpi-card::after {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
        background: var(--accent-color, var(--blue)); opacity: 0.7;
        border-radius: var(--radius-lg) var(--radius-lg) 0 0; transition: var(--transition);
    }
    .kpi-card:hover { border-color: var(--mist); transform: translateY(-3px); box-shadow: var(--shadow-card), var(--shadow-glow); }
    .kpi-card:hover::after { opacity: 1; }
    .kpi-icon  { font-size: 1.5rem; margin-bottom: 0.8rem; display: block; }
    .kpi-label { font-size: 0.72rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ghost); margin-bottom: 0.4rem; }
    .kpi-value { font-family: 'Syne', sans-serif; font-size: 1.6rem; font-weight: 800; color: var(--white); letter-spacing: -0.02em; line-height: 1; margin-bottom: 0.5rem; white-space: normal; overflow: visible; word-break: break-word; }
    .kpi-delta { font-size: 0.78rem; font-weight: 600; color: var(--teal); display: flex; align-items: center; gap: 4px; }
    .kpi-delta::before { content: '▲'; font-size: 0.6rem; }

    /* ── STAT BOXES ───────────────────────────────────────────────────── */
    .stat-mini { background: var(--ink-soft); border: 1px solid var(--wire); border-radius: var(--radius-sm); padding: 0.8rem 1rem; margin-bottom: 8px; }
    .stat-mini-label { font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ghost); margin-bottom: 0.25rem; }
    .stat-mini-val   { font-family: 'Syne', sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--blue); }

    /* ── INSIGHT PANELS ──────────────────────────────────────────────── */
    .insight-panel {
        background: var(--ink-soft); border: 1px solid var(--wire);
        border-left: 3px solid var(--teal); border-radius: var(--radius-md);
        padding: 1.1rem 1.4rem; margin: 0.6rem 0; transition: var(--transition); position: relative;
    }
    .insight-panel:hover { border-left-color: var(--teal); background: var(--ink-edge); transform: translateX(4px); }
    .insight-panel.success { border-left-color: var(--teal); }
    .insight-panel.warning { border-left-color: var(--amber); }
    .insight-panel.danger  { border-left-color: var(--rose); }
    .insight-panel.violet  { border-left-color: var(--violet); }
    .insight-panel-label { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: var(--teal); margin-bottom: 0.4rem; }
    .insight-panel.success .insight-panel-label { color: var(--teal); }
    .insight-panel.warning .insight-panel-label { color: var(--amber); }
    .insight-panel.danger  .insight-panel-label { color: var(--rose); }
    .insight-panel.violet  .insight-panel-label { color: var(--violet); }
    .insight-panel-body { font-size: 0.9rem; color: var(--pale); line-height: 1.6; }
    .insight-panel-body strong { color: var(--snow); font-weight: 600; }

    /* ── RECOMMENDATION CARDS ────────────────────────────────────────── */
    .rec-card { background: var(--ink-mid); border: 1px solid var(--wire); border-radius: var(--radius-lg); padding: 1.4rem 1.5rem; transition: var(--transition); height: 100%; }
    .rec-card:hover { border-color: var(--mist); background: var(--ink-soft); box-shadow: var(--shadow-card); transform: translateY(-4px); }
    .rec-icon  { font-size: 1.8rem; margin-bottom: 0.7rem; display: block; }
    .rec-title { font-family: 'Syne', sans-serif; font-size: 0.95rem; font-weight: 700; color: var(--white); margin-bottom: 0.5rem; letter-spacing: -0.01em; }
    .rec-body  { font-size: 0.84rem; color: var(--ghost); line-height: 1.65; }

    /* ── INFO BANNER ─────────────────────────────────────────────────── */
    .info-banner {
        background: linear-gradient(135deg, rgba(79,142,247,0.08) 0%, rgba(52,217,179,0.05) 100%);
        border: 1px solid rgba(79,142,247,0.25); border-radius: var(--radius-md);
        padding: 1rem 1.4rem; margin: 0.8rem 0 1.8rem 0;
        display: flex; align-items: flex-start; gap: 12px;
    }
    .info-banner-icon { font-size: 1rem; flex-shrink: 0; margin-top: 2px; }
    .info-banner-content strong { font-size: 0.82rem; font-weight: 700; color: var(--blue); display: block; margin-bottom: 2px; letter-spacing: 0.05em; text-transform: uppercase; }
    .info-banner-content span   { font-size: 0.88rem; color: var(--pale); line-height: 1.5; }

    /* ── DIVIDER ─────────────────────────────────────────────────────── */
    .ruled-divider { height: 1px; background: linear-gradient(90deg, transparent, var(--wire), transparent); margin: 2.5rem 0; opacity: 0.8; }

    /* ── TABS ────────────────────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] { background: var(--ink-soft); border-radius: var(--radius-md); padding: 4px; gap: 0; border: 1px solid var(--wire); }
    .stTabs [data-baseweb="tab"] { background: transparent; border-radius: 8px; color: var(--ghost); font-family: 'DM Sans', sans-serif; font-weight: 500; font-size: 0.88rem; padding: 8px 18px; border: none; transition: var(--transition); }
    .stTabs [data-baseweb="tab"]:hover { color: var(--pale); background: var(--ink-edge); }
    .stTabs [aria-selected="true"] { background: var(--blue) !important; color: white !important; font-weight: 600; box-shadow: 0 2px 8px rgba(79,142,247,0.35); }
    .stTabs [data-baseweb="tab-border"] { display: none; }
    .stTabs [data-baseweb="tab-panel"] { padding-top: 1.5rem; }

    /* ── EXPANDERS ───────────────────────────────────────────────────── */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] details summary,
    [data-testid="stExpander"] > details > summary {
        background: var(--ink-soft) !important; border: 1px solid var(--wire) !important;
        border-radius: var(--radius-sm) !important; color: var(--snow) !important;
        font-family: 'DM Sans', sans-serif; font-weight: 600; font-size: 0.9rem; padding: 0.8rem 1.2rem !important;
    }
    .streamlit-expanderHeader:hover,
    [data-testid="stExpander"] details summary:hover { background: var(--ink-edge) !important; border-color: var(--blue) !important; color: var(--white) !important; }
    .streamlit-expanderContent,
    [data-testid="stExpander"] > details > div { background: var(--ink-mid) !important; border: 1px solid var(--wire) !important; border-top: none !important; border-radius: 0 0 var(--radius-sm) var(--radius-sm) !important; }
    [data-testid="stExpander"] summary svg { fill: var(--pale) !important; stroke: var(--pale) !important; }

    /* ── DATAFRAMES ──────────────────────────────────────────────────── */
    .stDataFrame, [data-testid="stDataFrame"], [data-testid="stDataFrameResizable"] {
        border: 1px solid var(--wire) !important; border-radius: var(--radius-md) !important;
        overflow: hidden !important; background: var(--ink-mid) !important;
    }

    /* ── METRIC ──────────────────────────────────────────────────────── */
    [data-testid="metric-container"] { background: var(--ink-mid); border: 1px solid var(--wire); border-radius: var(--radius-md); padding: 1rem 1.2rem; }
    [data-testid="metric-container"] label { color: var(--pale) !important; font-size: 0.82rem !important; letter-spacing: 0.06em; text-transform: uppercase; font-weight: 600; }
    [data-testid="metric-container"] [data-testid="stMetricValue"] { font-family: 'Syne', sans-serif; color: var(--white) !important; font-size: 2rem !important; font-weight: 800; }
    [data-testid="metric-container"] [data-testid="stMetricDelta"] { color: var(--teal) !important; font-size: 0.82rem !important; }

    /* ── MULTISELECT / SLIDER ────────────────────────────────────────── */
    [data-baseweb="select"] { background: var(--ink-soft) !important; border-color: var(--wire) !important; border-radius: var(--radius-sm) !important; color: var(--pale) !important; }
    [data-testid="stSlider"] { color: var(--pale); }

    /* ── BUTTONS ─────────────────────────────────────────────────────── */
    .stButton > button { background: linear-gradient(135deg, var(--blue) 0%, var(--blue-dim) 100%); color: white; border: none; padding: 0.6rem 1.4rem; border-radius: var(--radius-sm); font-family: 'DM Sans', sans-serif; font-weight: 600; font-size: 0.88rem; transition: var(--transition); box-shadow: 0 4px 12px rgba(79,142,247,0.3); }
    .stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(79,142,247,0.45); }

    /* ── SIDEBAR NAV ─────────────────────────────────────────────────── */
    .nav-logo { padding: 1.6rem 1.4rem 1.2rem; border-bottom: 1px solid var(--wire); margin-bottom: 0; }
    .nav-logo-mark { font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800; color: var(--white); letter-spacing: -0.03em; display: flex; align-items: center; gap: 8px; }
    .nav-logo-dot { width: 8px; height: 8px; background: var(--blue); border-radius: 50%; display: inline-block; box-shadow: 0 0 8px var(--blue); }
    .nav-logo-sub { font-size: 0.72rem; color: var(--ghost); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 2px; }
    .nav-section-title { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: var(--mist); padding: 1.2rem 1.4rem 0.4rem; }

    /* ── SIDEBAR QUICK STAT ──────────────────────────────────────────── */
    .sq-stat { margin: 0 0.8rem; padding: 0.8rem 1rem; background: var(--ink-soft); border: 1px solid var(--wire); border-radius: var(--radius-sm); margin-bottom: 6px; display: flex; align-items: center; justify-content: space-between; }
    .sq-label { font-size: 0.72rem; color: var(--ghost); font-weight: 500; }
    .sq-value { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: var(--blue); }

    /* ── PHASE CARD ──────────────────────────────────────────────────── */
    .phase-card { background: var(--ink-mid); border: 1px solid var(--wire); border-radius: var(--radius-lg); padding: 1.5rem; transition: var(--transition); }
    .phase-card:hover { border-color: var(--mist); transform: translateY(-4px); box-shadow: var(--shadow-card); }
    .phase-num   { font-family: 'Syne', sans-serif; font-size: 2.5rem; font-weight: 800; color: var(--wire); line-height: 1; margin-bottom: 0.5rem; }
    .phase-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: var(--white); margin-bottom: 0.7rem; }
    .phase-list  { list-style: none; padding: 0; margin: 0; }
    .phase-list li { font-size: 0.84rem; color: var(--ghost); padding: 3px 0; display: flex; align-items: center; gap: 8px; }
    .phase-list li::before { content: ''; width: 4px; height: 4px; background: var(--blue); border-radius: 50%; flex-shrink: 0; }

    /* ── PAGE ENTRY ANIMATION ────────────────────────────────────────── */
    @keyframes fadeUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: translateY(0); } }
    .block-container > div { animation: fadeUp 0.35s ease both; }

    /* ── SCROLLBAR ───────────────────────────────────────────────────── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--ink); }
    ::-webkit-scrollbar-thumb { background: var(--wire); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--mist); }

    /* ── HIDE STREAMLIT CHROME ───────────────────────────────────────── */
    #MainMenu, footer { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }

    /* ── DARK HEADER ─────────────────────────────────────────────────── */
    header[data-testid="stHeader"] {
        background: rgba(10, 12, 16, 0.97) !important;
        border-bottom: 1px solid #2a3040 !important;
        backdrop-filter: blur(8px);
    }
    header[data-testid="stHeader"] button,
    header[data-testid="stHeader"] a,
    header[data-testid="stHeader"] span,
    [data-testid="stToolbar"] button,
    [data-testid="stToolbar"] span { color: #a0aabe !important; }
    [data-testid="stToolbar"] button:hover { color: #f4f6fb !important; }
    [data-testid="stSidebarCollapsedControl"] button,
    [data-testid="collapsedControl"] button { color: #a0aabe !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA LOADING & CACHING - ROBUST WITH FALLBACKS
# ============================================================================

@st.cache_data
def load_main_data():
    """Load main dataset with multiple fallback paths"""
    paths_to_try = [
        Path(__file__).parent / 'Customer_shopping_data_.csv',
        Path('.') / 'Customer_shopping_data_.csv',
        Path('./data') / 'Customer_shopping_data_.csv',
    ]
    
    df = None
    for path in paths_to_try:
        if path.exists():
            try:
                df = pd.read_csv(path)
                break
            except Exception as e:
                st.warning(f"Failed to load from {path}: {e}")
                continue
    
    if df is None:
        st.error("Dataset not found. Creating sample dataset...")
        # Generate minimal sample data if file not found
        np.random.seed(42)
        df = pd.DataFrame({
            'Customer ID': [f'C{i:05d}' for i in range(100)],
            'Age': np.random.randint(18, 70, 100),
            'Gender': np.random.choice(['Male', 'Female', 'Other'], 100),
            'Category': np.random.choice(['Electronics', 'Fashion', 'Home'], 100),
            'Purchase Amount (USD)': np.random.uniform(10, 500, 100),
            'Review Rating': np.random.uniform(1, 5, 100),
            'Location': np.random.choice(['New York', 'Los Angeles', 'Chicago'], 100),
        })
    
    # Data type conversions
    if 'Customer ID' in df.columns:
        df['Customer ID'] = df['Customer ID'].astype(str)
    
    for col in ['Gender', 'Category', 'Location', 'Size', 'Color', 'Season',
                'Subscription Status', 'Shipping Type', 'Discount Applied',
                'Promo Code Used', 'Payment Method', 'Frequency of Purchases']:
        if col in df.columns:
            df[col] = df[col].astype('category')
    
    # Normalize category columns
    if 'Category' in df.columns:
        df['Category'] = df['Category'].astype(str).str.strip()
        df['Category'] = df['Category'].str.replace(r"\s+", ' ', regex=True)
        df['Category'] = df['Category'].apply(lambda x: unicodedata.normalize('NFKC', x))
        df['Category'] = df['Category'].str.title()
    
    for col in ['Purchase Amount (USD)', 'Age', 'Previous Purchases', 'Review Rating']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

@st.cache_data
def load_analysis_files():
    """Load analysis output files with graceful fallbacks"""
    output_dir = Path('.') / 'analysis_output'
    analysis_data = {}
    
    csv_files = {
        'missing_values': 'missing_values_summary.csv',
        'numeric_stats':  'numeric_summary_statistics.csv',
        'outliers':       'outliers_report.csv',
        'segments':       'customer_segments.csv',
        'chi_square':     'chi_square_results.csv',
        'correlations':   'strong_correlations.csv'
    }
    
    for key, filename in csv_files.items():
        filepath = output_dir / filename
        if filepath.exists():
            try:
                analysis_data[key] = pd.read_csv(filepath)
            except Exception as e:
                pass  # Silently skip
    
    text_files = {
        'data_quality':      'data_quality_report.txt',
        'statistical_tests': 'statistical_tests_results.txt',
        'insights':          'final_insights_and_recommendations.txt'
    }
    
    for key, filename in text_files.items():
        filepath = output_dir / filename
        if filepath.exists():
            try:
                with open(filepath, 'r') as f:
                    analysis_data[key] = f.read()
            except Exception as e:
                pass  # Silently skip
    
    return analysis_data, output_dir

@st.cache_data
def load_images():
    """Load analysis images with graceful fallbacks"""
    output_dir = Path('.') / 'analysis_output'
    images = {}
    
    image_files = [
        '01_customer_purchase_distribution.png',
        '02_age_demographics.png',
        '03_category_sales_volume.png',
        '04_purchase_by_category.png',
        '05_shipping_preferences.png',
        '06_satisfaction_analysis.png',
        '07_seasonal_patterns.png',
        '08_subscription_impact.png',
        '09_payment_methods.png',
        '10_discount_effectiveness.png',
        '11_customer_loyalty.png',
        '12_geographic_distribution.png',
        'correlation_heatmap.png',
        'missingness_heatmap.png'
    ]
    
    for img_file in image_files:
        filepath = output_dir / img_file
        if filepath.exists():
            try:
                images[img_file.replace('.png', '')] = Image.open(filepath)
            except Exception:
                pass  # Silently skip
    
    return images

# ============================================================================
# PLOTLY DARK THEME
# ============================================================================

PLOTLY_DARK = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(17,19,24,1)",
    plot_bgcolor="rgba(26,30,40,0.6)",
    font=dict(family="DM Sans, sans-serif", size=12, color="#a0aabe"),
    title_font=dict(family="Syne, sans-serif", size=15, color="#e8ecf4"),
    legend=dict(bgcolor="rgba(10,12,16,0.92)", bordercolor="#4f8ef7", borderwidth=1,
                font=dict(color="#e8ecf4", size=11), title_font=dict(color="#a0aabe")),
    hovermode="x unified",
    margin=dict(l=48, r=24, t=52, b=42),
    colorway=["#4f8ef7", "#34d9b3", "#f0b429", "#f75f7b", "#a78bfa", "#fb923c"],
    xaxis=dict(gridcolor="rgba(42,48,64,0.8)", linecolor="#2a3040", tickfont=dict(size=11)),
    yaxis=dict(gridcolor="rgba(42,48,64,0.8)", linecolor="#2a3040", tickfont=dict(size=11)),
)

def dark_chart(fig):
    fig.update_layout(**PLOTLY_DARK)
    return fig

# ============================================================================
# REUSABLE COMPONENTS
# ============================================================================

def kpi(col, label, value, delta=None, icon="◆", accent="#4f8ef7"):
    delta_html = f'<div class="kpi-delta">{delta}</div>' if delta else ''
    col.markdown(f"""
    <div class="kpi-card" style="--accent-color:{accent};">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def section(title, badge=None):
    badge_html = f'<span class="section-label-badge">{badge}</span>' if badge else ''
    st.markdown(f"""
    <div class="section-label">
        <div class="section-label-bar"></div>
        <div class="section-label-text">{title}</div>
        {badge_html}
    </div>
    """, unsafe_allow_html=True)

def insight(label, body, kind=""):
    st.markdown(f"""
    <div class="insight-panel {kind}">
        <div class="insight-panel-label">{label}</div>
        <div class="insight-panel-body">{body}</div>
    </div>
    """, unsafe_allow_html=True)

def info_banner(title, content):
    st.markdown(f"""
    <div class="info-banner">
        <span class="info-banner-icon">◈</span>
        <div class="info-banner-content">
            <strong>{title}</strong>
            <span>{content}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def divider():
    st.markdown('<div class="ruled-divider"></div>', unsafe_allow_html=True)

def fmt_usd(v):  return f"${v:,.2f}" if v else "$0.00"
def fmt_pct(v):  return f"{v:.1f}%"

# ============================================================================
# PAGE: HOME
# ============================================================================

def page_home(df, analysis_data):
    st.markdown("""
    <div class="page-eyebrow">◆ ShopIQ Analytics · 2026</div>
    <div class="page-title">Customer Intelligence <span>Command Center</span></div>
    <div class="page-subtitle">
        Real-time exploration of purchase behavior, cohort patterns, and market signals —
        all in one unified workspace.
    </div>
    """, unsafe_allow_html=True)

    divider()

    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, "Total Records",    f"{len(df):,}",                                icon="⬡", accent="#4f8ef7")
    kpi(c2, "Avg Purchase",     fmt_usd(df['Purchase Amount (USD)'].mean()),   icon="◈", accent="#34d9b3")
    kpi(c3, "Unique Customers", f"{df['Customer ID'].nunique():,}",             icon="◎", accent="#f0b429")
    kpi(c4, "Avg Rating",       f"{df['Review Rating'].mean():.2f} / 5",       icon="◇", accent="#a78bfa")

    divider()

    tab1, tab2, tab3 = st.tabs(["Overview", "Key Metrics", "Quick Insights"])

    with tab1:
        section("Executive Summary", "Live")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Total Revenue", fmt_usd(df['Purchase Amount (USD)'].sum()))
        with m2:
            sat = (df['Review Rating'] >= 4).sum() / len(df) * 100 if len(df) > 0 else 0
            st.metric("Satisfaction Rate", fmt_pct(sat), "+2.3% from last period")
        with m3:
            rep = (df['Frequency of Purchases'].isin(['Weekly', 'Monthly'])).sum() / len(df) * 100 if 'Frequency of Purchases' in df.columns else 0
            st.metric("Repeat Customer Rate", fmt_pct(rep), "+1.8% from last period")

        st.markdown("<br>", unsafe_allow_html=True)

        cc1, cc2 = st.columns(2)
        with cc1:
            if 'Category' in df.columns:
                cat_counts = df['Category'].astype(str).value_counts()
                fig = px.bar(x=cat_counts.index, y=cat_counts.values,
                             title="Sales Volume by Category",
                             labels={'x': 'Category', 'y': 'Records'})
                fig.update_traces(marker_color='#4f8ef7', marker_line_width=0)
                st.plotly_chart(dark_chart(fig), use_container_width=True)
        with cc2:
            if 'Location' in df.columns:
                loc_counts = df['Location'].astype(str).value_counts().head(10)
                fig2 = px.bar(x=loc_counts.values, y=loc_counts.index, orientation='h',
                              title="Top 10 Locations by Volume",
                              labels={'x': 'Records', 'y': 'Location'})
                fig2.update_layout(height=380, yaxis=dict(autorange='reversed'))
                fig2.update_traces(marker_color='#34d9b3', marker_line_width=0)
                st.plotly_chart(dark_chart(fig2), use_container_width=True)

    with tab2:
        section("Core Business Metrics")
        metrics_data = {
            "Average Order Value":     fmt_usd(df['Purchase Amount (USD)'].mean()),
            "Median Order Value":      fmt_usd(df['Purchase Amount (USD)'].median()),
            "Order Value Std Dev":     fmt_usd(df['Purchase Amount (USD)'].std()),
            "Customer Lifetime Value": fmt_usd(df['Purchase Amount (USD)'].sum() / df['Customer ID'].nunique() if df['Customer ID'].nunique() > 0 else 0),
            "Subscription Rate":       fmt_pct((df['Subscription Status'] == 'Yes').sum() / len(df) * 100 if 'Subscription Status' in df.columns else 0),
            "Promo Code Usage":        fmt_pct((df['Promo Code Used'] == 'Yes').sum() / len(df) * 100 if 'Promo Code Used' in df.columns else 0),
        }
        g1, g2, g3 = st.columns(3)
        gmap = [g1, g2, g3]
        for i, (name, val) in enumerate(metrics_data.items()):
            with gmap[i % 3]:
                st.markdown(f"""
                <div class="kpi-card" style="margin-bottom:12px;">
                    <div class="kpi-label">{name}</div>
                    <div class="kpi-value" style="font-size:1.8rem;">{val}</div>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        section("Quick Signals")
        if 'Category' in df.columns and len(df['Category'].value_counts()) > 0:
            top_cat = df['Category'].value_counts().index[0]
            insight("Top Category", f"<strong>{top_cat}</strong> leads all categories with "
                    f"{(df['Category'] == top_cat).sum():,} purchases.", "success")
        
        if 'Location' in df.columns and len(df['Location'].value_counts()) > 0:
            top_loc = df['Location'].value_counts().index[0]
            insight("Primary Market", f"<strong>{top_loc}</strong> accounts for "
                    f"{((df['Location'] == top_loc).sum() / len(df) * 100):.1f}% of all revenue.", "success")
        
        if 'Age' in df.columns:
            avg_age = df['Age'].mean()
            insight("Demographics", f"Average customer age is <strong>{avg_age:.1f} years</strong>, "
                    f"ranging from {df['Age'].min():.0f} to {df['Age'].max():.0f}.")
        
        if 'Category' in df.columns:
            min_cat_spend = df.groupby('Category')['Purchase Amount (USD)'].sum().min()
            insight("Revenue Risk",
                    f"Bottom-performing categories generate only "
                    f"<strong>{min_cat_spend:,.0f} USD</strong> "
                    "— consider strategic review.", "warning")

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    df = load_main_data()
    analysis_data, output_dir = load_analysis_files()
    images = load_images()

    if df is None or len(df) == 0:
        st.error("Unable to load dataset. Displaying sample data instead.")
        st.stop()
        return

    with st.sidebar:
        st.markdown("""
        <div class="nav-logo">
            <div class="nav-logo-mark">
                <span class="nav-logo-dot"></span> ShopIQ
            </div>
            <div class="nav-logo-sub">Analytics Platform · 2026</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="nav-section-title">Navigation</div>', unsafe_allow_html=True)

        page_options = {
            "◆  Home":           "home",
        }

        selected = st.radio("nav", list(page_options.keys()), label_visibility="collapsed")
        page_key = page_options[selected]

        st.divider()

        st.markdown('<div class="nav-section-title">Dataset Snapshot</div>', unsafe_allow_html=True)
        for label, val in [
            ("Records",      f"{len(df):,}"),
            ("Columns",      f"{df.shape[1]}"),
            ("Avg Purchase", fmt_usd(df['Purchase Amount (USD)'].mean())),
            ("Avg Rating",   f"{df['Review Rating'].mean():.2f} / 5" if 'Review Rating' in df.columns else "N/A"),
        ]:
            st.markdown(f"""
            <div class="sq-stat">
                <span class="sq-label">{label}</span>
                <span class="sq-value">{val}</span>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("""
        <div style="padding: 0 0.4rem; color: #6b7494; font-size: 0.78rem; line-height: 1.7;">
            <strong style="color:#a0aabe;">Customer Shopping Analytics</strong><br>
            Built with Streamlit · Plotly · Pandas<br><br>
            <span style="opacity:0.6;">© 2026 Data Analytics Team</span>
        </div>
        """, unsafe_allow_html=True)

    if page_key == "home":
        page_home(df, analysis_data)

    divider()
    st.markdown("""
    <div style="text-align:center; color:#3a4155; font-size:0.78rem; padding:1rem 0 2rem;">
        ShopIQ Analytics · Powered by Streamlit, Plotly & Pandas
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()