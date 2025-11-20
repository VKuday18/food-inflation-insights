📊 U.S. Food Inflation Insights (2015–Present)
A real-time inflation analysis project using BLS CPI Food Categories
This project analyzes official U.S. food inflation trends using CPI data from the Bureau of Labor Statistics (BLS).
It includes:
✔ Automated data extraction via API
✔ Data cleaning & transformation
✔ Published dashboard using Tableau Public
✔ Fully reproducible code (Python + Pandas)
✔ Organized data folder with raw + processed datasets
🔗 Live Dashboard
👉 View Here:
https://public.tableau.com/app/profile/uday.babu.dharmapuri4235/viz/U_S_FoodInflationDashboard/Dashboard1?publish=yes
This dashboard visualizes monthly food inflation across key categories (dairy, grains, fruits, vegetables, beverages, meats, etc.) from 2015 to present.
🛠️ Project Structure
food-inflation-insights/
│
├── data/
│   ├── raw/                # Raw API dumps from BLS
│   └── processed/          # Cleaned CSV ready for analysis
│
├── notebooks/
│   └── 01_extract.ipynb    # Python notebook for fetching & cleaning the data
│
├── src/
│   ├── extract.py          # Placeholder for modularized ETL code
│   └── transform.py        # Placeholder for transformations
│
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
🚀 How the Data Pipeline Works
1️⃣ Extract:
A Python script calls the BLS Public API, requesting CPI time-series for specific food categories.
2️⃣ Transform:
Data is parsed, cleaned, date-formatted, and normalized using Pandas.
3️⃣ Load:
The final dataset is exported as:
data/raw/bls_cpi_food_raw.json
data/processed/cpi_food_clean.csv
4️⃣ Visualize:
The cleaned data feeds into Tableau Public to create dynamic inflation trend visualizations.
📈 Dashboard Features
Food inflation trends by category
Category-wise comparison
Long-term inflation trajectory (2015–present)
Interactive filters
Clean, responsive design
📚 Skills Demonstrated
Data Analytics
API data collection
Exploratory data analysis (EDA)
Data wrangling & cleaning
Time-series analysis
Data Engineering
ETL pipeline design
Folder-based data architecture
Modular Python structure
Version control with GitHub
Tools
Python (Pandas, Requests)
Jupyter Notebooks
Tableau Public
Git/GitHub
macOS terminal / venv
📦 Reproducibility
To reproduce this project:
git clone https://github.com/USERNAME/food-inflation-insights
cd food-inflation-insights
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
Open the notebook:
notebooks/01_extract.ipynb
Run all cells to regenerate raw + processed data.
🧭 Next Steps (coming soon)
SQL integration (PostgreSQL or SQLite)
Streamlit web app version
AI-powered inflation summarizer (OpenAI + Pandas)
Monthly automated refresh pipeline
Power BI version of dashboard
📝 About This Project
This project demonstrates real-world skills in:
Data extraction from public APIs
Time-series analysis
Building analytics dashboards
Reproducible data pipelines
Communicating insights visually
It reflects practical, industry-level work similar to what analysts and engineers do at companies like Capital One, Amazon, Netflix, and fintech organizations.
🧠 SQL Analysis
After loading the CPI dataset into a SQLite database (data/food_inflation.db), several analytical SQL queries were run to explore long-term inflation trends.
🔍 1. Preview 5 records
SELECT * FROM food_cpi LIMIT 5;
📅 2. Date range covered in the dataset
SELECT MIN(date) AS earliest_month,
       MAX(date) AS latest_month
FROM food_cpi;
🧮 3. Total number of observations
SELECT COUNT(*) AS total_records
FROM food_cpi;
🍎 4. All available food categories
SELECT DISTINCT category
FROM food_cpi;
📊 5. Average inflation per category (2015–Present)
SELECT category,
       AVG(value) AS avg_cpi
FROM food_cpi
GROUP BY category
ORDER BY avg_cpi DESC;
🥛 6. Inflation trend for Dairy
SELECT date,
       value
FROM food_cpi
WHERE category = 'Dairy'
ORDER BY date;
📈 7. Yearly average inflation by category
SELECT SUBSTR(date, 1, 4) AS year,
       category,
       AVG(value) AS avg_yearly_cpi
FROM food_cpi
GROUP BY year, category
ORDER BY year, category;
These queries demonstrate skills in:
Filtering
DATE handling
Aggregation
Grouping
Trend analysis
Basic time-series exploration
This section shows the SQL engineering piece of the project beyond just Python/visualization.