# 📊 Customer Shopping Behavior & Sales Analysis Dashboard

> **An end-to-end analytics platform** combining an interactive Streamlit web dashboard and a Power BI business intelligence report to explore customer shopping patterns, sales trends, and behavioral segmentation.

---

## 🌐 Live Demo

| Platform | Link |
|----------|------|
| **Streamlit App** | 🚀 [customer-shopping-behavior-sales-analysis.streamlit.app](https://customer-shopping-behavior-sales-analysis.streamlit.app/) |
| **Source Code** | 📁 [GitHub Repository](https://github.com/Goutam-Baid-zzz/Customer-Shopping-Behavior-Sales-Analysis-Dashboard) |

---

## 📈 Key Metrics at a Glance

| Metric | Value |
|--------|-------|
| Total Revenue | $233.1K |
| Total Customers | 3,900+ |
| Average Rating | 3.75 / 5 |
| Dataset Size | 3,900 transactions × 18 features |

---

## 🗂️ Project Structure

```
Customer-Shopping-Behavior-Sales-Analysis-Dashboard/
│
├── 🌐 Streamlit Dashboard
│   ├── app.py
│   ├── analysis_script.py
│   ├── Customer_shopping_EDA.ipynb
│   ├── requirements.txt
│   └── config.toml
│
├── 📊 Power BI
│   └── Customer Shopping Dashboard.pbix
│
├── 📁 Data
│   └── Customer_shopping_data_.csv
│
└── 📊 Analysis Output
    ├── visualizations/        # 12+ PNG charts
    ├── data_reports/          # CSV statistics
    └── statistical_reports/   # TXT findings
```

---

## 🚀 Features

### Streamlit Dashboard — 7 Pages

| Page | Description |
|------|-------------|
| 🏠 **Home** | Executive KPI summary and quick signals |
| 📋 **Dataset Preview** | Browse, filter, and inspect raw records |
| 🧹 **Data Quality** | Completeness, outlier detection, integrity scoring |
| 📈 **Univariate Analysis** | Distribution analysis per feature |
| 🔗 **Multivariate Analysis** | Correlations, chi-square tests, interaction effects |
| 👥 **Customer Segmentation** | RFM-based cohort clustering |
| 💡 **Insights & Recommendations** | Data-driven strategy and implementation roadmap |

### Power BI Dashboard — 4 Views

| View | Description |
|------|-------------|
| 📊 **Main Dashboard** | Sales by gender, category, top/bottom products |
| 📦 **Category Analysis** | Product performance breakdown |
| 📍 **Location Analysis** | Regional sales distribution |
| 📊 **KPI Panel** | Key metrics summary |

---

## 💻 Installation & Setup

### Prerequisites

- Python 3.9+
- Power BI Desktop *(optional, for .pbix file)*

### Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Goutam-Baid-zzz/Customer-Shopping-Behavior-Sales-Analysis-Dashboard.git
cd Customer-Shopping-Behavior-Sales-Analysis-Dashboard

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# .\venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the dashboard
streamlit run app.py
```

Dashboard opens at `http://localhost:8501`

### Run Analysis Script

```bash
python analysis_script.py
```

### Open Jupyter Notebook

```bash
jupyter notebook Customer_shopping_EDA.ipynb
```

---

## 📦 Requirements

```
streamlit==1.28.0
pandas==2.0.0
plotly==5.17.0
scikit-learn==1.3.0
scipy==1.10.0
numpy==1.24.0
matplotlib==3.5.0
seaborn==0.12.0
jupyter==1.0.0
```

---

## 📊 Dataset

| Property | Detail |
|----------|--------|
| Format | CSV |
| Records | 3,900+ transactions |
| Features | 18 dimensions |
| Key Fields | Customer ID, Age, Gender, Location, Purchase Amount, Category, Season, Rating, Subscription Status, Payment Method, and more |

---

## 📂 Analysis Output Files

```
visualizations/
├── 01_customer_purchase_distribution.png
├── 02_age_demographics.png
├── 03_category_sales_volume.png
├── 04_purchase_by_category.png
├── 05_shipping_preferences.png
├── 06_satisfaction_analysis.png
├── 07_seasonal_patterns.png
├── 08_subscription_impact.png
├── 09_payment_methods.png
├── 10_discount_effectiveness.png
├── 11_customer_loyalty.png
├── 12_geographic_distribution.png
└── correlation_heatmap.png

data_reports/
├── chi_square_results.csv
├── customer_segments.csv
├── missing_values_summary.csv
├── numeric_summary_statistics.csv
├── outliers_report.csv
└── strong_correlations.csv

statistical_reports/
├── data_quality_report.txt
├── final_insights_and_recommendations.txt
└── statistical_tests_results.txt
```

---

## 📊 Power BI Dashboard Preview

### Main Dashboard
<p align="center">
  <img width="100%" src="https://github.com/user-attachments/assets/e5e46341-224c-460b-a507-68a342032e88" alt="Main Dashboard" />
  <br><b>Figure 1:</b> KPIs, Sales Distribution & Product Performance
</p>

### Detailed Analysis Views

<table align="center">
<tr>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/13793eae-ee15-46a6-b676-130ec688e307" alt="Category Analysis" /><br>
<b>Figure 2:</b> Category-wise Sales
</td>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/a5e181ea-d581-41f3-a39f-cdc8fbf6c8c5" alt="Location Analysis" /><br>
<b>Figure 3:</b> Location-based Sales
</td>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/98af9fb4-562d-4ffc-9c18-a948df3d2433" alt="KPI Panel" /><br>
<b>Figure 4:</b> Key Metrics Panel
</td>
</tr>
</table>

---

## 📈 Key Insights

- **Clothing** leads all categories with 40%+ market share
- Average purchase amount: **$60 per transaction**
- Gender split: **48% female, 52% male**
- Subscription members show **3× higher retention rates**
- Seasonal spending peaks identified in **winter months**
- Top customer cohort drives **60% of total revenue**

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Web Dashboard | Streamlit, Plotly, Pandas |
| BI Dashboard | Power BI, DAX |
| Data Analysis | Python, Pandas, SciPy, Scikit-learn |
| Notebooks | Jupyter |

---
