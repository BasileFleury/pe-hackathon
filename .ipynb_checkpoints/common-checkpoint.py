import pandas as pd
DATA_PATH_NAME = "DataForTable2.1WHR2023.xlsx"

def load_data(filename = DATA_PATH_NAME):
    df = pd.read_excel(filename)
    df.dropna(inplace = True)
    return df

def normalize(df):

    Columns = df.columns()
    for col in Columns:
        _min,_max = df[col].min(), df[col].max()
        df[col] = (df[col] - _min)/(_max - _min)

def normalize_sans_zero(df,col):
    _min,_max = df[col].min(), df[col].max()
    df[col] = (df[col] - _min)/(_max - _min)

def normalize_avec_zero(df,col):
    _min,_max = min(df[col].min(),0), df[col].max()
    df[col] = (df[col] - _min)/(_max - _min)






# df = load_data()
