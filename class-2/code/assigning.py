import pandas as pd


df = pd.DataFrame(
    {
        'Soccer club': ['Flamengo', 'Barcelona', 'Real Madrid', 'Santos'], 
        'Country': ['Brazil', 'Spain', 'Spain', 'Brazil'],
        'Value': [1.2, 3.5, 4.2, 0.9],
        'Squad size': [25, 23, 24, 22]
    },
)


# Assinging data as a constant
df['Value'] = 1.0

# Assinging data as a list
df['Value'] = [1.0, 2.0, 3.0, 4.0]