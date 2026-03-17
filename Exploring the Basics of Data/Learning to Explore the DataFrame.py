"""---------------------------------------------------------
1. IMPORT LIBRARIES
  - Remember to install pandas and numpy first in the terminal! 
---------------------------------------------------------"""
# pandas is the main library for working with CSV/Excel data
import pandas as pd

"""---------------------------------------------------------
2. LOAD THE DATA
---------------------------------------------------------"""
df = pd.read_csv("Cars.csv")

"""---------------------------------------------------------
3. VIEWING THE DATA
---------------------------------------------------------"""

# SHOWING TOP ROWS
print("HEAD (first 5 rows):")
print(df.head(), "\n") # Show the first 5 rows by default
df.head(10)   # first 10 rows
df.head(20)   # first 20 rows
df.head(1)    # just the first row

# In short, df.head( any number ) will show the top rows up to that number
# and will only show the top 5 if you do not specify a number.

# SHOWING BOTTOM ROWS
print("TAIL (last 5 rows):")
print(df.tail(), "\n") # Show the bottom 5 rows by default
df.tail(10)   # last 10 rows
df.tail(50)   # last 50 rows
df.tail(1)    # last row only

# In short, df.tail( any number ) will show the bottom rows up to that number
# and will only show the bottom 5 if you do not specify a number.

# Show number of rows and columns
print("SHAPE (rows, columns):")
print(df.shape, "\n")

# Slicing a specific range of rows
df[0:10]      # rows 0 through 9
df[100:120]   # rows 100 through 119
df[50:]       # Leaving the second variable empty defaults to the end of the range
df[:25]       # and leaving the first empty defaults to the beginning.

# Locating specific rows or ranges
df.iloc[5]        # just row 5
df.iloc[5:15]     # rows 5–14
df.iloc[[0, 10]]  # just rows 0 and 10 

# Show column names
print("COLUMNS:")
print(df.columns, "\n")

# Slicing columns
df["Car"]                 # one column
df[["Car", "MPG"]]        # two columns
df[["Car", "MPG"]].head() # first rows of selected columns

# Locating specific columns
df.loc[0, "Car"]                 # value at row 0, column "Car"
df.loc[0:5, ["Car", "MPG"]]      # rows 0–5, selected columns
df.iloc[0:10, 0:3]               # rows 0–9, columns 0–2

# Locating specific rows and columns
df.loc[0, "Car"]                 # value at row 0, column "Car"
df.loc[0:5, ["Car", "MPG"]]      # rows 0–5, selected columns
df.iloc[0:10, 0:3]               # rows 0–9, columns 0–2


""" How is .iloc different from our simple df[0:10]? 

df[0:10] uses slicing syntax and not indexing. If your dataframe index
does NOT use 0, 1, 2, 3, etc, df[0:10] will either stop working or behave incorrectly.
.iloc can also select rows AND columns at the same time, which our simple operator cannot do. .iloc is reliable and always works.
Even if your dataframe uses years or strings as an index. 

How is .loc different from .iloc?

.loc uses label based searching while .iloc is index based. """

# Viewing a random sample of rows
df.sample(5)     # 5 random rows
df.sample(20)    # 20 random rows
df.sample(frac=0.1)  # 10% of the dataset

# Viewing ALL rows, which Pandas typically does not do to protect your screen from freezing when there is a large dataset.
pd.set_option("display.max_rows", None)
pd.reset_option("display.max_rows") # Resets this option

# Viewing ALL columns
pd.set_option("display.max_columns", None)
pd.reset_option("display.max_columns")

"""---------------------------------------------------------
 4. FIX DECIMAL FORMAT
---------------------------------------------------------"""
# Many numeric columns use commas instead of periods (e.g., "18,0")
# Replace commas with periods and convert to float
numeric_cols = ["MPG", "Displacement", "Horsepower", "Acceleration"]

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(",", ".")
    df[col] = pd.to_numeric(df[col], errors="coerce")

"""---------------------------------------------------------
5. CHECK DATA TYPES
---------------------------------------------------------"""
print("DATA TYPES:")
print(df.dtypes, "\n")

"""---------------------------------------------------------
6. SUMMARY STATISTICS
---------------------------------------------------------"""
print("SUMMARY STATISTICS:")
print(df.describe(), "\n")

"""---------------------------------------------------------
7. CHECK FOR MISSING VALUES
---------------------------------------------------------"""
print("MISSING VALUES PER COLUMN:")
print(df.isna().sum(), "\n")

"""---------------------------------------------------------
8. UNIQUE VALUES (good for categorical columns)
---------------------------------------------------------"""
print("UNIQUE ORIGINS:")
print(df["Origin"].unique(), "\n")

print("UNIQUE MODEL YEARS:")
print(df["Model"].unique(), "\n")

"""---------------------------------------------------------
9. FILTERING DATA (examples)
---------------------------------------------------------"""
# Cars with MPG greater than 30
high_mpg = df[df["MPG"] > 30]
print("CARS WITH MPG > 30:")
print(high_mpg.head(), "\n")

# Cars from Japan
japan_cars = df[df["Origin"] == "Japan"]
print("CARS FROM JAPAN:")
print(japan_cars.head(), "\n")

"""---------------------------------------------------------
10. GROUPING & AGGREGATION
---------------------------------------------------------"""
# Average MPG by country of origin
avg_mpg_by_origin = df.groupby("Origin")["MPG"].mean()
print("AVERAGE MPG BY ORIGIN:")
print(avg_mpg_by_origin, "\n")

# Average horsepower by model year
avg_hp_by_year = df.groupby("Model")["Horsepower"].mean()
print("AVERAGE HORSEPOWER BY MODEL YEAR:")
print(avg_hp_by_year, "\n")

"""---------------------------------------------------------
11. SORTING
---------------------------------------------------------"""
# Sort by MPG (highest first)
sorted_mpg = df.sort_values(by="MPG", ascending=False)
print("TOP 5 MOST FUEL-EFFICIENT CARS:")
print(sorted_mpg.head(), "\n")

# Sort by horsepower (highest first)
sorted_hp = df.sort_values(by="Horsepower", ascending=False)
print("TOP 5 MOST POWERFUL CARS:")
print(sorted_hp.head(), "\n")

"""---------------------------------------------------------
12. BASIC LOOP EXAMPLE (print all car names)
---------------------------------------------------------"""
print("ALL CAR NAMES (using a for loop):")
for car in df["Car"]:
    print(car)
print("\n")

"""---------------------------------------------------------
13. BASIC DICTIONARY EXAMPLE
---------------------------------------------------------"""
# Create a dictionary of car → MPG for the first 10 cars
car_mpg_dict = {}

for i in range(10):
    car_name = df.iloc[i]["Car"]
    mpg_value = df.iloc[i]["MPG"]
    car_mpg_dict[car_name] = mpg_value

print("FIRST 10 CARS AS A DICTIONARY:")
print(car_mpg_dict, "\n")

"""---------------------------------------------------------
14. SAVE CLEANED DATA (optional)
---------------------------------------------------------"""
# df.to_csv("Cars_cleaned.csv", index=False)
