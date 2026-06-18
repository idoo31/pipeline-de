import sqlite3
import os

def load_csv(df):
    dir_path = os.path.abspath("processed_data")
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "data_gabungan.csv")
    
    df.to_csv(
        file_path,
        index=False
    )

    print("CSV berhasil disimpan")


def load_database(df):
    dir_path = os.path.abspath("database")
    os.makedirs(dir_path, exist_ok=True)
    db_path = os.path.join(dir_path, "penyakit_global.db")

    conn = sqlite3.connect(
        db_path
    )

    df.to_sql(
        "kematian_penyakit",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database berhasil disimpan")