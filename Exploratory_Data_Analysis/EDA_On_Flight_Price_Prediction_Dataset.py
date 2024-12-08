import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

pd.set_option('display.width', None)

df = pd.read_excel('flight_price.xlsx')
print(df.head())

""" Applying Feature Engineering and EDA to Clean the data """

""" Get the basic information of the data """
# print(df.info())  # Give summary of the data

# Most of the columns are object type. So while converting into numerical format we need to typecase like int or float

# print(df.describe())    # Give Statistical information (Applied only for numerical Feature)

""" 1. Data_of_journey (24/03/2019 - object_type(string)) Model will not understand. 
       Using Feature Engineering we will separate data, month and year """

# Split data based on '/' and take their respective index and finally convert it to INT type
df['Date'] = df['Date_of_Journey'].str.split('/').str[0]
df['Month'] = df['Date_of_Journey'].str.split('/').str[1]
df['Year'] = df['Date_of_Journey'].str.split('/').str[2]

# print(df.head())  # verifying applied properly or not and still above 3 columns are object_type

df['Date'] = df['Date'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)

# print(df.info())

df.drop('Date_of_Journey', axis=1, inplace=True)  # Dropping Date_of_Journey column

"""2. Arrival_Time (01:10 22 Mar - object_type) date and month is not needed only hours and minutes will be extracted"""

df['Arrival_Time'] = df['Arrival_Time'].str.split(' ').str[0]  # It is for removing 22 Mar from the dataset

df['Arrival_hour'] = df['Arrival_Time'].str.split(':').str[0]
df['Arrival_min'] = df['Arrival_Time'].str.split(':').str[1]

df['Arrival_hour'] = df['Arrival_hour'].astype(int)
df['Arrival_min'] = df['Arrival_min'].astype(int)

df.drop('Arrival_Time', axis=1, inplace=True)

""" 3. Dep_Time - Converting into dep_hour and dep_min """
df['Departure_hour'] = df['Dep_Time'].str.split(':').str[0]
df['Departure_min'] = df['Dep_Time'].str.split(':').str[1]

df['Departure_hour'] = df['Departure_hour'].astype(int)
df['Departure_min'] = df['Departure_min'].astype(int)

df.drop('Dep_Time', axis=1, inplace=True)

""" 4. Total_Stops - categorical data(nan 'non-stop' '2 stops' '1 stop' '3 stops' '4 stops') """
# print(df['Total_Stops'].unique())  # To get unique data

""" In this case we can assign a label to these stops. 
    If there is less stops price will be less and more stops price will be more accordingly 
    In case of nan values we need to fill either mean, median or mode """

# print(df['Total_Stops'].value_counts()) # In this method null values cannot be checked
# print(df['Total_Stops'].isnull().sum())   # To check nul record count
# print(df[df['Total_Stops'].isnull()])    # To view that null record

""" Nan will be replace by mode """
# print(df['Total_Stops'].mode())   # Which is 1 stop (So nan will be replaced by 1)

df['Total_Stops'] = df['Total_Stops'].map(
    {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4, np.nan: 1})


""" 5. Route - We already have an source and Destination we can drop this column """
df.drop('Route', axis=1, inplace=True)


""" 6. Duration - convert into Duration_hour and Duration_min """

# Replace missing Duration values with a default
df['Duration'] = df['Duration'].fillna('0h 0m')  # Replace NaN with default '0h 0m'

# Extract hours and minutes explicitly
df['Duration_hour'] = df['Duration'].str.extract(r'(\d+)h').fillna(0).astype(int)  # Extract hours
df['Duration_min'] = df['Duration'].str.extract(r'(\d+)m').fillna(0).astype(int)  # Extract minutes

"""
Regex Explanation:
r'(\d+)h': Extract digits (\d+) followed by an h
r'(\d+)m': Extract digits (\d+) followed by an m
"""

# print(df.head())
# print("Number of NaN in Duration_min:", df['Duration_min'].isnull().sum())


""" 7. Source, Destination and Additional_Info converting into numerical feature using One-Hot-Encoding """

one_hot_encoder = OneHotEncoder()

Encoded = pd.DataFrame(one_hot_encoder.fit_transform(df[['Source', 'Destination', 'Additional_Info']]).toarray(),
                       columns=one_hot_encoder.get_feature_names_out())
# print(Encoded)

print(df.head())