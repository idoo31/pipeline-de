def validate(df):

    print("\nVALIDATION PROCESS")

    print("Jumlah Data :", len(df))

    print("\nMissing Value")
    print(df.isnull().sum())

    print("\nDuplicate")
    print(df.duplicated().sum())

    konflik = (
        df.groupby(
            ["Negara", "Year", "Penyakit"]
        )["Jumlah_Kematian"]
        .nunique()
    )

    konflik = konflik[konflik > 1]

    print("\nJumlah Konflik :", len(konflik))

    return konflik