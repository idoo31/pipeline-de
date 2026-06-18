import pandas as pd

def integrate(df1_long, df2_long):

    print("INTEGRATION PROCESS")

    data_gabungan = pd.concat(
        [df1_long, df2_long],
        ignore_index=True
    )

    print("Total Data :", data_gabungan.shape)

    return data_gabungan