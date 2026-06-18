import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def _plot_top10_penyakit(df, ax):
    """Plot bar chart top 10 penyebab kematian global ke dalam axes yang diberikan."""
    hasil = (
        df.groupby("Penyakit")["Jumlah_Kematian"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    bars = ax.bar(range(len(hasil)), hasil.values, color="steelblue")

    # Menambahkan label angka di atas setiap bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:,.0f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=7
        )

    ax.set_title("Top 10 Penyebab Kematian Global", fontsize=10, fontweight="bold")
    ax.set_ylabel("Jumlah Kematian", fontsize=8)
    ax.set_xlabel("Penyakit", fontsize=8)
    ax.set_xticks(range(len(hasil)))
    ax.set_xticklabels(hasil.index, rotation=40, ha="right", fontsize=7)
    ax.tick_params(axis="y", labelsize=7)


def _plot_perbandingan_4_penyakit_4_negara(df, ax, tahun_analisis=2019):
    """Plot grouped bar chart perbandingan 4 penyakit di 4 negara ke dalam axes yang diberikan."""
    daftar_negara = ["United States", "Germany", "South Korea", "Japan"]

    data_per_tahun = df[
        (df["Negara"].isin(daftar_negara)) & (df["Year"] == tahun_analisis)
    ].copy()

    peringkat_penyakit_total = (
        data_per_tahun
        .groupby("Penyakit", as_index=False)["Jumlah_Kematian"]
        .sum()
        .sort_values("Jumlah_Kematian", ascending=False)
    )

    daftar_top4_penyakit = peringkat_penyakit_total.head(4)["Penyakit"].tolist()

    data_perbandingan = data_per_tahun[
        data_per_tahun["Penyakit"].isin(daftar_top4_penyakit)
    ].copy()

    tabel_perbandingan = data_perbandingan.pivot_table(
        index="Negara",
        columns="Penyakit",
        values="Jumlah_Kematian",
        aggfunc="sum"
    )

    tabel_perbandingan.plot(kind="bar", ax=ax)

    # Menambahkan label angka di atas setiap bar
    for container in ax.containers:
        labels = [
            f"{v:,.0f}" if not pd.isna(v) and v > 0 else ""
            for v in container.datavalues
        ]
        ax.bar_label(container, labels=labels, padding=2, fontsize=6.5)

    ax.set_title(
        f"Perbandingan 4 Penyakit Tertinggi pada 4 Negara Maju ({tahun_analisis})",
        fontsize=10, fontweight="bold"
    )
    ax.set_xlabel("Negara", fontsize=8)
    ax.set_ylabel("Jumlah Kematian", fontsize=8)
    ax.tick_params(axis="x", rotation=0, labelsize=8)
    ax.tick_params(axis="y", labelsize=7)
    ax.legend(
        title="Penyakit",
        bbox_to_anchor=(1.01, 1),
        loc="upper left",
        fontsize=7,
        title_fontsize=7
    )


def _plot_proporsi_penyakit_negara(df, ax, negara="Indonesia", tahun_analisis=2019, top_n=5):
    """Plot donut chart proporsi penyakit di suatu negara ke dalam axes yang diberikan."""
    data_negara = df[
        (df["Negara"] == negara) & (df["Year"] == tahun_analisis)
    ].copy()

    if data_negara.empty:
        ax.text(
            0.5, 0.5,
            f"Data tidak ditemukan\n({negara}, {tahun_analisis})",
            ha="center", va="center", transform=ax.transAxes, fontsize=10
        )
        ax.axis("off")
        return

    proporsi = (
        data_negara.groupby("Penyakit")["Jumlah_Kematian"]
        .sum()
        .sort_values(ascending=False)
    )

    top_penyakit = proporsi.head(top_n)
    lainnya = pd.Series({"Penyakit Lainnya": proporsi.iloc[top_n:].sum()})
    data_plot = pd.concat([top_penyakit, lainnya])

    colors = plt.cm.Paired(range(len(data_plot)))

    wedges, texts, autotexts = ax.pie(
        data_plot,
        labels=data_plot.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        textprops=dict(color="black", fontsize=7.5),
        pctdistance=0.82
    )

    # Membuat lingkaran putih di tengah (efek Donut)
    centre_circle = plt.Circle((0, 0), 0.68, fc="white")
    ax.add_artist(centre_circle)

    plt.setp(autotexts, size=7.5, weight="bold")

    ax.set_title(
        f"Proporsi {top_n} Penyakit Kematian Tertinggi\ndi {negara} ({tahun_analisis})",
        fontsize=10, fontweight="bold"
    )


def tampilkan_dashboard(df, tahun_analisis=2019, negara="Indonesia"):
    """
    Menampilkan ketiga visualisasi (Top 10 Global, Perbandingan 4 Negara,
    Donut Proporsi Negara) dalam satu window secara bersamaan menggunakan GridSpec.
    """
    print("MENAMPILKAN DASHBOARD VISUALISASI...")

    # Membuat satu figure besar dengan layout GridSpec 2 baris x 2 kolom
    # Baris 0 : perbandingan 4 negara (span 2 kolom, lebih lebar)
    # Baris 1 kiri : top 10 global
    # Baris 1 kanan : donut chart proporsi negara
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle("Dashboard Analisis Kematian Penyakit Global", fontsize=14, fontweight="bold", y=1.00)

    gs = gridspec.GridSpec(
        2, 2,
        figure=fig,
        hspace=0.55,
        wspace=0.45
    )

    # Panel atas: perbandingan 4 penyakit 4 negara (span seluruh lebar)
    ax_perbandingan = fig.add_subplot(gs[0, :])

    # Panel bawah kiri: top 10 penyakit global
    ax_top10 = fig.add_subplot(gs[1, 0])

    # Panel bawah kanan: donut chart proporsi negara
    ax_donut = fig.add_subplot(gs[1, 1])

    # Render masing-masing visualisasi ke axes yang sudah ditentukan
    _plot_perbandingan_4_penyakit_4_negara(df, ax_perbandingan, tahun_analisis)
    _plot_top10_penyakit(df, ax_top10)
    _plot_proporsi_penyakit_negara(df, ax_donut, negara, tahun_analisis)

    plt.show()


# -----------------------------------------------------------------------
# Fungsi-fungsi individual di bawah ini tetap dipertahankan
# agar kompatibel jika dipanggil secara terpisah di luar pipeline utama.
# -----------------------------------------------------------------------

def top10_penyakit(df):
    """Menampilkan grafik bar 10 penyebab kematian tertinggi secara global."""
    fig, ax = plt.subplots(figsize=(12, 6))
    _plot_top10_penyakit(df, ax)
    plt.tight_layout()
    plt.show()


def perbandingan_4_penyakit_4_negara(df, tahun_analisis=2019):
    """Menampilkan grafik bar perbandingan 4 penyakit tertinggi pada 4 negara maju."""
    fig, ax = plt.subplots(figsize=(14, 7))
    _plot_perbandingan_4_penyakit_4_negara(df, ax, tahun_analisis)
    plt.tight_layout()
    plt.show()


def proporsi_penyakit_negara(df, negara="Indonesia", tahun_analisis=2019, top_n=5):
    """Menampilkan donut chart proporsi penyebab kematian (Top N) di satu negara."""
    fig, ax = plt.subplots(figsize=(10, 8))
    _plot_proporsi_penyakit_negara(df, ax, negara, tahun_analisis, top_n)
    plt.tight_layout()
    plt.show()