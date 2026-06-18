import pandas as pd

def extract():

    print("EXTRACT PROCESS")

    df1 = pd.read_csv("raw_data/data1.csv")
    df2 = pd.read_csv("raw_data/data2.csv")

    print("Dataset 1:", df1.shape)
    print("Dataset 2:", df2.shape)

    return df1, df2

