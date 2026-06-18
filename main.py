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

from visualization.dashboard import tampilkan_dashboard

def main():

    print("=" * 60)
    print("DATA ENGINEERING PIPELINE")
    print("=" * 60)

    # 1. EXTRACT
    df1, df2 = extract()

    # 2. TRANSFORM
    df1_long = transform_dataset1(df1)
    df2_long = transform_dataset2(df2)

    # 3. INTEGRATE
    data_gabungan = integrate(
        df1_long,
        df2_long
    )

    # 4. VALIDATE
    validate(data_gabungan)

    # 5. LOAD
    load_csv(data_gabungan)
    load_database(data_gabungan)

    # 6. VISUALIZATION
    # Menampilkan ketiga visualisasi sekaligus dalam 1 window
    tampilkan_dashboard(data_gabungan, tahun_analisis=2019, negara="Indonesia")

    print("\nPIPELINE SELESAI")


if __name__ == "__main__":
    main()