import pandas as pd

file_path = 'class-1/data/winemag-data-130k-v2.csv'

# Read CSV
wine_reviews = pd.read_csv(file_path)

# How large DataFrame is
print(wine_reviews.shape)

# Get first five rows
print(wine_reviews.head())

# Set col 0 as index instead create other column
wine_reviews = pd.read_csv(file_path, index_col=0)

