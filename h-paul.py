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
df = pd.read_excel("DataForTable2.1WHR2023.xls")

# %%
df.head(5)

# %%
#df["Life Ladder"].max()

#df.loc[df["Life Ladder"].argmax()]

# %%
