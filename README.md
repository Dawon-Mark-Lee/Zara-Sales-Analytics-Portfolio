# Zara-Sales-Analytics-Portfolio
Retail Sales Performance Analysis: Promotion and Pricing Strategy
Project Overview
This project analyzes a dataset containing over 20,000 retail product transactions to identify the primary drivers of Sales Volume and uncover strategic insights regarding product positioning and pricing. The goal is to provide actionable recommendations for optimizing promotional spend and inventory strategy.

Key Analytical Findings
This analysis validates the effectiveness of promotional strategy over physical placement.

Promotion is the Dominant Factor: Promotional activities drive a significant increase in average sales volume, representing a +61% lift over non-promoted items. The physical product position (Aisle, End-cap, Front of Store) has no meaningful additional impact on sales when promotion status is isolated.

Two-Tier Pricing Strategy: The Sales Volume vs. Price scatter plot reveals two distinct performance tiers. The promotional cluster achieves high volume across a wide range of prices, effectively segmenting the market and overriding the typical inverse price-demand relationship.

Seasonality: Autumn generates the highest total sales volume. This period is critical for inventory and resource allocation planning.

Deliverables
The final output is a polished, single-page dashboard designed for executive review.

Deliverable	Description	Location
Final Dashboard PDF	High-ranking visual summary of all key findings and recommendations.	results/Business_Sales_Dashboard.pdf
Analysis Code	Jupyter Notebook demonstrating data cleaning, EDA, feature engineering, and metric calculation.	src/sales_analysis.ipynb
Raw Data	The original CSV used for the analysis.	data/Business_sales_EDA_edited.csv


Repository Structure
The repository follows a standard, reproducible structure:

Retail-Sales-Performance-Analysis/
├── data/
│   └── Business_sales_EDA_edited.csv    # Source data
├── src/
│   └── sales_analysis.ipynb             # Python analysis code
└── results/
    └── Business_Sales_Dashboard.pdf     # Final dashboard output

Tools and Technology
Category	Tools Used
Analysis	Python, Pandas, NumPy
Visualization	Tableau Public, Matplotlib, Seaborn
Version Control	Git, GitHub
