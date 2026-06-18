import pandas as pd
import matplotlib.pyplot as plt

def top10_penyakit(df):

    hasil = (
        df.groupby("Penyakit")["Jumlah_Kematian"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12,6))

    hasil.plot(kind="bar")

    plt.title("Top 10 Penyebab Kematian")

    plt.ylabel("Jumlah Kematian")

    plt.tight_layout()

    plt.show()