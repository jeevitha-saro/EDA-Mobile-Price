# -*- coding: utf-8 -*-
"""Mobile Price EDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ngeO4r_WeVTJH6I8ntl8uWEbvtYu_G5o
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
train_df = pd.read_csv('train.csv')

print(train_df.head())

print(train_df.tail())

print("Dataset Shape:", train_df.shape)

print(train_df.describe())

print("Missing Values:", train_df.isnull().sum())

train_df.dropna(inplace=True)

print(train_df.info())

train_df.columns = [col.lower().replace(' ', '_') for col in train_df.columns]

binary_cols = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']
train_df[binary_cols] = train_df[binary_cols].applymap(lambda x: 'Yes' if x==1 else 'No')

price_map = {'Low Cost': 1, 'Medium Cost': 2, 'High Cost': 3}
train_df['price_range'] = train_df['price_range'].map(price_map)

print(train_df.head())

# 2. 3G or Not 3G Mobile VS Sale Price
sns.barplot(x='three_g', y='price_range', data=train_df)
plt.title('3G or Not 3G Mobile VS Sale Price')
plt.show()

# 3. Count Plot FOR Supporting Bluetooth or NOT vs price
sns.countplot(x='blue', hue='price_range', data=train_df)
plt.title('Supporting Bluetooth or NOT vs price')
plt.show()

# 4. Relation of pixel resolution height and pixel resolution width with price range
sns.scatterplot(x='px_height', y='px_width', hue='price_range', data=train_df)
plt.title('Relation of Pixel Resolution with Price Range')
plt.show()

# 5. Relation of Screen Height and Screen Width with Price Ranges
sns.scatterplot(x='sc_h', y='sc_w', hue='price_range', data=train_df)
plt.title('Relation of Screen Size with Price Range')
plt.show()