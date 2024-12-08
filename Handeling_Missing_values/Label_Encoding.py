import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'color': ['Red', 'Green', 'Blue', 'Red', 'Green']
})

print(df.head())

""" Initialize Label_Encoder """
lbl_encoder = LabelEncoder()

""" Fit and Transform"""
lbl_encoded = lbl_encoder.fit_transform(df['color'])
print(lbl_encoded)

""" New data """
print(lbl_encoder.transform(['Blue']))
