# 📊 Customer Shopping Behavior & Sales Analysis Dashboard

A professional analytics solution featuring an interactive **Streamlit web dashboard** and **Power BI business intelligence dashboard** for analyzing customer shopping behavior, sales trends, and customer segmentation.

## 🎯 Quick Overview

| Metric | Value |
|--------|-------|
| **Total Sales** | $233.1K |
| **Total Customers** | 3,900+ |
| **Avg Rating** | 3.75/5 |
| **Records** | 3,900+ transactions |

## 🚀 Features

### Streamlit Dashboard (7 Pages)
- 🏠 **Home** - Executive KPI summary
- 📋 **Dataset Preview** - Data exploration & sampling
- 🧹 **Data Quality** - Missing values, outliers detection
- 📈 **Univariate Analysis** - Distribution analysis
- 🔗 **Multivariate Analysis** - Correlations & relationships
- 👥 **Customer Segmentation** - RFM-based clustering
- 💡 **Insights & Recommendations** - Business recommendations

### Power BI Dashboard
- 📊 **Main Dashboard** - Sales by Gender, Category, Top/Bottom Products
- 📦 **Category Analysis** - Product performance breakdown
- 📍 **Location Analysis** - Regional sales distribution
- 📊 **KPI Panel** - Key metrics summary

## 📁 Project Structure

```
Customer-Shopping-Behavior-Sales-Analysis-Dashboard/
│
├── 🌐 Streamlit Dashboard
│   ├── app.py (or streamlit_dashboard.py)
│   ├── analysis_script.py
│   ├── Customer_shopping_EDA.ipynb
│   ├── requirements.txt
│   └── config.toml
│
├── 📊 Power BI
│   └── Customer Shopping Dashboard.pbix
│
├── 📁 Data
│   └── Customer_shopping_data_.csv (3,900+ records)
│
├── 📊 Analysis Output
│   ├── visualizations/ (12+ PNG charts)
│   ├── data_reports/ (CSV statistics)
│   └── statistical_reports/ (TXT findings)
│
└── 📖 Documentation
    └── README.md
```

## 📊 Dataset

- **Format:** CSV
- **Records:** 3,900+ customer transactions
- **Features:** 18 dimensions
- **Fields:** Customer ID, Age, Gender, Location, Purchase Amount, Category, Season, Rating, Subscription Status, and more

## 💻 Installation

### Prerequisites
- Python 3.9+
- Power BI Desktop (optional, for Power BI dashboard)

### Streamlit Dashboard

```bash
# Clone repository
git clone https://github.com/Goutam-Baid-zzz/Customer-Shopping-Behavior-Sales-Analysis-Dashboard.git
cd Customer-Shopping-Behavior-Sales-Analysis-Dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py
```

✅ Dashboard opens at `http://localhost:8501`

### Power BI Dashboard

1. Download `Customer Shopping Dashboard.pbix`
2. Open with Power BI Desktop
3. Use filters and visuals to explore


## 📊 Power BI Dashboard Preview

### Main Dashboard
<p align="center">
  <img width="100%" src="https://github.com/user-attachments/assets/e5e46341-224c-460b-a507-68a342032e88" alt="Main Dashboard" />
  <br>
  <b>Figure 1:</b> KPIs, Sales Distribution & Product Performance
</p>

### Detailed Analysis Views
<table align="center">
<tr>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/13793eae-ee15-46a6-b676-130ec688e307" alt="Category Analysis" /><br>
<b>Figure 2:</b><br>Category-wise Sales
</td>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/a5e181ea-d581-41f3-a39f-cdc8fbf6c8c5" alt="Location Analysis" /><br>
<b>Figure 3:</b><br>Location-based Sales
</td>
<td align="center" width="33%">
<img src="https://github.com/user-attachments/assets/98af9fb4-562d-4ffc-9c18-a948df3d2433" alt="KPI Panel" /><br>
<b>Figure 4:</b><br>Key Metrics Panel
</td>
</tr>
</table>

## 📈 Key Insights

- **Clothing** leads with 40%+ market share
- Average purchase amount: **$60**
- Gender split: **48% female, 52% male**
- Subscription members show **3x higher retention**
- Seasonal peaks identified in **winter months**
- Top customers drive **60% of revenue**

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Web Dashboard** | Streamlit, Plotly, Pandas |
| **BI Dashboard** | Power BI, DAX |
| **Data Analysis** | Python, Pandas, SciPy, Scikit-learn |
| **Notebooks** | Jupyter |

## 📂 Analysis Output

Generated reports in `analysis_output/`:

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

## 🚀 Usage

### Run Streamlit
```bash
streamlit run app.py
```

### Run Analysis Script
```bash
python analysis_script.py
```

### Jupyter Notebook
```bash
jupyter notebook Customer_shopping_EDA.ipynb
```

## 📋 Requirements

**Python Dependencies** (`requirements.txt`):
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


[⬆ Back to top](#-customer-shopping-behavior--sales-analysis-dashboard)

</div>
