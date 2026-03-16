import pandas as pd

df = pd.read_csv("Cars.csv", sep=";")

"""---------------------------------------------------------
2. FIX DECIMAL FORMAT FOR NUMERIC COLUMNS
    (Our dataset uses commas for decimals, e.g., "18,0" so we 
    are going to fix that and replace the commas with periods.)
---------------------------------------------------------"""

numeric_cols = ["MPG", "Displacement", "Horsepower", "Acceleration"]

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(",", ".")
    df[col] = pd.to_numeric(df[col], errors="coerce")

"""---------------------------------------------------------
3. SORTING EXAMPLES
---------------------------------------------------------"""


# Sort by a single column (ascending)
print("Sort by MPG (lowest to highest):")
print(df.sort_values(by="MPG", ascending=True).head(), "\n")


# Sort by a single column (descending)
print("Sort by MPG (highest to lowest):")
print(df.sort_values(by="MPG", ascending=False).head(), "\n")


# Sort alphabetically by car name
print("Sort alphabetically by Car name:")
print(df.sort_values(by="Car").head(), "\n")


# Sort by multiple columns
# Example: sort by Origin, then MPG within each Origin
print("Sort by Origin, then MPG (descending within each Origin):")
print(df.sort_values(by=["Origin", "MPG"], ascending=[True, False]).head(10), "\n")


# Sort by index (ascending)
print("Sort by index (ascending):")
print(df.sort_index().head(), "\n")


# Sort by index (descending)
print("Sort by index (descending):")
print(df.sort_index(ascending=False).head(), "\n")


# Sort with missing values first
print("Sort Horsepower with NaN values first:")
print(df.sort_values(by="Horsepower", na_position="first").head(10), "\n")


# Permanent sort (overwrite DataFrame)
df_sorted = df.sort_values(by="Weight", ascending=True)
print("Permanent sort example (sorted by Weight):")
print(df_sorted.head(), "\n")

# If you wanted to overwrite df itself:
# df = df.sort_values(by="Weight", ascending=True)

