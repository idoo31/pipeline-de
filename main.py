from pipeline.extract import extract
from pipeline.transform import (
    transform_dataset1,
    transform_dataset2
)
from pipeline.integrate import integrate
from pipeline.validate import validate
from pipeline.load import (
    load_csv,
    load_database
)

from visualization.dashboard import (
    top10_penyakit
)

def main():

    print("=" * 60)
    print("DATA ENGINEERING PIPELINE")
    print("=" * 60)

    # EXTRACT
    df1, df2 = extract()

    # TRANSFORM
    df1_long = transform_dataset1(df1)
    df2_long = transform_dataset2(df2)

    # INTEGRATE
    data_gabungan = integrate(
        df1_long,
        df2_long
    )

    # VALIDATE
    validate(data_gabungan)

    # LOAD
    load_csv(data_gabungan)

    load_database(data_gabungan)

    # VISUALIZATION
    top10_penyakit(data_gabungan)

    print("\nPIPELINE SELESAI")


if __name__ == "__main__":
    main()