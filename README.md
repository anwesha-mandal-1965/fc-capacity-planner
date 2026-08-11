# 📦 E-commerce FC Capacity & Inventory Placement Planner

An interactive supply chain planning tool that translates demand forecasts into inventory placement and capacity requirements for **BAU (Business as Usual)** and **BBD (Big Billion Days / Peak Sale)** scenarios.

Built as a portfolio project demonstrating FC-level planning, stockout risk analysis, and data-driven replenishment recommendations.

---

## 🎯 What This Project Does

1. **Generates synthetic e-commerce data** — 50 SKUs across 5 categories, 5 Fulfilment Centers, 90 days of daily demand
2. **Runs a planning engine** — Analyzes capacity utilization, stockout risk, service levels, and generates replenishment recommendations
3. **Visualizes everything** — Interactive dark-themed dashboard with charts, heatmaps, and sortable tables

## 🖥️ Dashboard Features

| Feature | Description |
|---------|-------------|
| **KPI Cards** | Total SKUs, Active FCs, Fill Rate %, Stockout Alerts — with animated counters |
| **Scenario Toggle** | Switch between BAU and BBD to compare metrics side-by-side |
| **FC Utilization Chart** | Horizontal bar chart showing storage and throughput utilization per FC |
| **Demand Forecast** | 90-day line chart with BBD spike visualization |
| **Stockout Risk Heatmap** | Category × FC matrix with color-coded risk levels |
| **Service Level Radar** | 5-axis radar comparing availability, speed, cost efficiency, capacity, resilience |
| **Replenishment Table** | Sortable, searchable table with priority badges (Critical / Urgent / Monitor) |

## 🚀 How to Run

### Step 1: Generate the Data
```bash
python generate_data.py
python planning_engine.py
```
This creates JSON files in `data/` and CSV reports in `reports/`.

### Step 2: Start a Local Server
```bash
python -m http.server 8000
```

### Step 3: Open the Dashboard
Navigate to [http://localhost:8000](http://localhost:8000) in your browser.

## 📁 Project Structure

```
fc-planner/
├── generate_data.py           # Synthetic data generation (50 SKUs, 5 FCs, 90 days)
├── planning_engine.py          # Analysis engine (capacity, risk, service levels)
├── index.html                  # Dashboard page
├── style.css                   # Dark glassmorphism styling
├── dashboard.js                # Chart logic & interactivity
├── data/                       # Generated JSON data
│   ├── fc_master.json          # FC details and capacities
│   ├── sku_master.json         # SKU catalog (50 products)
│   ├── demand_forecast.json    # 90-day BAU vs BBD demand
│   ├── capacity_analysis.json  # FC utilization metrics
│   ├── stockout_risk.json      # Risk matrix (category × FC)
│   ├── replenishment_recs.json # Replenishment recommendations
│   └── service_levels.json     # Service level metrics
├── reports/                    # CSV reports (Excel-compatible)
│   ├── inventory_placement_plan.csv
│   ├── capacity_summary.csv
│   ├── stockout_risk_report.csv
│   └── replenishment_recommendations.csv
└── README.md
```

## 🛠️ Technology Stack

| Tool | Purpose |
|------|---------|
| Python (standard library) | Data generation & analysis — no external dependencies |
| HTML / CSS / JavaScript | Interactive dashboard |
| Chart.js (CDN) | Data visualization |
| CSV | Excel-compatible reports |

## 📊 Key Metrics Explained

- **Fill Rate**: % of orders fulfilled from available inventory
- **Days of Supply (DOS)**: Current inventory ÷ daily demand — how many days stock will last
- **Stockout Risk Score**: 0–1 scale based on BBD days of supply (1 = highest risk)
- **Capacity Utilization**: Required inventory ÷ FC storage capacity × 100
- **Throughput Utilization**: Daily orders ÷ FC processing capacity × 100

## 📝 Notes

- All data is **synthetic** — generated using Python's random module with seed 42 for reproducibility
- The BBD peak window simulates a 5-day sale event (days 45–49) with category-specific demand multipliers
- Regional demand biases are applied (e.g., Delhi gets higher Appliance demand)

---

**Author**: Anwesha Mandal | **Year**: 2024
