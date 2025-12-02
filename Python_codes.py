import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Business_sales_EDA_edited.csv')

# Drop rows with missing values in 'name' or 'description'
df_clean = df.dropna(subset=['name', 'description']).copy()

# Check unique values in a key categorical column (example: Product Position)
print("Unique Product Position before cleaning:")
print(df_clean['Product Position'].unique())

# --- Phase 2: Exploratory Data Analysis (EDA) ---

# Calculate total Sales Volume by Season
season_sales = df_clean.groupby('season')['Sales Volume'].sum().sort_values(ascending=False).reset_index()
print("\nTotal Sales Volume by Season:")
# Results: Autumn is the highest selling season.
print(season_sales.to_markdown(index=False, numalign="left", stralign="left"))

# Create a visualization (Bar chart of Sales Volume by Season)
plt.figure(figsize=(8, 5))
sns.barplot(x='season', y='Sales Volume', data=df_clean, hue='season', palette='viridis', legend=False)
plt.title('Total Sales Volume by Season', fontsize=14)
plt.xlabel('Season', fontsize=12)
plt.ylabel('Total Sales Volume', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sales_volume_by_season.png')
plt.close()

# --- Phase 3: Key Business Questions (Promotional Effectiveness) ---

# Q1: Compare mean Sales Volume by Promotion and Product Position
promo_position_sales = df_clean.groupby(['Promotion', 'Product Position'])['Sales Volume'].mean().reset_index()
promo_position_sales = promo_position_sales.rename(columns={'Sales Volume': 'Avg Sales Volume'})

print("\nAverage Sales Volume by Promotion and Product Position:")
# Results: Promotional items consistently sell more, regardless of product position.
print(promo_position_sales.to_markdown(index=False, numalign="left", stralign="left"))
