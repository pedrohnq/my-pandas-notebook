import pandas as pd

# Introducing DataFrame
df = pd.DataFrame(
    {'Jan': [5000, 3500], 'Feb': [5200, 4000], 'Mar': [4750, 5000]}, 
    index = ['Wage', 'Expenses']
)

# Introducing Series
serie = pd.Series([5000, 5200, 4750], index=['Jan Wage', 'Feb Wage', 'Mar Wage'], name = 'Wages')