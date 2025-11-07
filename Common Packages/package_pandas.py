# -----------------------------
# Pandas Basics Cheat-Sheet
# -----------------------------

import pandas as pd

# -----------------------------
# 1. SERIES
# -----------------------------
# A Series is a 1D labeled array
s = pd.Series([10, 20, 30, 40])
print("Series s:\n", s, "\n")

# -----------------------------
# 2. DATAFRAME
# -----------------------------
# A DataFrame is a 2D table
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "SF"]
}
df = pd.DataFrame(data)
print("DataFrame df:\n", df, "\n")

# -----------------------------
# 3. VIEWING DATA
# -----------------------------
print("First 5 rows:\n", df.head(), "\n")
print("Last 3 rows:\n", df.tail(3), "\n")
print("DataFrame info:\n")
df.info()
print("\nStatistics:\n", df.describe(), "\n")

# -----------------------------
# 4. SELECTING DATA
# -----------------------------
print("Select 'Name' column:\n", df['Name'], "\n")
print("Select multiple columns:\n", df[['Name','Age']], "\n")
print("Select first row by label (loc):\n", df.loc[0], "\n")
print("Select second row by position (iloc):\n", df.iloc[1], "\n")

# -----------------------------
# 5. FILTERING DATA
# -----------------------------
print("Rows where Age > 25:\n", df[df['Age'] > 25], "\n")

# -----------------------------
# 6. ADDING & DROPPING COLUMNS
# -----------------------------
df['Salary'] = [50000, 60000, 70000]
print("Added 'Salary' column:\n", df, "\n")

df = df.drop('Salary', axis=1)
print("Dropped 'Salary' column:\n", df, "\n")

# -----------------------------
# 7. READING & WRITING DATA
# -----------------------------
# df.to_csv('output.csv', index=False)
# df.to_excel('output.xlsx', index=False)
# df = pd.read_csv('file.csv')
# df = pd.read_excel('file.xlsx')

# -----------------------------
# 8. BASIC AGGREGATIONS
# -----------------------------
print("Mean Age:", df['Age'].mean())
print("Sum of Ages:", df['Age'].sum())
print("Minimum Age:", df['Age'].min())
print("Maximum Age:", df['Age'].max())
print("Frequency of Ages:\n", df['Age'].value_counts(), "\n")

# -----------------------------
# 9. SORTING
# -----------------------------
print("DataFrame sorted by Age descending:\n", df.sort_values('Age', ascending=False), "\n")

# -----------------------------
# 10. HANDLING MISSING DATA
# -----------------------------
df.loc[3] = [None, None, None]  # Add a row with missing values
print("DataFrame with missing values:\n", df, "\n")

print("Drop rows with missing values:\n", df.dropna(), "\n")
print("Fill missing values with 0:\n", df.fillna(0), "\n")
