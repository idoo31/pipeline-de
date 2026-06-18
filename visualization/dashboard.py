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


def perbandingan_4_penyakit_4_negara(df, tahun_analisis=2019):
    """Menampilkan grafik bar perbandingan 4 penyakit tertinggi pada 4 negara maju"""
    
    # 1. Menyiapkan daftar 4 negara yang akan dianalisis
    daftar_negara = ["United States", "Germany", "South Korea", "Japan"]
    
    # 2. Memfilter data hanya untuk 4 negara tersebut pada tahun analisis yang diminta
    data_per_tahun = df[(df["Negara"].isin(daftar_negara)) & (df["Year"] == tahun_analisis)].copy()
    
    # 3. Mencari 4 penyakit paling dominan secara total di ke-4 negara tersebut
    peringkat_penyakit_total = (
        data_per_tahun
        .groupby("Penyakit", as_index=False)["Jumlah_Kematian"]
        .sum()
        .sort_values("Jumlah_Kematian", ascending=False)
    )
    
    # Mengekstrak nama 4 penyakit tertinggi ke dalam list
    daftar_top4_penyakit = peringkat_penyakit_total.head(4)["Penyakit"].tolist()
    
    # 4. Memfilter dataset agar hanya mengandung 4 penyakit tertinggi tersebut
    data_perbandingan = data_per_tahun[
        data_per_tahun["Penyakit"].isin(daftar_top4_penyakit)
    ].copy()
    
    # 5. Membentuk data menjadi pivot table (Negara sebagai indeks baris, Penyakit sebagai kolom)
    tabel_perbandingan = data_perbandingan.pivot_table(
        index="Negara",
        columns="Penyakit",
        values="Jumlah_Kematian",
        aggfunc="sum"
    )
    
    # 6. Menampilkan visualisasi
    ax = tabel_perbandingan.plot(kind="bar", figsize=(14, 7))
    
    # Menambahkan label angka di atas setiap bar
    for container in ax.containers:
        labels = [f"{val:,.0f}" if not pd.isna(val) and val > 0 else "" for val in container.datavalues]
        ax.bar_label(container, labels=labels, padding=3, fontsize=8)
    
    plt.title(f"Perbandingan Jumlah Kematian Akibat 4 Penyakit Tertinggi\npada 4 Negara Maju ({tahun_analisis})")
    plt.xlabel("Negara")
    plt.ylabel("Jumlah Kematian")
    plt.xticks(rotation=0)
    
    # Menempatkan legenda (legend) di luar area grafik agar tidak menutupi bar
    plt.legend(title="Penyakit", bbox_to_anchor=(1.05, 1), loc="upper left")
    
    plt.tight_layout()
    plt.show()