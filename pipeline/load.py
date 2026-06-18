import sqlite3
import os

def load_csv(df):

    os.makedirs("processed_data", exist_ok=True)

    df.to_csv(
        "processed_data/data_gabungan.csv",
        index=False
    )

    print("CSV berhasil disimpan")


def load_database(df):

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(
        "database/penyakit_global.db"
    )

    df.to_sql(
        "kematian_penyakit",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database berhasil disimpan")