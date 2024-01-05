import pandas as pd

df = pd.DataFrame(
    {
        'Soccer club': ['Flamengo', 'Barcelona', 'Real Madrid', 'Santos'], 
        'Country': ['Brazil', 'Spain', 'Spain', 'Brazil'],
        'Value': [1.2, 3.5, 4.2, 0.9],
        'Squad size': [25, 23, 24, 22]
    },
)


# Index-based selection
print(df.iloc[0]) # First row: returns a Series
print(df.iloc[1:3]) # First row: returns a DataFrame
print(df.iloc[1, 0]) # Element in the second row and first column
print(df.iloc[-1]) # Last row
print(df.iloc[0:2]) # First two rows

# Label-based selection
print(df.loc[0]) # First row: returns a Series
print(df.loc[1:3]) # First row: returns a DataFrame
print(df.loc[1, 'Soccer club']) # Element in the second row and first column
print(df.loc[0:2]) # Lines 0, 1 and 2


# Setting the index
df = df.set_index('Soccer club')
print(df.loc['Flamengo']) # Accessing by label (only works with loc)


# Conditionals
condition = df['Country'] == 'Brazil' # Returns a Series of booleans
print(df[condition]) # All rows where Country is Brazil (returns a DataFrame)

condition = df['Country'] == 'Brazil' & df['Value'] > 1.0 # Returns a Series of booleans
print(df[condition]) # All rows where Country is Brazil and Value is greater than 1.0 (returns a DataFrame)

# Built-in functions
# isin and isnull (and notnull)
condition = df['Country'].isin(['Brazil'])
print(df[condition]) # All rows where Country is Brazil (returns a DataFrame)

condition = df['Country'].isnull()
print(df[condition]) # All rows where Country is null (returns a DataFrame)