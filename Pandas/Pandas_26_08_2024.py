import pandas as pd

data = [1, 2, 3, 4]
series = pd.Series(data)
print('series :\n', series)
print(type(series))

data = {'a': 1, 'b': 2, 'c': 3}
series_dict = pd.Series(data)
print('series_dict \n', series_dict)

data = [1, 2, 4]
index = ['a', 'b', 'c']
print(pd.Series(data, index=index))

""" Dataframes """
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [28, 34, 22],
    "city": ["New York", "Los Angeles", "Chicago"]
}
print(data)
print(type(data))

df = pd.DataFrame(data)
print(df)
print(type(df))

data = [
    {'Name': 'Yogesh', 'Age': 26, 'City': 'Chennai'},
    {'Name': 'Priya', 'Age': 30, 'City': 'Mumbai'},
    {'Name': 'Rohan', 'Age': 24, 'City': 'Bangalore'}
]

df = pd.DataFrame(data)
print(df)

"""Accessing data form dataframe"""

print(df['Name'])
print(type(df), '\n')

print(df.iloc[0])  # to display the first record
print('--------------------------------------------------------------')

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 95, 80, 88]
}

df = pd.DataFrame(data)
print(df)

"""iloc Integer based indexing"""
"""Selecting a Single Cell by Position:"""

# Selecting the value in the second row (index 1), third column (index 2)
print('Getting 1st row 2nd column data :', df.iloc[1,2])

# Selecting the third row (index 2)
print("Selecting the third row :", df.iloc[2])

# Selecting the first three rows and the first two columns
print("Selecting the first three rows and the first two columns :\n ", df.iloc[0:3, 0:2])


"""loc (Label-Based Indexing)"""
# Selecting the 'Score' of the person with index 3 (which is 'David')
print("Selecting the 'Score' of the person with index 3 (which is 'David') :",df.loc[3,'Score'])

# Selecting the 'Name' column for rows with indices 1 to 3
print("Selecting the 'Name' column for rows with indices 1 to 3 : \n",df.loc[1:3, 'Name'])

# Selecting rows with indices 0 to 2 and columns 'Name' and 'City'
print("Selecting rows with indices 0 to 2 and columns 'Name' and 'City' :\n", df.loc[0:2, ['Name', 'City']])

# Selecting all rows where 'Age' is greater than 30
print('Selecting all rows where "Age" is greater than 30 :', df.loc[df['Age']>30])


"""Using 'at' we can locate the specific data"""
print(df)

print(df.at[3,'City'])
print(df.iat[2,2])


"""Data manipulation with Dataframe"""

"""Adding a column"""
df['Salary'] = [1000, 2000, 3000, 4000, 5000]
print(df)

"""Removing a column"""
#df.drop('Salary', axis=0)  # axis 0 is row (by default it will check rows)
df.drop('Salary', axis=1, inplace=True)
# (inplace=True) if you didn't assign this is to some variable we need to mention else this changes will not reflect
print(df)

df['Score'] = df['Score']+5
print(df)