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
# à installer avant de commencer
# pip install geopandas

import common as cm
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# %%
df = pd.read_excel('DataForTable2.1WHR2023.xls')

# %%
df

# %%
world = gpd.read_file('map data/ne_110m_admin_0_countries.shp')

# %%
world

# %%
merged = world.set_index('SOVEREIGNT').join(df.set_index('Country name'))

# %%
print(merged.head())

# %%
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.boundary.plot(ax=ax, linewidth=1)
merged.plot(column='Healthy life expectancy at birth', ax=ax, legend=True,
            legend_kwds={'label': "Esperance de Vie",
                         'orientation': "horizontal"},
            cmap='coolwarm')

plt.title('World life expectancy Index by Country')
plt.show()

# %%
