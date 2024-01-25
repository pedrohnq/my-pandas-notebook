# Indexing, Selecting and Assigning 
The second class teaches how to select and assing new values to cells in a DataFrame 
and explains how indexing works

## Indexing and Selecting
### Index-based selection
It's used through the 'iloc' method and is based on numbers. For instance, we could execute 
the following code to get the value at row number 1 and column number 0:
```python
df.iloc[1, 0]
```

### Label-based selection
Sometimes, selecting by numbers is not very intuitive. In those cases, we can use a new method 
called 'loc'. It works like 'iloc', but the difference is that now we can pass the names of columns 
instead of the numbers:
```python
df.loc[0, ['Name', 'Age']]
```
Some datasets could have their index as a column. Keeping the same example, the 'Name' column 
could be used to improve searching and getting values. This way, we could set the 
column 'Name' as an index:
```python
df.set_index('Name', inplace = True)
df.loc['Pedro']
```
To select a specific column or value, we can use the following notation:
```python
df['Name'][0]
```
This will return the value in the cell at index 0 in the 'Name' column.

## Conditionals
Conditional statements can serve as a powerful means to perform basic queries within a dataframe.
```python
condition = df['Age'] == '18'
df[condition] 
```
By the way, there are some built-in functions that can be used as conditionals like 'isin' and 'isnull':
```python
condition = df['Age'].isin(['18', '19'])
df[condition]

condition = df['Age'].isnull()
df[condition]
```

# Assigning
To assign an entire column with a constant value, we can execute the following code:
```python
df['Age'] = 20
```
If we want to set a specified value for each row:
```python
df['Age'] = [19, 30,]
```