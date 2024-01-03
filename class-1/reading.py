import pandas as pd


# Read CSV
wine_reviews = pd.read_csv('./winemag-data-130k-v2.csv')

# How large DataFrame is
print(wine_reviews.shape)

# Get first five rows
print(wine_reviews.head())

# Set col 0 as index instead create other column
wine_reviews = pd.read_csv('./winemag-data-130k-v2.csv', index_col=0)
