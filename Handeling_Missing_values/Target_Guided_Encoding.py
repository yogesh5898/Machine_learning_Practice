import pandas as pd

df = pd.DataFrame({
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "New York", "Chicago"],
    "price": [250, 300, 150, 350, 240, 200]
})

Tar_guided_encoder = df.groupby('city')['price'].mean().to_dict()
print(Tar_guided_encoder)

df['city_encoded'] = df['city'].map(Tar_guided_encoder)
print(df)

print(df[['price', 'city_encoded']])