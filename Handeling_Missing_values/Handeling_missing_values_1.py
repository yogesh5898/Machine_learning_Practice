import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')
print(df.head())

""" Check Missing values """
print(df.isnull().sum())

""" Delete the data for missing values -- In this case we will lose larger amount of data """
print(df.shape)                 # (891, 12)
print(df.dropna().shape)        # (183, 12)   deleted the row for missing data
print(df.dropna(axis=1).shape)  # (891, 9)  Deleted the column which are having missing data (axis=1 is for columns)

# If you inplace=True then it will be permanent change


""" Imputation Missing values (How to handle this) """
""" 1. Mean Value Imputation """
""" It works well if we have normally distributed data """

sns.histplot(df['Age'], kde=True)
plt.show()

""" In age column I'm going to fill mean"""
df['Age_mean'] = df['Age'].fillna(df['Age'].mean())
print(df[['Age_mean', 'Age']])


""" 2. Median Value Imputation"""
""" If there is Left/Right Skewed there will be outliers """

df['Age_median'] = df['Age'].fillna(df['Age'].median())
print(df[['Age_median', 'Age_mean', 'Age']])
print(print(df.isnull().sum()))

""" 3. Mode Value Imputation """
""" It can be used with categorical Values """

print(df['Embarked'].unique())  # ['S' 'C' 'Q' nan]  In this case this NAN will be replaced with any of the 'S' 'C' 'Q' using Mode
mode_value = df[df['Embarked'].notna()]['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(mode_value)
print(df.isnull().sum())

""" notna will remove the null data in the column and show only which has data  """