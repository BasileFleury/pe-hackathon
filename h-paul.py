# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import common
df = common.load_data()

# %%
df.head(5)

# %%
#df["Life Ladder"].max()
#df.loc[df["Life Ladder"].argmax()]

# %%
#df.columns
#df.shape
#df.dtypes

# %%
df1 = df.copy()
df1["Affect"] = df1["Positive affect"] - df1["Negative affect"]
df1.drop(columns = ["Positive affect", "Negative affect"], inplace = True)

for col in ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect']:
    common.normalize_avec_zero(df1,col)

#df1["Life Ladder"].min()
#df1["Life Ladder"].max()

#df.head(10)
df1.head(10)

# %%
df1.columns

# %%
#Création de la table de données
df2 = df1.pivot_table(values = ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect'], index = "Country name", aggfunc = "mean")
df2

# %%
df2["Joy"] = 0
for col in df2.columns :
    df2["Joy"] += df2[col]
df2

# %%
common.normalize_sans_zero(df2,"Joy")

# %%
df2

# %%

# %%
"""# pip install geopandas
import geopandas as gpd

df3 = df2.copy()
world = gpd.read_file('map data/ne_110m_admin_0_countries.shp')
merged = world.set_index('SOVEREIGNT').join(df3.set_index('Country name'))

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.boundary.plot(ax=ax, linewidth=1)
merged.plot(column='Joy', ax=ax, legend=True,
            legend_kwds={'label': "Bonheur",
                         'orientation': "horizontal"},
            cmap='coolwarm')

plt.title('World Happiness Index by Country')
plt.show()"""

# %%
