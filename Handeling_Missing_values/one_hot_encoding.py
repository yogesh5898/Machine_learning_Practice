import pandas as pd
from sklearn.preprocessing import OneHotEncoder

""" Creating a dataframe """
df = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red', 'green']
})

print(df.head())

""" Create a instance for oneHotEncoder """
encoder = OneHotEncoder()

""" Fit and Transform """
encoded = encoder.fit_transform(df[['color']]).toarray()

encoder_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
print(encoder_df)

""" New data """
print(encoder.transform([['blue']]).toarray())

print(pd.concat([df, encoder_df], axis=1))
