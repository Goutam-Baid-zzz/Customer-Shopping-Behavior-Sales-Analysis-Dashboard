"""
================================================================================
  CUSTOMER SHOPPING DATA ANALYTICS DASHBOARD - OBSIDIAN EDITION
  Ultra-Premium Streamlit Application for EDA & Business Insights
================================================================================

Author: Data Analytics Team
Purpose: Interactive, production-ready dashboard for customer shopping analysis
Date: 2026

================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import warnings
import unicodedata

warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
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
# DATA LOADING & CACHING
# ============================================================================

@st.cache_data
def load_main_data():
    """Load main dataset. Returns (df, error_message) tuple."""
    data_path = Path(__file__).parent / 'Customer_shopping_data_.csv'
    if not data_path.exists():
        return None, f"Dataset not found at {data_path}"
    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        return None, f"Failed to read CSV: {e}"

    if 'Customer ID' in df.columns:
        df['Customer ID'] = df['Customer ID'].astype(str)

    for col in ['Gender', 'Category', 'Location', 'Size', 'Color', 'Season',
                'Subscription Status', 'Shipping Type', 'Discount Applied',
                'Promo Code Used', 'Payment Method', 'Frequency of Purchases']:
        if col in df.columns:
            df[col] = df[col].astype('category')

    if 'Category' in df.columns:
        df['Category'] = df['Category'].astype(str).str.strip()
        df['Category'] = df['Category'].str.replace(r"\s+", ' ', regex=True)
        df['Category'] = df['Category'].apply(lambda x: unicodedata.normalize('NFKC', x))
        df['Category'] = df['Category'].str.title()
        df['Category'] = df['Category'].astype('category')

    for col in ['Purchase Amount (USD)', 'Age', 'Previous Purchases', 'Review Rating']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df, None


@st.cache_data
def load_analysis_files():
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
            except Exception:
                pass

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
            except Exception:
                pass

    return analysis_data, output_dir


@st.cache_data
def load_images():
    """Load pre-generated analysis images. Returns dict of image paths (not PIL objects)."""
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
            # Store path strings instead of PIL objects to avoid file handle leaks
            images[img_file.replace('.png', '')] = str(filepath)
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

def fmt_usd(v):  return f"${v:,.2f}"
def fmt_pct(v):  return f"{v:.1f}%"

def show_image(images, key):
    """Safely display an image from the images dict (paths)."""
    if key in images:
        st.image(images[key], width="stretch")


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
            sat = (df['Review Rating'] >= 4).sum() / len(df) * 100
            st.metric("Satisfaction Rate", fmt_pct(sat), "+2.3% from last period")
        with m3:
            rep = (df['Frequency of Purchases'].isin(['Weekly', 'Monthly'])).sum() / len(df) * 100
            st.metric("Repeat Customer Rate", fmt_pct(rep), "+1.8% from last period")

        st.markdown("<br>", unsafe_allow_html=True)

        cc1, cc2 = st.columns(2)
        with cc1:
            cat_counts = df['Category'].astype(str).value_counts()
            fig = px.bar(x=cat_counts.index, y=cat_counts.values,
                         title="Sales Volume by Category",
                         labels={'x': 'Category', 'y': 'Records'})
            fig.update_traces(marker_color='#4f8ef7', marker_line_width=0)
            st.plotly_chart(dark_chart(fig), width="stretch")
        with cc2:
            loc_counts = df['Location'].astype(str).value_counts().head(10)
            fig2 = px.bar(x=loc_counts.values, y=loc_counts.index, orientation='h',
                          title="Top 10 Locations by Volume",
                          labels={'x': 'Records', 'y': 'Location'})
            fig2.update_layout(height=380, yaxis=dict(autorange='reversed'))
            fig2.update_traces(marker_color='#34d9b3', marker_line_width=0)
            st.plotly_chart(dark_chart(fig2), width="stretch")

    with tab2:
        section("Core Business Metrics")
        metrics_data = {
            "Average Order Value":     fmt_usd(df['Purchase Amount (USD)'].mean()),
            "Median Order Value":      fmt_usd(df['Purchase Amount (USD)'].median()),
            "Order Value Std Dev":     fmt_usd(df['Purchase Amount (USD)'].std()),
            "Customer Lifetime Value": fmt_usd(df['Purchase Amount (USD)'].sum() / max(df['Customer ID'].nunique(), 1)),
            "Subscription Rate":       fmt_pct((df['Subscription Status'] == 'Yes').sum() / len(df) * 100),
            "Promo Code Usage":        fmt_pct((df['Promo Code Used'] == 'Yes').sum() / len(df) * 100),
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
        top_cat = df['Category'].value_counts().index[0]
        top_loc = df['Location'].value_counts().index[0]
        avg_age = df['Age'].mean()

        insight("Top Category", f"<strong>{top_cat}</strong> leads all categories with "
                f"{(df['Category'].astype(str) == str(top_cat)).sum():,} purchases.", "success")
        insight("Primary Market", f"<strong>{top_loc}</strong> accounts for "
                f"{((df['Location'].astype(str) == str(top_loc)).sum() / len(df) * 100):.1f}% of all revenue.", "success")
        insight("Demographics", f"Average customer age is <strong>{avg_age:.1f} years</strong>, "
                f"ranging from {df['Age'].min():.0f} to {df['Age'].max():.0f}.")
        insight("Revenue Risk",
                f"Bottom-performing categories generate only "
                f"<strong>{df.groupby(df['Category'].astype(str))['Purchase Amount (USD)'].sum().min():,.0f} USD</strong> "
                "— consider strategic review.", "warning")


# ============================================================================
# PAGE: DATASET PREVIEW
# ============================================================================

def page_dataset_preview(df):
    st.markdown('<div class="page-eyebrow">◆ Data Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Dataset <span>Explorer</span></div>', unsafe_allow_html=True)

    info_banner("About This Dataset",
                "Browse, filter, and inspect every record in the customer shopping dataset. "
                "Use the Filtered View tab to narrow down by segment.")

    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, "Total Rows",    f"{len(df):,}",                                       icon="⬡", accent="#4f8ef7")
    kpi(c2, "Total Columns", f"{df.shape[1]}",                                     icon="◈", accent="#34d9b3")
    kpi(c3, "Memory",        f"{df.memory_usage(deep=True).sum()/1024**2:.2f} MB", icon="◎", accent="#f0b429")
    kpi(c4, "Data Types",    f"{df.dtypes.nunique()}",                              icon="◇", accent="#a78bfa")

    divider()

    tab1, tab2, tab3, tab4 = st.tabs(["Full Dataset", "Filtered View", "Column Info", "Sample Stats"])

    with tab1:
        section("Complete Dataset")
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:0.8rem;">
            <span style="font-size:0.78rem;color:var(--ghost);letter-spacing:0.08em;text-transform:uppercase;">
                {len(df):,} rows &times; {df.shape[1]} columns
            </span>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(df, width="stretch", height=500)

    with tab2:
        section("Interactive Filter")
        f1, f2, f3 = st.columns([2, 1, 1])
        with f1:
            cat_options = sorted(df['Category'].astype(str).unique().tolist())
            sel_cat = st.multiselect("Category", options=cat_options,
                                     default=cat_options[:3],
                                     label_visibility="visible")
        with f2:
            gen_options = sorted(df['Gender'].astype(str).unique().tolist())
            sel_gen = st.multiselect("Gender", options=gen_options,
                                     default=gen_options,
                                     label_visibility="visible")
        with f3:
            min_rat = st.slider("Min Rating ★", 1.0, 5.0, 1.0, step=0.5)

        fdf = df[
            df['Category'].astype(str).isin(sel_cat) &
            df['Gender'].astype(str).isin(sel_gen) &
            (df['Review Rating'] >= min_rat)
        ]

        rc1, rc2, rc3 = st.columns(3)
        avg_filt = fdf['Purchase Amount (USD)'].mean() if len(fdf) else 0
        with rc1:
            st.markdown(f"""<div class="kpi-card" style="--accent-color:#4f8ef7;min-height:90px;">
                <div class="kpi-label">Filtered Records</div>
                <div class="kpi-value" style="font-size:1.4rem;">{len(fdf):,}</div>
            </div>""", unsafe_allow_html=True)
        with rc2:
            st.markdown(f"""<div class="kpi-card" style="--accent-color:#34d9b3;min-height:90px;">
                <div class="kpi-label">% of Total</div>
                <div class="kpi-value" style="font-size:1.4rem;">{len(fdf)/len(df)*100:.1f}%</div>
            </div>""", unsafe_allow_html=True)
        with rc3:
            st.markdown(f"""<div class="kpi-card" style="--accent-color:#f0b429;min-height:90px;">
                <div class="kpi-label">Avg Purchase</div>
                <div class="kpi-value" style="font-size:1.4rem;">{fmt_usd(avg_filt)}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.dataframe(fdf, width="stretch", height=380)

    with tab3:
        section("Column Schema")
        col_info = pd.DataFrame({
            'Column':   df.columns,
            'Type':     df.dtypes.astype(str),
            'Non-Null': df.count().values,
            'Null':     df.isnull().sum().values,
            'Null %':   (df.isnull().sum()/len(df)*100).round(2).values,
            'Unique':   df.nunique().values
        })
        st.dataframe(col_info, width="stretch")

    with tab4:
        section("Statistical Summary")
        st.dataframe(df.describe().round(3), width="stretch")


