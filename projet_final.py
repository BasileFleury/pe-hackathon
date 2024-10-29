import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import common
df = common.load_data()

#Normalisation des données
df1 = df.copy()
df1["Affect"] = df1["Positive affect"] - df1["Negative affect"]
df1.drop(columns = ["Positive affect", "Negative affect"], inplace = True)

for col in ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect']:
    common.normalize_avec_zero(df1,col)

#Création de la table de données des moyennes
df2 = df1.pivot_table(values = ['Life Ladder', 'Log GDP per capita',
       'Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption', 'Affect'], index = "Country name", aggfunc = "mean")

#Fonction pour calculer l'index
df2["Joy"] = 0
for col in df2.columns :
    df2["Joy"] += df2[col]

common.normalize_sans_zero(df2,"Joy")

#Dessiner la carte
import geopandas as gpd

df3 = df2.copy()
world = gpd.read_file('map data/ne_110m_admin_0_countries.shp')
merged = world.set_index('SOVEREIGNT').join(df3)

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged.boundary.plot(ax=ax, linewidth=1)
merged.plot(column='Joy', ax=ax, legend=True,
            legend_kwds={'label': "Joy Level",
                         'orientation': "vertical"},
            cmap='coolwarm')

plt.title('Joy Index by Country')
plt.show()