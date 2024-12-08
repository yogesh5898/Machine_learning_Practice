import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

list_marks = [45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]
minimum, Q1, median, Q3, maximum = np.quantile(list_marks, [0, 0.25, 0.50, 0.75, 1.0])

print(minimum, Q1, median, Q3, maximum)   # 32.0 54.0 67.0 89.0 99.0

""" In the above dataset there is no outliers, If we have outlier then we need to calculate IQR"""

IQR = Q3 - Q1
print('IQR is', IQR)

lower_fence = Q1 - 1.5*(IQR)
higher_fence = Q3 + 1.5*(IQR)

print('higher_fence is', higher_fence)
print('lower_fence is', lower_fence)

""" If the value is < than lower_fence or > higher_fence then it is considered as outliers """
list_marks_new = [-35, 0, 45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74, 160, 170]

sns.boxplot(list_marks_new)
plt.show()