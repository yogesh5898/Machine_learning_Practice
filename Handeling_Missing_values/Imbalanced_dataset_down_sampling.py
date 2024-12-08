import numpy as np
import pandas as pd
from sklearn.utils import resample

""" Set random seed for reproducibility """
np.random.seed(45)

""" Creating dataframe with 2 classes """
n_sample = 1000
class_0_article = 0.9

n_class_0 = int(n_sample * class_0_article)  # 900
n_class_1 = n_sample - n_class_0  # 100

# print(n_class_0, n_class_1)

""" Creating dataframe with imbalanced dataset """
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),  # (loc - mean,  scale - std)
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df = pd.concat([class_0, class_1]).reset_index(drop=True)
#print(df.head())
# print(df['target'].value_counts())

""" Down_sampling """
df_minority = df[df['target'] == 1]  # 100
df_majority = df[df['target'] == 0]  # 900

df_majority_down_sample = resample(df_majority, n_samples=len(df_minority), random_state=42)

# print(df_majority_down_sample)

df_down_sampled = pd.concat([df_minority, df_majority_down_sample])
print(df_down_sampled['target'].value_counts())