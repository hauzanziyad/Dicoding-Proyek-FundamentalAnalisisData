# 📊 Proyek Analisis Data: Brazilian E-Commerce (Olist) Public Dataset

Proyek ini merupakan submission akhir untuk kelas **Belajar Fundamental Analisis Data** pada program Dicoding Indonesia. Proyek mencakup seluruh tahapan analisis data secara komprehensif: perumusan pertanyaan bisnis menggunakan kaidah SMART, Data Wrangling (Gathering, Assessing, Cleaning), Exploratory Data Analysis (EDA), Visualisasi Data & Explanatory Analysis, Analisis Lanjutan (RFM Analysis), penarikan kesimpulan & rekomendasi *action items*, serta pembuatan dashboard interaktif menggunakan **Streamlit**.

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

1. **Pertanyaan 1**: *Kategori produk apa saja yang mencatatkan total pendapatan (revenue) tertinggi dan terendah pada platform E-Commerce Olist selama periode 2017 hingga 2018?*
2. **Pertanyaan 2**: *Bagaimana tingkat kepuasan pelanggan berdasarkan skor ulasan (review score), dan bagaimana pengaruh keterlambatan pengiriman terhadap penurunan skor kepuasan pelanggan pada periode 2017-2018?*
3. **Analisis Lanjutan**: *Bagaimana segmentasi pelanggan Olist berdasarkan analisis Recency, Frequency, dan Monetary (RFM) untuk merancang strategi retensi dan penawaran pemasaran yang tepat sasaran?*

---

## ⚙️ Panduan Menjalankan Proyek & Dashboard

### 1. Prasyarat Sistem
Pastikan Python 3.9 atau versi yang lebih baru telah terpasang di komputer Anda.

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
Jalankan perintah berikut di root folder proyek:
```bash
streamlit run dashboard/dashboard.py
```
Aplikasi dashboard akan otomatis terbuka pada peramban web (browser) Anda di alamat `http://localhost:8501`.

---

## 📈 Ringkasan Temuan Utama

1. **Kategori Produk dengan Performa Tertinggi & Terendah**:
   - **Top 5 Revenue**: `health_beauty` (R$ 1.23 Juta), `watches_gifts` (R$ 1.16 Juta), `bed_bath_table` (R$ 1.02 Juta), `sports_leisure` (R$ 952.8 Ribu), dan `computers_accessories` (R$ 888.1 Ribu).
   - **Bottom 5 Revenue**: `security_and_services` (R$ 283.29), `fashion_childrens_clothes` (R$ 519.95), `cds_dvds_musicals` (R$ 730.00), `home_comfort_2` (R$ 760.27), dan `flowers` (R$ 1,110.04).

2. **Dampak Ketepatan Waktu Pengiriman terhadap Kepuasan Pelanggan**:
   - Rata-rata skor ulasan keseluruhan adalah **4.16 / 5.00**.
   - Pesanan yang tiba tepat waktu / lebih cepat mendapatkan rata-rata rating **4.29** (median 5.0).
   - Pesanan yang terlambat anjlok menjadi rata-rata **2.57** (median 2.0). Keterlambatan memicu penurunan rating drastis sebesar **-1.72 poin (-40.2%)**.

3. **Segmentasi Pelanggan (RFM Analysis)**:
   - Sebanyak 97% pelanggan saat ini merupakan *one-time buyer* (Frequency = 1), menunjukkan bahwa platform memiliki tantangan retensi yang tinggi.
   - Segmen *Champions* dan *Loyal Customers* berkontribusi signifikan terhadap nilai belanja, sementara segmen *At Risk* dan *Hibernating* membutuhkan intervensi kampanye re-engagement secara terarah.

---

## 🌐 Tautan Dashboard Streamlit Cloud

Dashboard interaktif yang telah dipublikasikan dapat diakses secara daring melalui tautan berikut:
👉 **[Live Streamlit Dashboard](https://dashboard-hauzanziyadatulkhoir-ds001b6y0726.streamlit.app/)**
*(Tautan ini juga tercantum di dalam berkas `url.txt`).*
