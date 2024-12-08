import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pd.set_option('display.max_columns', None)  # which will split into lines
pd.set_option('display.width', None)   # In single line

plt.figure(figsize=(10, 6))

df = pd.read_csv('Red_wine_dataset.csv')
# print(df.head())
#
# print(df.info())  # Non-null values, datatype (Summary of dataset)
#
# print(df.shape)  # total rows and columns
#
# print(df.describe()) # Descriptive statistics details
#
# print(df.columns)   # List down all columns in a dataset
#
# print(df['quality'].unique())   # To get unique data in target column(Quality)
#
# print(df.isnull().sum())  # To check Missing values in a dataset
#
# print(df[df.duplicated()])    # To find duplicate records in my dataset (240 duplicates)

print(df.drop_duplicates(inplace=True))    # To remove a duplicates

""" To check the correlation """
# print(df.corr())

""" To see the correlation in visualised look """
# sns.heatmap(df.corr(), annot=True)   # If we want the vales inside the color box we can use (annot)
# plt.show()

""" Visualization """
""" Conclusion : It is an Imbalanced dataset because values are not equally distributed over here """
print(df['quality'].value_counts())

# quality
# 5    577
# 6    535
# 7    167
# 4     53
# 8     17
# 3     10

# print(df['quality'].value_counts().plot(kind='bar'))
# plt.xlabel('Wine Quality')
# plt.ylabel('Count')


""" To check distribution on all columns in a dataset """
# for column in df.columns:
#     sns.histplot(df[column], kde=True)   # kde which will give distribution line over the plot
# plt.show()

""" To check distribution on individual columns in a dataset """
# sns.histplot(df['alcohol'], kde=True)
# plt.show()

""" To compare one feature with other we can use pairplot (univariate, bivariate, multivariate analysis) """
# sns.pairplot(df)   # Need to check some data....
# plt.show()

""" Categorical plot """
# sns.catplot(x='quality', y='alcohol', data=df, kind='box')  # to check any outliers and their relation
# plt.show()

sns.scatterplot(x='alcohol', y='pH', hue='quality', data=df)
plt.show()