import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 4), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three', 'four'])

print(df)
print(df.loc['c'])

print(df.describe())