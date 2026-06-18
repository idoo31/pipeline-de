import pandas as pd


def clean_dataset2_column(col):

    if col.startswith("Deaths - "):

        col = col.replace("Deaths - ", "")

        col = col.replace(
            " - Sex: Both - Age: All Ages (Number)",
            ""
        )

    return col


def transform_dataset1(df1):

    print("TRANSFORM DATASET 1")

    df1["Source_ID"] = "DB1"

    identity_columns = [
        "Country/Territory",
        "Code",
        "Year",
        "Source_ID"
    ]

    disease_columns = [
        c for c in df1.columns
        if c not in identity_columns
    ]

    df1_long = df1.melt(
        id_vars=identity_columns,
        value_vars=disease_columns,
        var_name="Penyakit",
        value_name="Jumlah_Kematian"
    )

    df1_long.rename(
        columns={
            "Country/Territory": "Negara"
        },
        inplace=True
    )

    return df1_long


def transform_dataset2(df2):

    print("TRANSFORM DATASET 2")

    df2["Source_ID"] = "DB2"

    df2.rename(
        columns={
            "Entity": "Negara"
        },
        inplace=True
    )

    df2.columns = [
        clean_dataset2_column(col)
        for col in df2.columns
    ]

    identity_columns = [
        "Negara",
        "Code",
        "Year",
        "Source_ID"
    ]

    disease_columns = [
        c for c in df2.columns
        if c not in identity_columns
    ]

    df2_long = df2.melt(
        id_vars=identity_columns,
        value_vars=disease_columns,
        var_name="Penyakit",
        value_name="Jumlah_Kematian"
    )

    df2_long["Jumlah_Kematian"] = pd.to_numeric(
        df2_long["Jumlah_Kematian"],
        errors="coerce"
    )

    df2_long = df2_long.dropna(
        subset=["Jumlah_Kematian"]
    )

    return df2_long