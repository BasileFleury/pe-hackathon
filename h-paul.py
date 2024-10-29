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
df.columns
#df.shape
#df.dtypes

# %%

# %%
df1 = df.copy()
df1["Affect"] = df1["Positive affect"] - df1["Negative affect"]
df1.drop(columns = ["Positive affect", "Negative affect"], inplace = True)

for col in ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect']:
    common.normalize_avec_zero(df1,col)

#df.head(10)
df1.head(10)
#df1["Life Ladder"].min()
#df1["Life Ladder"].max()

# %%
df1.columns

# %%

# %%
df2 = df1.pivot_table(values = ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect'], index = "Country name", aggfunc = "mean")
df2

# %%

# %%
