import pandas as pd

pd.set_option('display.width', None)  # to display all column in single line

data = pd.read_csv('ipl_data.csv')
print(data.head())

print(data.describe())  # Will check only for integer column

