from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE

x, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_clusters_per_class=1, weights=[0.90],
                           random_state=42)
""" Weights is 90% data one side and another side only 10% data """
""" X is Independent Feature and Y is dependent Feature"""
print(x, y)

df1 = pd.DataFrame(x, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)
print(final_df['target'].value_counts())

plt.scatter(final_df['f1'], final_df['f2'], c=final_df['target'])
# plt.show()

""" Applying SMOTE"""
""" Transform the dataset """

oversample = SMOTE()
x, y = oversample.fit_resample(final_df[['f1', 'f2']], final_df['target'])

print(x.shape)
print(y.shape)

print(len(y[y == 0]))
print(len(y[y == 1]))

df1 = pd.DataFrame(x, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
oversample_df = pd.concat([df1, df2], axis=1)

plt.scatter(oversample_df['f1'], oversample_df['f2'], c=oversample_df['target'])
plt.show()