import pandas as pd
DATA_PATH_NAME = "DataForTable2.1WHR2023.xls"

def load_data(filename = DATA_PATH_NAME):
    df = pd.read_excel(filename)
    return df

