import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    'size': ['small', 'medium', 'large', 'small', 'medium', 'large']
})

print(df.head())

""" Creating Instance of Ordinal_Encoder """
ord_encoder = OrdinalEncoder(categories=[['small', 'medium', 'large']])

""" Fit and Transform """
ord_encoded = ord_encoder.fit_transform(df[['size']])
print(ord_encoded)

""" New data """
print(ord_encoder.transform([['large']]))