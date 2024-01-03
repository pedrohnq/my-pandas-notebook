# Creating, Reading and Writing
The first class is focused on how to create, read, and write DataFrame and Series.

## DataFrame
A DataFrame works like a table; each entry has a row and column associated with it.
To create a DataFrame, we use the `DataFrame` constructor. This constructor has many possible 
parameters, but, for the first, we will learn only 2: `data` and `index`.
- `data`: it's used to pass the range of data that will be set on entries of DataFrame;
- `index`: it's used to name the lines of DataFrame;

## Series
We can compare a Series with a list organized as a column. We also can pass data and index 
attributes, but we will learn that it is possible to name a Series; for that, we use 
the `name` attribute.

# Reading existing data
To read existing data, we can use the `read_csv` method. Pandas will load the CSV file and 
turn it into a DataFrame. Pandas, by default, sets a new column as the index of the DataFrame, 
but sometimes the DataFrame already has the index column. To fix that, we can use the `index_col` 
parameter to set what is the column we want to use as an index (the most common is column 0).