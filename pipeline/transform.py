import pandas as pd

# Deklarasi kamus pemetaan nama penyakit
kamus_nama_penyakit = {
    # Penyakit kardiovaskular
    "Cardiovascular Diseases": "Penyakit Jantung & Pembuluh Darah",
    "Ischemic Heart Disease": "Serangan Jantung",
    "Stroke": "Stroke",
    "Hypertensive Heart Disease": "Penyakit Jantung Hipertensi",
    "Atrial Fibrillation And Flutter": "Gangguan Irama Jantung",
    "Peripheral Vascular Disease": "Penyakit Pembuluh Darah Tepi",
    "Endocarditis": "Radang Selaput Jantung",
    "Non-Rheumatic Valvular Heart Disease": "Penyakit Katup Jantung",
    "Aortic Aneurysm": "Aneurisma Aorta",
    "Rheumatic Heart Disease": "Penyakit Jantung Rematik",
    "Cardiomyopathy And Myocarditis": "Radang & Kelemahan Otot Jantung",

    # Kanker / Neoplasma
    "Neoplasms": "Kanker (Semua Jenis)",
    "Tracheal, Bronchus And Lung Cancer": "Kanker Paru-Paru",
    "Colon And Rectum Cancer": "Kanker Usus Besar",
    "Stomach Cancer": "Kanker Lambung",
    "Breast Cancer": "Kanker Payudara",
    "Prostate Cancer": "Kanker Prostat",
    "Liver Cancer": "Kanker Hati",
    "Cervical Cancer": "Kanker Serviks",
    "Esophageal Cancer": "Kanker Kerongkongan",
    "Pancreatic Cancer": "Kanker Pankreas",
    "Ovarian Cancer": "Kanker Indung Telur",
    "Kidney Cancer": "Kanker Ginjal",
    "Bladder Cancer": "Kanker Kandung Kemih",
    "Brain And Central Nervous System Cancer": "Kanker Otak",
    "Leukemia": "Kanker Darah (Leukemia)",
    "Hodgkin Lymphoma": "Limfoma Hodgkin",
    "Non-Hodgkin Lymphoma": "Limfoma Non-Hodgkin",
    "Multiple Myeloma": "Mieloma Multipel",
    "Lip And Oral Cavity Cancer": "Kanker Mulut",
    "Nasopharynx Cancer": "Kanker Nasofaring",
    "Larynx Cancer": "Kanker Laring",
    "Gallbladder And Biliary Tract Cancer": "Kanker Kantung Empedu",
    "Thyroid Cancer": "Kanker Tiroid",
    "Uterine Cancer": "Kanker Rahim",
    "Testicular Cancer": "Kanker Testis",
    "Mesothelioma": "Kanker Selaput Paru (Mesothelioma)",

    # Penyakit pernapasan
    "Chronic Obstructive Pulmonary Disease": "Penyakit Paru Obstruktif Kronis (PPOK)",
    "Lower Respiratory Infections": "Infeksi Saluran Napas Bawah",
    "Chronic Respiratory Diseases": "Penyakit Paru Kronis",
    "Asthma": "Asma",
    "Pneumoconiosis": "Penyakit Paru Akibat Debu",
    "Interstitial Lung Disease And Pulmonary Sarcoidosis": "Penyakit Paru Interstisial",
    "Upper Respiratory Infections": "Infeksi Saluran Napas Atas",

    # Penyakit metabolik & endokrin
    "Diabetes Mellitus": "Diabetes",
    "Nutritional Deficiencies": "Kekurangan Gizi",
    "Protein-Energy Malnutrition": "Kekurangan Protein & Energi",
    "Iron-Deficiency Anaemia": "Anemia Kekurangan Zat Besi",

    # Penyakit saraf & jiwa
    "Alzheimer'S Disease and Other Dementias": "Alzheimer & Demensia",
    "Alzheimer's Disease and Other Dementias": "Alzheimer & Demensia",
    "Parkinson'S Disease": "Parkinson",
    "Parkinson's Disease": "Parkinson",
    "Epilepsy": "Epilepsi",
    "Multiple Sclerosis": "Sklerosis Multipel",
    "Motor Neuron Disease": "Penyakit Neuron Motorik",

    # Penyakit pencernaan
    "Cirrhosis And Other Chronic Liver Diseases": "Sirosis & Penyakit Hati Kronis",
    "Digestive Diseases": "Penyakit Pencernaan",
    "Peptic Ulcer Disease": "Tukak Lambung",
    "Pancreatitis": "Radang Pankreas",
    "Inflammatory Bowel Disease": "Radang Usus Kronis",
    "Gallbladder And Biliary Diseases": "Penyakit Kantung Empedu",

    # Penyakit ginjal
    "Chronic Kidney Disease": "Penyakit Ginjal Kronis",
    "Acute Kidney Injury": "Gagal Ginjal Akut",

    # Penyakit infeksi
    "HIV/AIDS": "HIV/AIDS",
    "Hiv/Aids": "HIV/AIDS",
    "Tuberculosis": "TBC (Tuberkulosis)",
    "Malaria": "Malaria",
    "Hepatitis B": "Hepatitis B",
    "Hepatitis C": "Hepatitis C",
    "Diarrheal Diseases": "Diare",
    "Typhoid And Paratyphoid": "Demam Tifoid",
    "Meningitis": "Radang Selaput Otak",
    "Sepsis": "Sepsis (Infeksi Darah)",
    "Measles": "Campak",

    # Penyakit akibat gaya hidup / cedera
    "Suicide": "Bunuh Diri",
    "Drug Use Disorders": "Gangguan Penggunaan Narkoba",
    "Alcohol Use Disorders": "Gangguan Penggunaan Alkohol",
    "Road Injuries": "Kecelakaan Lalu Lintas",

    # Penyakit otot & tulang
    "Rheumatoid Arthritis": "Artritis Reumatoid",

    # Kelainan darah & imun
    "Hemoglobinopathies And Haemolytic Anaemias": "Kelainan Hemoglobin & Anemia Hemolitik",
    
    # Tambahan untuk variasi kapitalisasi dari dataset
    "Cirrhosis and Other Chronic Liver Diseases": "Sirosis & Penyakit Hati Kronis"
}

def ubah_nama_penyakit(nama_penyakit):
    """Mengubah nama penyakit ilmiah ke nama umum yang lebih mudah dipahami."""
    # .strip() digunakan untuk menghindari kegagalan mapping karena spasi berlebih
    return kamus_nama_penyakit.get(str(nama_penyakit).strip(), nama_penyakit)


def clean_dataset2_column(col):
    if col.startswith("Deaths - "):
        col = col.replace("Deaths - ", "")
        col = col.replace(" - Sex: Both - Age: All Ages (Number)", "")
        # Beberapa dataset2 memiliki variasi Title Case 
        # (seperti Hiv/Aids, namun dicocokkan di dict atau diperbaiki di sini)
        if col == "Hiv/Aids":
            col = "HIV/AIDS"
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

    # ---> Menerapkan mapping nama penyakit ke bentuk umum
    df1_long["Penyakit"] = df1_long["Penyakit"].apply(ubah_nama_penyakit)

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

    # ---> Menerapkan mapping nama penyakit ke bentuk umum
    df2_long["Penyakit"] = df2_long["Penyakit"].apply(ubah_nama_penyakit)

    return df2_long