# ============================================================================
# PAGE: DATA QUALITY
# ============================================================================

def page_data_quality(df, analysis_data, images):
    st.markdown('<div class="page-eyebrow">◆ Quality Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Data <span>Quality</span></div>', unsafe_allow_html=True)

    info_banner("Quality Assessment",
                "Completeness, outlier detection, and integrity scoring across all features.")

    completeness = (1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, "Completeness",   f"{completeness:.1f}%",              icon="✓", accent="#34d9b3")
    kpi(c2, "Missing Values", f"{df.isnull().sum().sum():,}",      icon="⚠", accent="#f0b429")
    kpi(c3, "Duplicates",     f"{df.duplicated().sum():,}",        icon="⬡", accent="#f75f7b")
    kpi(c4, "Quality Score",  f"{min(completeness*.95,100):.1f}",  icon="◈", accent="#4f8ef7")

    divider()

    tab1, tab2, tab3 = st.tabs(["Completeness & Missing", "Outlier Detection", "Quality Report"])

    with tab1:
        section("Data Completeness by Column")
        comp_col = (1 - df.isnull().sum() / len(df)) * 100
        comp_col = comp_col.sort_values()
        fig = px.bar(x=comp_col.values, y=comp_col.index, orientation='h',
                     title="Data Completeness (%)",
                     labels={'x': 'Completeness (%)', 'y': ''},
                     color=comp_col.values,
                     color_continuous_scale=[[0, "#f75f7b"], [0.5, "#f0b429"], [1, "#34d9b3"]])
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(dark_chart(fig), width="stretch")

        divider()
        section("Missing Values Breakdown")
        miss_count = df.isnull().sum()
        miss_pct   = (miss_count / len(df) * 100).round(2)
        miss_df    = pd.DataFrame({
            'Column':        miss_count.index,
            'Missing Count': miss_count.values,
            'Missing %':     miss_pct.values
        }).query('`Missing Count` > 0').sort_values('Missing Count', ascending=False).reset_index(drop=True)

        if len(miss_df) == 0:
            insight("No Missing Values", "The dataset is fully complete — no null values detected.", "success")
        else:
            c1, c2 = st.columns([3, 2])
            with c1:
                fig2 = px.bar(miss_df, x='Column', y='Missing %',
                              title='Missing Value Rate by Column',
                              labels={'Missing %': '% Missing'},
                              color='Missing %',
                              color_continuous_scale=[[0, "#f0b429"], [1, "#f75f7b"]])
                fig2.update_layout(coloraxis_showscale=False)
                st.plotly_chart(dark_chart(fig2), width="stretch")
            with c2:
                st.dataframe(miss_df, width="stretch", hide_index=True)
                st.markdown("<br>", unsafe_allow_html=True)
                insight("Highest Missing",
                        f"<strong>{miss_df.iloc[0]['Column']}</strong> has the most missing data at "
                        f"<strong>{miss_df.iloc[0]['Missing %']:.1f}%</strong>.", "warning")

        if 'missingness_heatmap' in images:
            section("Missingness Heatmap")
            show_image(images, 'missingness_heatmap')

    with tab2:
        section("Outlier Detection — Numeric Features")
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        c1, c2 = st.columns(2)
        with c1:
            fig_box = px.box(df, y=numeric_cols,
                             title="Distribution & Outliers (Box Plots)",
                             labels={'value': 'Value', 'variable': 'Feature'})
            st.plotly_chart(dark_chart(fig_box), width="stretch")
        with c2:
            outlier_rows = []
            for col in numeric_cols:
                Q1  = df[col].quantile(0.25)
                Q3  = df[col].quantile(0.75)
                IQR = Q3 - Q1
                n_out = ((df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)).sum()
                outlier_rows.append({'Feature': col, 'Outlier Count': int(n_out),
                                     'Outlier %': round(n_out/len(df)*100, 2),
                                     'Q1': round(Q1,2), 'Q3': round(Q3,2), 'IQR': round(IQR,2)})
            out_df = pd.DataFrame(outlier_rows).sort_values('Outlier Count', ascending=False)
            st.dataframe(out_df, width="stretch", hide_index=True)
            total_out = out_df['Outlier Count'].sum()
            insight("Outlier Summary",
                    f"Detected <strong>{total_out:,}</strong> outlier records across all numeric features "
                    f"using IQR × 1.5 method.", "warning")

        if 'outliers' in analysis_data:
            section("Pre-computed Outliers Report")
            out_display = analysis_data['outliers'].copy()
            if 'iqr_bounds' in out_display.columns:
                import re
                def clean_bounds(val):
                    nums = re.findall(r'np\.float64\(([-+]?\d*\.?\d+)\)', str(val))
                    if len(nums) >= 2:
                        return f"({float(nums[0]):.2f}, {float(nums[1]):.2f})"
                    nums = re.findall(r'[-+]?\d*\.?\d+', str(val))
                    if len(nums) >= 2:
                        return f"({float(nums[0]):.2f}, {float(nums[1]):.2f})"
                    return str(val)
                out_display['iqr_bounds'] = out_display['iqr_bounds'].apply(clean_bounds)
            st.dataframe(out_display, width="stretch")

    with tab3:
        section("Data Quality Report")
        if 'data_quality' in analysis_data and analysis_data['data_quality'].strip():
            st.code(analysis_data['data_quality'], language='text')
        else:
            total_cells  = len(df) * len(df.columns)
            missing_tot  = df.isnull().sum().sum()
            dup_count    = df.duplicated().sum()
            comp_pct     = (1 - missing_tot/total_cells)*100

            report = f"""DATA QUALITY REPORT — ShopIQ Analytics
{'='*60}

DATASET DIMENSIONS
  Rows    : {len(df):,}
  Columns : {len(df.columns)}
  Cells   : {total_cells:,}

COMPLETENESS
  Complete cells  : {total_cells - missing_tot:,} / {total_cells:,}
  Completeness    : {comp_pct:.2f}%
  Missing total   : {missing_tot:,}

COLUMNS WITH MISSING VALUES
{'Column':<35} {'Missing':>10} {'%':>8}
{'-'*55}"""
            for col in df.columns:
                mc = df[col].isnull().sum()
                if mc > 0:
                    report += f"\n  {col:<33} {mc:>10,} {mc/len(df)*100:>7.2f}%"

            report += f"""

DUPLICATES
  Duplicate rows  : {dup_count:,}

DATA TYPES
"""
            for col, dtype in df.dtypes.items():
                report += f"  {col:<35} {str(dtype)}\n"

            report += f"\nNUMERIC SUMMARY\n"
            report += df.describe().to_string()
            st.code(report, language='text')


