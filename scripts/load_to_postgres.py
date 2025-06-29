import pandas as pd
from sqlalchemy import create_engine

# STEP 1: Load the CSV into pandas
df = pd.read_csv("data/netflix_titles.csv")

# STEP 2: Optional - Preview first few rows
print("🔍 Preview of Data:")
print(df.head())

# STEP 3: Clean column names (optional but good practice)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# STEP 4: Connect to PostgreSQL
# NOTE: Change password if yours is different
engine = create_engine("postgresql://postgres:isha24%40@localhost:5432/hrdb")

# STEP 5: Upload to PostgreSQL
df.to_sql("netflix_titles", engine, if_exists="replace", index=False)

print("✅ Data loaded into PostgreSQL table: netflix_titles")
