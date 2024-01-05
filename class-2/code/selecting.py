import pandas as pd


df = pd.DataFrame(
    {
        'Soccer club': ['Flamengo', 'Barcelona', 'Real Madrid', 'Santos'], 
        'Country': ['Brazil', 'Spain', 'Spain', 'Brazil']
    }
)

# Accessing a column by property
print(df.Country)

# Accessing a column by key
print(df['Soccer club'])

# Accessing a single value
print(df['Soccer club'][0])