# ============================================================================
# PAGE: UNIVARIATE ANALYSIS
# ============================================================================

def page_univariate_analysis(df, images):
    st.markdown('<div class="page-eyebrow">◆ Univariate Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Single Variable <span>Distributions</span></div>', unsafe_allow_html=True)

    info_banner("Univariate Analysis",
                "Explore the shape, spread, and character of each individual feature.")

    tab1, tab2, tab3, tab4 = st.tabs(["Purchase Distribution", "Demographics", "Product Mix", "Satisfaction"])

    with tab1:
        section("Purchase Amount Distribution")
        c1, c2 = st.columns([3, 2])
        with c1:
            if '01_customer_purchase_distribution' in images:
                show_image(images, '01_customer_purchase_distribution')
            else:
                fig = px.histogram(df, x='Purchase Amount (USD)', nbins=50,
                                   title='Purchase Amount Distribution',
                                   labels={'count': 'Frequency'})
                fig.update_traces(marker_color='#4f8ef7', marker_line_width=0.8, marker_line_color='rgba(255,255,255,0.22)')
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            stats = {
                'Mean':   fmt_usd(df['Purchase Amount (USD)'].mean()),
                'Median': fmt_usd(df['Purchase Amount (USD)'].median()),
                'Std':    fmt_usd(df['Purchase Amount (USD)'].std()),
                'Min':    fmt_usd(df['Purchase Amount (USD)'].min()),
                'Max':    fmt_usd(df['Purchase Amount (USD)'].max()),
                'Q1':     fmt_usd(df['Purchase Amount (USD)'].quantile(0.25)),
                'Q3':     fmt_usd(df['Purchase Amount (USD)'].quantile(0.75)),
            }
            for name, val in stats.items():
                st.markdown(f"""
                <div class="sq-stat">
                    <span class="sq-label">{name}</span>
                    <span class="sq-value">{val}</span>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        section("Demographic Distributions")
        c1, c2 = st.columns(2)
        with c1:
            if '02_age_demographics' in images:
                show_image(images, '02_age_demographics')
            else:
                fig = px.histogram(df, x='Age', nbins=30, title='Age Distribution',
                                   labels={'count': 'Frequency'})
                fig.update_traces(marker_color='#34d9b3', marker_line_width=0.8, marker_line_color='rgba(255,255,255,0.22)')
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            fig2 = px.pie(df, names='Gender', title='Gender Distribution',
                          color_discrete_sequence=['#4f8ef7', '#34d9b3', '#f0b429'])
            fig2.update_traces(textfont_size=13)
            st.plotly_chart(dark_chart(fig2), width="stretch")

    with tab3:
        section("Product Mix")
        c1, c2 = st.columns(2)
        with c1:
            if '03_category_sales_volume' in images:
                show_image(images, '03_category_sales_volume')
            else:
                cat_d = df['Category'].astype(str).value_counts()
                fig = px.bar(x=cat_d.index, y=cat_d.values, title='Sales by Category',
                             labels={'x': 'Category', 'y': 'Count'})
                fig.update_traces(marker_color='#4f8ef7', marker_line_width=0)
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            if '05_shipping_preferences' in images:
                show_image(images, '05_shipping_preferences')
            else:
                ship_d = df['Shipping Type'].astype(str).value_counts()
                fig2 = px.pie(values=ship_d.values, names=ship_d.index,
                              title='Shipping Type Split',
                              color_discrete_sequence=['#4f8ef7', '#34d9b3', '#f0b429', '#f75f7b', '#a78bfa'])
                st.plotly_chart(dark_chart(fig2), width="stretch")

    with tab4:
        section("Satisfaction & Ratings")
        c1, c2 = st.columns([3, 2])
        with c1:
            if '06_satisfaction_analysis' in images:
                show_image(images, '06_satisfaction_analysis')
            else:
                fig = px.histogram(df, x='Review Rating', nbins=5,
                                   title='Review Rating Distribution',
                                   labels={'count': 'Count'})
                fig.update_traces(marker_color='#a78bfa', marker_line_width=0.8, marker_line_color='rgba(255,255,255,0.22)')
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            avg_r = df['Review Rating'].mean()
            high  = (df['Review Rating'] >= 4).sum() / len(df) * 100
            low   = (df['Review Rating'] <= 3).sum() / len(df) * 100
            insight("Average Rating",  f"<strong>{avg_r:.2f} / 5.0</strong> across all customers.", "success")
            insight("Promoters",       f"<strong>{high:.1f}%</strong> rated 4+ stars.", "success")
            insight("Detractors",      f"<strong>{low:.1f}%</strong> rated 3 stars or below.", "warning")


# ============================================================================
# PAGE: MULTIVARIATE ANALYSIS
# ============================================================================

def page_multivariate_analysis(df, images, analysis_data):
    st.markdown('<div class="page-eyebrow">◆ Multivariate Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Feature <span>Relationships</span></div>', unsafe_allow_html=True)

    info_banner("Multivariate Analysis",
                "Correlations, cross-tabulations, and interaction effects across all dimensions.")

    tab1, tab2, tab3, tab4 = st.tabs(["Correlations", "Purchase Patterns", "Chi-Square", "Advanced Patterns"])

    with tab1:
        section("Correlation Matrix")
        c1, c2 = st.columns([3, 1])
        with c1:
            if 'correlation_heatmap' in images:
                show_image(images, 'correlation_heatmap')
            else:
                num_cols = df.select_dtypes(include=[np.number]).columns
                corr = df[num_cols].corr()
                fig = go.Figure(data=go.Heatmap(
                    z=corr.values, x=corr.columns, y=corr.columns,
                    colorscale=[[0, '#f75f7b'], [0.5, '#1a1e28'], [1, '#34d9b3']],
                    zmid=0, text=corr.round(2).values,
                    texttemplate="%{text}", textfont={"size": 10}
                ))
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            section("Numeric Correlations")
            num_cols = df.select_dtypes(include=[np.number]).columns
            corr     = df[num_cols].corr()
            pairs    = []
            cols_l   = list(corr.columns)
            for i in range(len(cols_l)):
                for j in range(i+1, len(cols_l)):
                    pairs.append({'Feature A': cols_l[i], 'Feature B': cols_l[j],
                                  'r': round(corr.iloc[i,j], 3)})
            corr_pairs = pd.DataFrame(pairs).sort_values('r', key=abs, ascending=False)
            st.dataframe(corr_pairs, width="stretch", hide_index=True)

    with tab2:
        section("Purchase Amount Analysis")
        c1, c2 = st.columns(2)
        with c1:
            if '04_purchase_by_category' in images:
                show_image(images, '04_purchase_by_category')
            else:
                df_box = df.copy()
                df_box['Category'] = df_box['Category'].astype(str)
                fig = px.box(df_box, x='Category', y='Purchase Amount (USD)',
                             title='Purchase Distribution by Category',
                             color='Category',
                             color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#f75f7b','#a78bfa'])
                fig.update_layout(showlegend=False)
                st.plotly_chart(dark_chart(fig), width="stretch")
        with c2:
            df_age = df.dropna(subset=['Age']).copy()
            age_spend = df_age.groupby(
                pd.cut(df_age['Age'], bins=10)
            )['Purchase Amount (USD)'].mean().reset_index()
            age_spend.columns = ['Age Group', 'Avg Purchase']
            age_spend['Age Group'] = age_spend['Age Group'].astype(str)
            fig2 = px.bar(age_spend, x='Age Group', y='Avg Purchase',
                          title='Avg Purchase Amount by Age Group',
                          labels={'Age Group': 'Age Range', 'Avg Purchase': 'Avg ($)'},
                          color='Avg Purchase',
                          color_continuous_scale=[[0,'#1a1e28'],[1,'#4f8ef7']])
            fig2.update_layout(coloraxis_showscale=False, hovermode='x', xaxis_tickangle=-35)
            st.plotly_chart(dark_chart(fig2), width="stretch")

        divider()
        section("Gender × Category Spending")
        gender_cat = df.groupby([df['Category'].astype(str), df['Gender'].astype(str)])['Purchase Amount (USD)'].mean().reset_index()
        gender_cat.columns = ['Category', 'Gender', 'Purchase Amount (USD)']
        fig3 = px.bar(gender_cat, x='Category', y='Purchase Amount (USD)', color='Gender',
                      barmode='group', title='Avg Purchase by Category & Gender',
                      color_discrete_sequence=['#4f8ef7', '#f75f7b'])
        fig3.update_layout(hovermode='x')
        st.plotly_chart(dark_chart(fig3), width="stretch")

    with tab3:
        section("Chi-Square Test Results")
        if 'chi_square' in analysis_data and not analysis_data['chi_square'].empty:
            st.dataframe(analysis_data['chi_square'], width="stretch")
            insight("Statistical Significance",
                    "Chi-square tests examine categorical variable relationships. "
                    "P-values &lt; 0.05 indicate statistically significant associations.", "violet")
        else:
            try:
                from scipy.stats import chi2_contingency
                cat_cols = df.select_dtypes(include='category').columns.tolist()
                chi_rows = []
                tested = set()
                for i, col_a in enumerate(cat_cols):
                    for col_b in cat_cols[i+1:]:
                        pair = tuple(sorted([col_a, col_b]))
                        if pair in tested:
                            continue
                        tested.add(pair)
                        try:
                            ct = pd.crosstab(df[col_a], df[col_b])
                            chi2, p, dof, _ = chi2_contingency(ct)
                            chi_rows.append({
                                'Variable A': col_a, 'Variable B': col_b,
                                'Chi²': round(chi2, 3), 'p-value': round(p, 6),
                                'DoF': dof, 'Significant': '✓ Yes' if p < 0.05 else '✗ No'
                            })
                        except Exception:
                            pass
                chi_df = pd.DataFrame(chi_rows).sort_values('Chi²', ascending=False).reset_index(drop=True)
                st.dataframe(chi_df, width="stretch", hide_index=True)
                sig_count = (chi_df['Significant'] == '✓ Yes').sum()
                insight("Chi-Square Summary",
                        f"<strong>{sig_count}</strong> out of <strong>{len(chi_df)}</strong> variable pairs "
                        f"show statistically significant associations (p &lt; 0.05).", "violet")
            except ImportError:
                insight("SciPy Not Available", "Install scipy to compute chi-square tests.", "warning")

        section("Category × Season Sales Heatmap")
        ct = pd.crosstab(df['Category'].astype(str), df['Season'].astype(str))
        fig_ht = go.Figure(data=go.Heatmap(
            z=ct.values, x=ct.columns.tolist(), y=ct.index.tolist(),
            colorscale=[[0,'#1a1e28'],[0.5,'#4f8ef7'],[1,'#34d9b3']],
            text=ct.values, texttemplate="%{text}", textfont={"size":12}
        ))
        fig_ht.update_layout(title='Purchase Count: Category × Season')
        st.plotly_chart(dark_chart(fig_ht), width="stretch")

    with tab4:
        section("Advanced Pattern Library")
        has_images = any(k in images for k in ['07_seasonal_patterns','08_subscription_impact',
                                                 '09_payment_methods','10_discount_effectiveness'])
        if has_images:
            r1c1, r1c2 = st.columns(2)
            with r1c1:
                if '07_seasonal_patterns' in images:
                    st.caption("Seasonal Patterns")
                    show_image(images, '07_seasonal_patterns')
            with r1c2:
                if '09_payment_methods' in images:
                    st.caption("Payment Methods")
                    show_image(images, '09_payment_methods')
            r2c1, r2c2 = st.columns(2)
            with r2c1:
                if '08_subscription_impact' in images:
                    st.caption("Subscription Impact")
                    show_image(images, '08_subscription_impact')
            with r2c2:
                if '10_discount_effectiveness' in images:
                    st.caption("Discount Effectiveness")
                    show_image(images, '10_discount_effectiveness')
        else:
            r1c1, r1c2 = st.columns(2)
            with r1c1:
                if 'Season' in df.columns:
                    seas = df.groupby(df['Season'].astype(str))['Purchase Amount (USD)'].agg(['mean','count']).reset_index()
                    seas.columns = ['Season','Avg Purchase','Count']
                    fig_s = px.bar(seas, x='Season', y='Avg Purchase', title='Avg Purchase by Season',
                                   color='Season', color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#a78bfa'])
                    fig_s.update_traces(marker_line_width=0)
                    st.plotly_chart(dark_chart(fig_s), width="stretch")
            with r1c2:
                if 'Payment Method' in df.columns:
                    pay = df['Payment Method'].astype(str).value_counts().reset_index()
                    pay.columns = ['Method','Count']
                    fig_p = px.pie(pay, names='Method', values='Count', title='Payment Method Distribution',
                                   hole=0.38, color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#f75f7b','#a78bfa'])
                    st.plotly_chart(dark_chart(fig_p), width="stretch")
            r2c1, r2c2 = st.columns(2)
            with r2c1:
                if 'Subscription Status' in df.columns:
                    sub = df.groupby(df['Subscription Status'].astype(str))['Purchase Amount (USD)'].agg(
                        ['mean','median','count']).reset_index()
                    sub.columns = ['Status','Avg Purchase','Median Purchase','Count']
                    fig_sub = px.bar(sub, x='Status', y=['Avg Purchase','Median Purchase'],
                                     title='Purchase Amount: Subscriber vs Non-Subscriber',
                                     barmode='group', color_discrete_sequence=['#4f8ef7','#34d9b3'])
                    st.plotly_chart(dark_chart(fig_sub), width="stretch")
            with r2c2:
                if 'Discount Applied' in df.columns:
                    disc = df.groupby(df['Discount Applied'].astype(str))['Purchase Amount (USD)'].agg(['mean','count']).reset_index()
                    disc.columns = ['Discount','Avg Purchase','Count']
                    fig_d = px.bar(disc, x='Discount', y='Avg Purchase',
                                   title='Avg Purchase: Discount Applied vs Not',
                                   color='Discount', color_discrete_sequence=['#f75f7b','#34d9b3'])
                    fig_d.update_traces(marker_line_width=0)
                    st.plotly_chart(dark_chart(fig_d), width="stretch")

        divider()
        section("Customer Loyalty & Frequency")
        c1, c2 = st.columns(2)
        with c1:
            if '11_customer_loyalty' in images:
                show_image(images, '11_customer_loyalty')
            elif 'Frequency of Purchases' in df.columns:
                freq = df['Frequency of Purchases'].astype(str).value_counts().reset_index()
                freq.columns = ['Frequency','Count']
                fig_f = px.bar(freq, x='Frequency', y='Count', title='Purchase Frequency Distribution',
                               color='Count', color_continuous_scale=[[0,'#1a1e28'],[1,'#4f8ef7']])
                fig_f.update_layout(coloraxis_showscale=False)
                fig_f.update_traces(marker_line_width=0)
                st.plotly_chart(dark_chart(fig_f), width="stretch")
        with c2:
            if '12_geographic_distribution' in images:
                show_image(images, '12_geographic_distribution')
            elif 'Location' in df.columns:
                loc = df.groupby(df['Location'].astype(str))['Purchase Amount (USD)'].agg(
                    ['mean','count']).reset_index().sort_values('mean', ascending=False).head(15)
                loc.columns = ['Location','Avg Purchase','Count']
                fig_l = px.bar(loc, x='Avg Purchase', y='Location', orientation='h',
                               title='Top 15 Locations by Avg Purchase',
                               color='Avg Purchase', color_continuous_scale=[[0,'#1a1e28'],[1,'#34d9b3']])
                fig_l.update_layout(
                    coloraxis_showscale=False,
                    height=480,
                    yaxis=dict(autorange='reversed')
                )
                st.plotly_chart(dark_chart(fig_l), width="stretch")


# ============================================================================
# PAGE: SEGMENTATION
# ============================================================================

def page_segmentation(df, analysis_data):
    st.markdown('<div class="page-eyebrow">◆ Segment Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Customer <span>Segments</span></div>', unsafe_allow_html=True)

    info_banner("Behavioral Segmentation",
                "Purchase frequency and spend buckets identify distinct customer cohorts.")

    freq_col    = 'Frequency of Purchases'
    weekly_pct  = (df[freq_col].astype(str) == 'Weekly').sum() / len(df) * 100 if freq_col in df.columns else 0
    monthly_pct = (df[freq_col].astype(str) == 'Monthly').sum() / len(df) * 100 if freq_col in df.columns else 0
    high_spend  = (df['Purchase Amount (USD)'] >= df['Purchase Amount (USD)'].quantile(0.75)).sum()
    repeat_pct  = (df['Previous Purchases'] > df['Previous Purchases'].median()).sum() / len(df) * 100 if 'Previous Purchases' in df.columns else 0

    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, "Weekly Buyers",    f"{weekly_pct:.1f}%",   icon="◈", accent="#4f8ef7")
    kpi(c2, "Monthly Buyers",   f"{monthly_pct:.1f}%",  icon="⬡", accent="#34d9b3")
    kpi(c3, "High Spenders",    f"{high_spend:,}",       icon="◇", accent="#f0b429")
    kpi(c4, "Above-Avg Repeat", f"{repeat_pct:.1f}%",   icon="◎", accent="#a78bfa")

    divider()

    if 'segments' in analysis_data and not analysis_data['segments'].empty:
        seg_df = analysis_data['segments'].copy()

        if 'Purchase Amount (USD)' not in seg_df.columns:
            if 'Customer ID' in seg_df.columns and 'Customer ID' in df.columns:
                purchase_map = (df.drop_duplicates('Customer ID')
                                  .set_index('Customer ID')['Purchase Amount (USD)'])
                seg_df['Purchase Amount (USD)'] = seg_df['Customer ID'].map(purchase_map)

            if ('Purchase Amount (USD)' not in seg_df.columns or
                    seg_df['Purchase Amount (USD)'].isna().all()):
                seg_df = seg_df.reset_index(drop=True)
                seg_df['Purchase Amount (USD)'] = (
                    df['Purchase Amount (USD)']
                    .reset_index(drop=True)
                    .reindex(seg_df.index)
                    .fillna(df['Purchase Amount (USD)'].mean())
                )

        if 'freq_per_year' in seg_df.columns:
            seg_df['freq_category'] = pd.cut(
                seg_df['freq_per_year'], bins=[-1, 1, 6, 12, 999],
                labels=['Very Low', 'Low', 'Medium', 'High']
            )
            tab1, tab2, tab3 = st.tabs(["Distribution", "Spend Analysis", "Segment Details"])
            with tab1:
                section("Frequency Segment Breakdown")
                c1, c2 = st.columns(2)
                with c1:
                    seg_cnt = seg_df['freq_category'].value_counts().sort_index()
                    fig = px.pie(values=seg_cnt.values, names=seg_cnt.index,
                                 title='Customers by Purchase Frequency', hole=0.42,
                                 color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#a78bfa'])
                    fig.update_traces(textposition='outside')
                    st.plotly_chart(dark_chart(fig), width="stretch")
                with c2:
                    section("Segment Sizes")
                    stats_disp = pd.DataFrame({
                        'Segment': seg_cnt.index, 'Count': seg_cnt.values,
                        'Share (%)': (seg_cnt.values / len(seg_df) * 100).round(1)
                    })
                    st.dataframe(stats_disp, width="stretch", hide_index=True)
            with tab2:
                section("Spend by Segment")
                c1, c2 = st.columns(2)
                with c1:
                    seg_sp = seg_df.groupby('freq_category', observed=True)['Purchase Amount (USD)'].mean().reset_index()
                    fig = px.bar(seg_sp, x='freq_category', y='Purchase Amount (USD)',
                                 title='Average Purchase by Segment',
                                 labels={'freq_category':'Segment','Purchase Amount (USD)':'Avg ($)'},
                                 color='Purchase Amount (USD)',
                                 color_continuous_scale=[[0,'#1a1e28'],[1,'#4f8ef7']])
                    fig.update_layout(coloraxis_showscale=False)
                    st.plotly_chart(dark_chart(fig), width="stretch")
                with c2:
                    sp_stats = seg_df.groupby('freq_category', observed=True)['Purchase Amount (USD)'].agg(
                        Mean='mean', Median='median', Total='sum').round(2)
                    st.dataframe(sp_stats, width="stretch")
            with tab3:
                section("Full Segment Profile")
                summary = seg_df.groupby('freq_category', observed=True).agg(
                    Customers=('Customer ID','count'),
                    Avg_Purchase=('Purchase Amount (USD)','mean'),
                    Median_Purchase=('Purchase Amount (USD)','median'),
                    Std_Dev=('Purchase Amount (USD)','std'),
                    Min=('Purchase Amount (USD)','min'),
                    Max=('Purchase Amount (USD)','max')
                ).round(2)
                st.dataframe(summary, width="stretch")
    else:
        tab1, tab2, tab3, tab4 = st.tabs(["Frequency Segments", "Spend Segments", "Demographics", "RFM Overview"])

        with tab1:
            section("Purchase Frequency Segmentation")
            if freq_col in df.columns:
                c1, c2 = st.columns(2)
                with c1:
                    freq_counts = df[freq_col].astype(str).value_counts().reset_index()
                    freq_counts.columns = ['Frequency', 'Count']
                    fig = px.pie(freq_counts, names='Frequency', values='Count',
                                 title='Customer Distribution by Purchase Frequency', hole=0.40,
                                 color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#a78bfa','#f75f7b'])
                    fig.update_traces(textposition='outside', textinfo='percent+label')
                    st.plotly_chart(dark_chart(fig), width="stretch")
                with c2:
                    freq_spend = df.groupby(df[freq_col].astype(str))['Purchase Amount (USD)'].agg(
                        ['count','mean','median','sum']).reset_index()
                    freq_spend.columns = ['Frequency','Count','Avg Purchase','Median','Total Revenue']
                    freq_spend = freq_spend.round(2)
                    freq_spend['Share %'] = (freq_spend['Count']/len(df)*100).round(1)
                    st.dataframe(freq_spend, width="stretch", hide_index=True)
                    best = freq_spend.sort_values('Avg Purchase', ascending=False).iloc[0]
                    insight("Highest Value Segment",
                            f"<strong>{best['Frequency']}</strong> buyers have the highest average spend at "
                            f"<strong>{fmt_usd(best['Avg Purchase'])}</strong>.", "success")

                divider()
                section("Spend by Frequency")
                fig2 = px.bar(freq_spend, x='Frequency', y='Avg Purchase',
                              title='Average Purchase Amount by Frequency',
                              color='Avg Purchase',
                              color_continuous_scale=[[0,'#1a1e28'],[1,'#4f8ef7']])
                fig2.update_layout(coloraxis_showscale=False)
                fig2.update_traces(marker_line_width=0)
                st.plotly_chart(dark_chart(fig2), width="stretch")

        with tab2:
            section("Spend-Based Segmentation")
            df_seg = df.copy()
            q1 = df_seg['Purchase Amount (USD)'].quantile(0.25)
            q2 = df_seg['Purchase Amount (USD)'].quantile(0.50)
            q3 = df_seg['Purchase Amount (USD)'].quantile(0.75)
            df_seg['Spend Tier'] = pd.cut(
                df_seg['Purchase Amount (USD)'],
                bins=[-1, q1, q2, q3, float('inf')],
                labels=['Budget (<Q1)', 'Mid (Q1–Q2)', 'Premium (Q2–Q3)', 'Elite (>Q3)']
            )
            c1, c2 = st.columns(2)
            with c1:
                tier_counts = df_seg['Spend Tier'].value_counts().sort_index()
                fig = px.bar(x=tier_counts.index, y=tier_counts.values,
                             title='Customer Count by Spend Tier',
                             labels={'x':'Tier','y':'Customers'},
                             color=tier_counts.values,
                             color_continuous_scale=[[0,'#1a1e28'],[1,'#34d9b3']])
                fig.update_layout(coloraxis_showscale=False)
                fig.update_traces(marker_line_width=0)
                st.plotly_chart(dark_chart(fig), width="stretch")
            with c2:
                tier_stats = df_seg.groupby('Spend Tier', observed=True)['Purchase Amount (USD)'].agg(
                    ['count','mean','median','sum']).reset_index()
                tier_stats.columns = ['Tier','Count','Avg','Median','Total Revenue']
                tier_stats = tier_stats.round(2)
                tier_stats['Share %'] = (tier_stats['Count']/len(df)*100).round(1)
                st.dataframe(tier_stats, width="stretch", hide_index=True)

            divider()
            section("Spend Tier × Category")
            tier_cat = df_seg.groupby(['Spend Tier','Category'], observed=True).size().reset_index(name='Count')
            fig3 = px.bar(tier_cat, x='Category', y='Count', color='Spend Tier',
                          barmode='stack', title='Category Breakdown per Spend Tier',
                          color_discrete_sequence=['#4f8ef7','#34d9b3','#f0b429','#a78bfa'])
            fig3.update_traces(marker_line_width=0)
            st.plotly_chart(dark_chart(fig3), width="stretch")

        with tab3:
            section("Demographic Segmentation")
            c1, c2 = st.columns(2)
            with c1:
                if 'Age' in df.columns:
                    df_ag = df.dropna(subset=['Age']).copy()
                    df_ag['Age Band'] = pd.cut(df_ag['Age'], bins=[18,25,35,45,55,70],
                                               labels=['18–25','25–35','35–45','45–55','55–70'])
                    age_cat = df_ag.groupby(['Age Band','Category'], observed=True)['Purchase Amount (USD)'].mean().reset_index()
                    age_pivot = age_cat.pivot(index='Age Band', columns='Category', values='Purchase Amount (USD)').fillna(0)
                    fig = go.Figure(data=go.Heatmap(
                        z=age_pivot.values, x=age_pivot.columns.tolist(), y=age_pivot.index.tolist(),
                        colorscale=[[0,'#1a1e28'],[0.5,'#4f8ef7'],[1,'#34d9b3']],
                        text=age_pivot.round(1).values, texttemplate='$%{text}', textfont={'size':10}
                    ))
                    fig.update_layout(title='Avg Purchase: Age Band × Category')
                    st.plotly_chart(dark_chart(fig), width="stretch")
            with c2:
                if 'Gender' in df.columns:
                    gender_cat = df.groupby([df['Gender'].astype(str), df['Category'].astype(str)])['Purchase Amount (USD)'].mean().reset_index()
                    gender_cat.columns = ['Gender', 'Category', 'Purchase Amount (USD)']
                    fig2 = px.bar(gender_cat, x='Category', y='Purchase Amount (USD)',
                                  color='Gender', barmode='group',
                                  title='Avg Purchase: Gender × Category',
                                  color_discrete_sequence=['#4f8ef7','#f75f7b'])
                    fig2.update_traces(marker_line_width=0)
                    st.plotly_chart(dark_chart(fig2), width="stretch")

        with tab4:
            section("RFM Overview (Recency-Frequency-Monetary)")
            if 'Previous Purchases' in df.columns and freq_col in df.columns:
                freq_map = {'Weekly':4,'Bi-Weekly':3,'Monthly':2,'Quarterly':1,'Annually':0,'Every 3 Months':1}
                df_rfm = df.copy()
                df_rfm['F_score'] = df_rfm[freq_col].astype(str).map(freq_map).fillna(1)
                df_rfm['M_score'] = df_rfm['Purchase Amount (USD)']
                df_rfm['R_score'] = df_rfm['Previous Purchases']
                for col in ['F_score','M_score','R_score']:
                    mn, mx = df_rfm[col].min(), df_rfm[col].max()
                    if mx > mn:
                        df_rfm[col] = ((df_rfm[col]-mn)/(mx-mn)*3+1).round(0).astype(int)
                    else:
                        df_rfm[col] = 1
                df_rfm['RFM Score'] = df_rfm['R_score'] + df_rfm['F_score'] + df_rfm['M_score']
                df_rfm['Segment'] = pd.cut(df_rfm['RFM Score'], bins=[2,5,7,9,13],
                                           labels=['At-Risk','Developing','Loyal','Champions'])
                c1, c2 = st.columns(2)
                with c1:
                    seg_cnt = df_rfm['Segment'].value_counts().sort_index()
                    fig = px.pie(values=seg_cnt.values, names=seg_cnt.index,
                                 title='RFM Segment Distribution', hole=0.42,
                                 color_discrete_sequence=['#f75f7b','#f0b429','#4f8ef7','#34d9b3'])
                    fig.update_traces(textposition='outside', textinfo='percent+label')
                    st.plotly_chart(dark_chart(fig), width="stretch")
                with c2:
                    rfm_stats = df_rfm.groupby('Segment', observed=True)['Purchase Amount (USD)'].agg(
                        ['count','mean','sum']).reset_index()
                    rfm_stats.columns = ['Segment','Count','Avg Purchase','Total Revenue']
                    rfm_stats = rfm_stats.round(2)
                    rfm_stats['Share %'] = (rfm_stats['Count']/len(df)*100).round(1)
                    st.dataframe(rfm_stats, width="stretch", hide_index=True)
                    champ_count = rfm_stats[rfm_stats['Segment']=='Champions']['Count'].sum()
                    risk_count  = rfm_stats[rfm_stats['Segment']=='At-Risk']['Count'].sum()
                    insight("Champions",
                            f"Your top RFM segment has <strong>{champ_count:,}</strong> "
                            "customers. Prioritise retention with exclusive offers.", "success")
                    insight("At-Risk",
                            f"<strong>{risk_count:,}</strong> customers are "
                            "at risk of churning. Launch a win-back campaign immediately.", "warning")


# ============================================================================
# PAGE: INSIGHTS
# ============================================================================

def page_insights(df, analysis_data):
    st.markdown('<div class="page-eyebrow">◆ Strategy Layer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Insights & <span>Recommendations</span></div>', unsafe_allow_html=True)

    info_banner("Executive Intelligence",
                "Data-driven findings and strategic actions derived from the full analysis pipeline.")

    tab1, tab2, tab3 = st.tabs(["Key Findings", "Recommendations", "Statistical Analysis"])

    with tab1:
        section("Data-Driven Findings")
        top_cat   = df['Category'].astype(str).value_counts().index[0]
        top_cat_n = df['Category'].astype(str).value_counts().iloc[0]
        top_loc   = df['Location'].astype(str).value_counts().index[0]
        avg_age   = df['Age'].mean()
        avg_pur   = df['Purchase Amount (USD)'].mean()
        sat_pct   = (df['Review Rating'] >= 4).sum() / len(df) * 100
        sub_pct   = (df['Subscription Status'].astype(str) == 'Yes').sum() / len(df) * 100 if 'Subscription Status' in df.columns else 0
        promo_pct = (df['Promo Code Used'].astype(str) == 'Yes').sum() / len(df) * 100 if 'Promo Code Used' in df.columns else 0
        top_pay   = df['Payment Method'].astype(str).value_counts().index[0] if 'Payment Method' in df.columns else 'N/A'
        top_ship  = df['Shipping Type'].astype(str).value_counts().index[0] if 'Shipping Type' in df.columns else 'N/A'
        disc_avg  = df[df['Discount Applied'].astype(str)=='Yes']['Purchase Amount (USD)'].mean() if 'Discount Applied' in df.columns else 0
        nodisc_avg= df[df['Discount Applied'].astype(str)=='No']['Purchase Amount (USD)'].mean() if 'Discount Applied' in df.columns else 0

        c1, c2 = st.columns(2)
        with c1:
            insight("Top Category",
                    f"<strong>{top_cat}</strong> dominates with <strong>{top_cat_n:,}</strong> purchases "
                    f"({top_cat_n/len(df)*100:.1f}% of all transactions).", "success")
            insight("Primary Market",
                    f"<strong>{top_loc}</strong> is the top-performing location, accounting for "
                    f"<strong>{df['Location'].astype(str).value_counts().iloc[0]/len(df)*100:.1f}%</strong> of volume.", "warning")
            insight("Average Spend",
                    f"Customers spend an average of <strong>{fmt_usd(avg_pur)}</strong> per transaction. "
                    f"Median is <strong>{fmt_usd(df['Purchase Amount (USD)'].median())}</strong>.", "danger")
            insight("Satisfaction",
                    f"<strong>{sat_pct:.1f}%</strong> of customers rated their experience 4+ stars. "
                    f"Average rating: <strong>{df['Review Rating'].mean():.2f}/5</strong>.", "violet")
        with c2:
            insight("Subscription Rate",
                    f"<strong>{sub_pct:.1f}%</strong> of customers hold an active subscription. "
                    "Growing this base is the fastest path to higher LTV.", "violet")
            insight("Promo Code Usage",
                    f"<strong>{promo_pct:.1f}%</strong> of purchases used a promo code. "
                    f"Discount buyers average <strong>{fmt_usd(disc_avg)}</strong> vs "
                    f"<strong>{fmt_usd(nodisc_avg)}</strong> without.", "danger")
            insight("Top Payment Method",
                    f"<strong>{top_pay}</strong> is the most used payment method. "
                    "Optimising checkout for this method can reduce drop-off.", "warning")
            insight("Top Shipping Type",
                    f"<strong>{top_ship}</strong> is the most selected shipping option. "
                    "Consider negotiating bulk rates with that carrier.", "success")

        if 'insights' in analysis_data and analysis_data['insights'].strip():
            divider()
            section("Full Pipeline Report")
            with st.expander("View raw insights file", expanded=False):
                st.code(analysis_data['insights'], language='text')

    with tab2:
        section("Strategic Recommendations")
        top_cat  = df['Category'].astype(str).value_counts().index[0]
        avg_age  = df['Age'].mean()
        top_ship = df['Shipping Type'].astype(str).value_counts().index[0] if 'Shipping Type' in df.columns else 'N/A'
        disc_avg  = df[df['Discount Applied'].astype(str)=='Yes']['Purchase Amount (USD)'].mean() if 'Discount Applied' in df.columns else 0
        nodisc_avg= df[df['Discount Applied'].astype(str)=='No']['Purchase Amount (USD)'].mean() if 'Discount Applied' in df.columns else 0
        sub_pct   = (df['Subscription Status'].astype(str) == 'Yes').sum() / len(df) * 100 if 'Subscription Status' in df.columns else 0
        top_loc   = df['Location'].astype(str).value_counts().index[0]

        recs = [
            ("◈", "Product Mix Optimization",
             f"Focus on <strong>{top_cat}</strong> — your top category. Allocate 40% of inventory "
             "to your top-3 performers and run category-specific promotions.", "#4f8ef7"),
            ("◎", "Customer Targeting",
             f"Average customer age is {avg_age:.0f}. Build age-specific campaigns for the 25–40 bracket "
             "which shows the highest spend potential.", "#34d9b3"),
            ("⬡", "Logistics Enhancement",
             f"<strong>{top_ship}</strong> is your top shipping choice. Partner deeper with this carrier "
             "to offer exclusive fast-delivery perks to subscribers.", "#f0b429"),
            ("◇", "Discount Strategy",
             f"Discount buyers spend <strong>{fmt_usd(disc_avg)}</strong> vs "
             f"<strong>{fmt_usd(nodisc_avg)}</strong> for non-discount. "
             "Test targeted discounts on low-frequency segments only.", "#a78bfa"),
            ("⬡", "Subscription Growth",
             f"Only <strong>{sub_pct:.1f}%</strong> are subscribers. A tiered loyalty programme could "
             "convert high-frequency shoppers and raise customer LTV by 2–3×.", "#f75f7b"),
            ("◈", "Geographic Expansion",
             f"<strong>{top_loc}</strong> leads by volume. Identify the next 5 high-potential states "
             "by mapping spend per capita against current market penetration.", "#34d9b3"),
        ]

        for row_start in range(0, len(recs), 3):
            cols = st.columns(3, gap="medium")
            for j, rec in enumerate(recs[row_start:row_start+3]):
                icon, title, body, clr = rec
                with cols[j]:
                    st.markdown(f"""
                    <div class="rec-card">
                        <span class="rec-icon" style="color:{clr};">{icon}</span>
                        <div class="rec-title">{title}</div>
                        <div class="rec-body">{body}</div>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    with tab3:
        section("Statistical Test Results")
        try:
            from scipy import stats as scipy_stats

            test_rows = []
            test_insights = []

            if 'Gender' in df.columns:
                male   = df[df['Gender'].astype(str)=='Male']['Purchase Amount (USD)'].dropna()
                female = df[df['Gender'].astype(str)=='Female']['Purchase Amount (USD)'].dropna()
                if len(male) > 1 and len(female) > 1:
                    t, p = scipy_stats.ttest_ind(male, female)
                    sig = p < 0.05
                    test_rows.append(('Independent t-test', 'Male vs Female Purchase Amount',
                                       f"{t:.4f}", f"{p:.6f}", '✓ Yes' if sig else '✗ No'))
                    test_insights.append(("t-test: Male vs Female Spend",
                        f"t = <strong>{t:.4f}</strong>, p = <strong>{p:.6f}</strong> — "
                        f"{'Significant gender difference in spending' if sig else 'No significant gender difference in spending'}.",
                        "success" if sig else "warning"))

            if 'Season' in df.columns:
                groups = [g['Purchase Amount (USD)'].dropna().values
                          for _, g in df.groupby(df['Season'].astype(str)) if len(g) > 1]
                if len(groups) >= 2:
                    F, p = scipy_stats.f_oneway(*groups)
                    sig = p < 0.05
                    test_rows.append(('One-way ANOVA', 'Purchase Amount by Season',
                                       f"{F:.4f}", f"{p:.6f}", '✓ Yes' if sig else '✗ No'))
                    test_insights.append(("ANOVA: Purchase Amount across Seasons",
                        f"F = <strong>{F:.4f}</strong>, p = <strong>{p:.6f}</strong> — "
                        f"{'Seasonal patterns significantly affect spend' if sig else 'No significant seasonal effect on spend'}.",
                        "success" if sig else "warning"))

            if 'Category' in df.columns:
                groups = [g['Purchase Amount (USD)'].dropna().values
                          for _, g in df.groupby(df['Category'].astype(str)) if len(g) > 1]
                if len(groups) >= 2:
                    F, p = scipy_stats.f_oneway(*groups)
                    sig = p < 0.05
                    test_rows.append(('One-way ANOVA', 'Purchase Amount by Category',
                                       f"{F:.4f}", f"{p:.6f}", '✓ Yes' if sig else '✗ No'))
                    test_insights.append(("ANOVA: Purchase Amount across Categories",
                        f"F = <strong>{F:.4f}</strong>, p = <strong>{p:.6f}</strong> — "
                        f"{'Category significantly affects spend' if sig else 'No significant category effect'}.",
                        "success" if sig else "warning"))

            if 'Discount Applied' in df.columns and 'Review Rating' in df.columns:
                disc_num = (df['Discount Applied'].astype(str) == 'Yes').astype(int)
                rating   = df['Review Rating']
                mask     = rating.notna()
                r, p     = scipy_stats.pearsonr(disc_num[mask], rating[mask])
                sig = p < 0.05
                test_rows.append(('Pearson Correlation', 'Discount Applied vs Review Rating',
                                   f"{r:.4f}", f"{p:.6f}", '✓ Yes' if sig else '✗ No'))
                test_insights.append(("Correlation: Discount Applied vs Review Rating",
                    f"r = <strong>{r:.4f}</strong>, p = <strong>{p:.6f}</strong> — "
                    f"{'Significant correlation found' if sig else 'No significant correlation'}.",
                    "success" if sig else "warning"))

            if test_rows:
                test_df = pd.DataFrame(test_rows,
                                       columns=['Test Type', 'Variables', 'Statistic', 'p-value', 'Significant (p<0.05)'])
                st.dataframe(test_df, width="stretch", hide_index=True)
                divider()
                section("Detailed Interpretations")
                for label, body, kind in test_insights:
                    insight(label, body, kind)

        except ImportError:
            insight("SciPy Not Available",
                    "Install <strong>scipy</strong> in your requirements.txt to enable statistical tests.", "warning")

        if 'statistical_tests' in analysis_data and analysis_data['statistical_tests'].strip():
            divider()
            with st.expander("Raw analysis file output", expanded=False):
                st.code(analysis_data['statistical_tests'].strip(), language='text')

    divider()
    section("Implementation Roadmap")
    p1, p2, p3 = st.columns(3, gap="medium")
    with p1:
        st.markdown("""
        <div class="phase-card">
            <div class="phase-num">01</div>
            <div class="phase-title">Validation</div>
            <ul class="phase-list">
                <li>Confirm findings with data team</li>
                <li>Validate data quality thresholds</li>
                <li>Establish monitoring systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with p2:
        st.markdown("""
        <div class="phase-card">
            <div class="phase-num">02</div>
            <div class="phase-title">Deep Analysis</div>
            <ul class="phase-list">
                <li>Conduct RFM analysis</li>
                <li>Perform cohort analysis</li>
                <li>Build time-series forecasts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with p3:
        st.markdown("""
        <div class="phase-card">
            <div class="phase-num">03</div>
            <div class="phase-title">Implementation</div>
            <ul class="phase-list">
                <li>Develop targeted campaigns</li>
                <li>A/B test strategic changes</li>
                <li>Monitor KPIs continuously</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    # Load data — errors are now returned, not raised inside cached functions
    df, load_error = load_main_data()
    analysis_data, output_dir = load_analysis_files()
    images = load_images()

    if df is None:
        st.error(f"⚠️ Unable to load dataset: {load_error}")
        st.info("Please ensure `Customer_shopping_data_.csv` is in the same directory as this app.")
        st.stop()

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
            "⬡  Dataset":        "preview",
            "◎  Data Quality":   "quality",
            "◈  Univariate":     "univariate",
            "⬡  Multivariate":   "multivariate",
            "◇  Segmentation":   "segmentation",
            "◆  Insights":       "insights",
        }

        selected = st.radio("nav", list(page_options.keys()), label_visibility="collapsed")
        page_key = page_options[selected]

        st.divider()

        st.markdown('<div class="nav-section-title">Dataset Snapshot</div>', unsafe_allow_html=True)
        for label, val in [
            ("Records",      f"{len(df):,}"),
            ("Columns",      f"{df.shape[1]}"),
            ("Avg Purchase", fmt_usd(df['Purchase Amount (USD)'].mean())),
            ("Avg Rating",   f"{df['Review Rating'].mean():.2f} / 5"),
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

    if   page_key == "home":         page_home(df, analysis_data)
    elif page_key == "preview":      page_dataset_preview(df)
    elif page_key == "quality":      page_data_quality(df, analysis_data, images)
    elif page_key == "univariate":   page_univariate_analysis(df, images)
    elif page_key == "multivariate": page_multivariate_analysis(df, images, analysis_data)
    elif page_key == "segmentation": page_segmentation(df, analysis_data)
    elif page_key == "insights":     page_insights(df, analysis_data)

    divider()
    st.markdown("""
    <div style="text-align:center; color:#3a4155; font-size:0.78rem; padding:1rem 0 2rem;">
        ShopIQ Analytics · Powered by Streamlit, Plotly & Pandas
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()