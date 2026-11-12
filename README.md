# 📊 Proyek Analisis Data: Brazilian E-Commerce (Olist) Public Dataset

- **Nama:** Hauzan Ziyadatul Khoir
- **Email:** hauzanziyadk@gmail.com
- **ID Dicoding:** hauzanziyadk

Proyek ini merupakan submission akhir untuk kelas **Belajar Fundamental Analisis Data** pada program Dicoding Indonesia. Proyek mencakup seluruh tahapan analisis data secara komprehensif: perumusan pertanyaan bisnis menggunakan kaidah SMART, Data Wrangling (Gathering, Assessing, Cleaning), Exploratory Data Analysis (EDA), Visualisasi Data dan Explanatory Analysis, Analisis Lanjutan (RFM Analysis), penarikan kesimpulan dan rekomendasi *action items*, serta pembuatan dashboard interaktif menggunakan **Streamlit**.

---

## 📁 Struktur Direktori Proyek

```text
submission/
├── dashboard/
│   ├── main_data.csv          # Dataset gabungan dan bersih untuk dashboard
│   └── dashboard.py           # Skrip utama aplikasi dashboard Streamlit
├── data/                      # Kumpulan berkas CSV mentah dari dataset Olist
│   ├── olist_customers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   └── product_category_name_translation.csv
├── notebook.ipynb             # Jupyter Notebook lengkap dan telah dieksekusi
├── README.md                  # Dokumentasi proyek dan panduan menjalankan dashboard
├── requirements.txt           # Daftar dependensi library Python
└── url.txt                    # Tautan dashboard yang dideploy di Streamlit Cloud
```

---

## 🎯 Pertanyaan Bisnis (SMART Framework)

1. **Pertanyaan 1**: *Kategori produk apa saja yang mencatatkan total pendapatan (revenue) tertinggi dan terendah pada platform E-Commerce Olist selama periode tahun 2017 hingga 2018?*
2. **Pertanyaan 2**: *Bagaimana tingkat kepuasan pelanggan berdasarkan skor ulasan (review score), dan bagaimana pengaruh keterlambatan pengiriman terhadap penurunan skor kepuasan pelanggan pada periode 2017-2018?*
3. **Analisis Lanjutan**: *Bagaimana segmentasi pelanggan Olist berdasarkan analisis Recency, Frequency, dan Monetary (RFM) untuk merancang strategi retensi dan penawaran pemasaran yang tepat sasaran?*

---

## ⚙️ Panduan Menjalankan Proyek dan Dashboard

### 1. Prasyarat Sistem
Pastikan Python 3.9 sampai dengan 3.11 telah terpasang pada komputer Anda.

### 2. Menyiapkan Virtual Environment

**Pengguna Windows (Command Prompt / PowerShell):**
```bash
# Membuat virtual environment bernama .venv
python -m venv .venv

# Mengaktifkan virtual environment
.\.venv\Scripts\activate
```

**Pengguna macOS / Linux:**
```bash
# Membuat virtual environment bernama .venv
python3 -m venv .venv

# Mengaktifkan virtual environment
source .venv/bin/activate
```

### 3. Menginstal Dependensi
Setelah virtual environment aktif, instal seluruh library yang diperlukan dengan menjalankan:
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Dashboard Streamlit
Jalankan perintah berikut di folder proyek:
```bash
streamlit run dashboard/dashboard.py
```
*(Atau jika berada di dalam folder `dashboard/`, cukup jalankan `streamlit run dashboard.py`).*
Aplikasi dashboard akan otomatis terbuka pada peramban web (browser) Anda di alamat `http://localhost:8501`.

---

## 📈 Ringkasan Temuan Utama

1. **Kategori Produk dengan Performa Tertinggi dan Terendah**:
   - **Top 5 Revenue**: `health_beauty` (R$ 1,229,557.50), `watches_gifts` (R$ 1,163,465.91), `bed_bath_table` (R$ 1,022,955.77), `sports_leisure` (R$ 952,840.40), dan `computers_accessories` (R$ 888,055.59).
   - **Bottom 5 Revenue**: `security_and_services` (R$ 283.29), `fashion_childrens_clothes` (R$ 519.95), `cds_dvds_musicals` (R$ 730.00), `home_comfort_2` (R$ 760.27), dan `flowers` (R$ 1,110.04).

2. **Dampak Ketepatan Waktu Pengiriman terhadap Kepuasan Pelanggan**:
   - Rata-rata skor ulasan agregat adalah **4.16 / 5.00**, dengan **79.0%** ulasan berada pada kategori positif (bintang 5 sebesar 59.3% dan bintang 4 sebesar 19.7%).
   - Pesanan yang terkirim tepat waktu mendapatkan rata-rata rating **4.30** (dengan 62.5% memberikan rating bintang 5).
   - Pesanan yang mengalami keterlambatan anjlok menjadi rata-rata **2.57** (dengan 46.1% memberikan rating bintang 1). Terjadi penurunan signifikan sebesar **-1.73 poin (-40.2%)**.

3. **Segmentasi Pelanggan (RFM Analysis)**:
   - Sebanyak 97.0% pelanggan (90,557 dari 93,358 pengguna unik) merupakan pembeli satu kali (*single-order buyer*).
   - Segmen *Champions* (18.9%) dan *Loyal / High Potential* (43.6%) mencakup **62.5%** dari total pelanggan serta menyumbang lebih dari 72% dari total pengeluaran belanja pada platform.

---

## 🌐 Tautan Dashboard Streamlit Cloud

Dashboard interaktif yang telah dipublikasikan dapat diakses secara daring melalui tautan berikut:
👉 **[Live Streamlit Dashboard](https://dashboard-hauzanziyadatulkhoir-ds001b6y0726.streamlit.app/)**
*(Tautan ini juga tercantum di dalam berkas `url.txt`).*
