import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Set page configuration
st.set_page_config(
    page_title="Olist E-Commerce Analytics Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling for cards and charts
st.markdown("""
<style>
    .main-header {
        font-size: 28px;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 4px;
    }
    .sub-header {
        font-size: 15px;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 16px;
        border: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    return df

df_raw = load_data()

# Sidebar: Filter Controls
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=80)
    st.title("Filter Parameter")
    st.write("Silakan atur filter berikut untuk memfilter visualisasi data:")
    
    # Date Range Filter
    min_date = df_raw['order_purchase_timestamp'].min().date()
    max_date = df_raw['order_purchase_timestamp'].max().date()
    
    # Default range to main operational years (2017 - 2018)
    default_start = dt.date(2017, 1, 1)
    default_end = max_date
    
    date_range = st.date_input(
        "Pilih Rentang Tanggal Transaksi:",
        value=(default_start, default_end),
        min_value=min_date,
        max_value=max_date
    )
    
    if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = default_start, default_end
    
    # State Filter
    all_states = sorted(df_raw['customer_state'].dropna().unique())
    selected_states = st.multiselect(
        "Filter Negara Bagian (State):",
        options=all_states,
        default=all_states[:5]  # Top states by default or user choice
    )
    
    if not selected_states:
        selected_states = all_states
        
    st.markdown("---")
    st.markdown("**Dicoding Final Project Submission**")
    st.markdown("Dataset: *Brazilian E-Commerce (Olist)*")

# Apply Filters
filtered_df = df_raw[
    (df_raw['order_purchase_timestamp'].dt.date >= start_date) &
    (df_raw['order_purchase_timestamp'].dt.date <= end_date) &
    (df_raw['customer_state'].isin(selected_states))
]

# Header Section
st.markdown('<div class="main-header">🛍️ Brazilian E-Commerce Performance & Customer Satisfaction Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Menganalisis Kinerja Kategori Produk, Pengaruh Ketepatan Pengiriman terhadap Kepuasan Pelanggan, dan Segmentasi RFM (Olist Dataset)</div>', unsafe_allow_html=True)

# KPI Summary Metrics
col1, col2, col3, col4, col5 = st.columns(5)

total_orders = filtered_df['order_id'].nunique()
total_revenue = filtered_df['price'].sum()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
avg_review = filtered_df['review_score'].mean()
on_time_rate = (filtered_df['delivery_status'] == 'On-Time / Early').mean() * 100 if len(filtered_df) > 0 else 0

with col1:
    st.metric("Total Pesanan", f"{total_orders:,}")
with col2:
    st.metric("Total Pendapatan", f"R$ {total_revenue:,.2f}")
with col3:
    st.metric("Rata-rata Order (AOV)", f"R$ {avg_order_value:,.2f}")
with col4:
    st.metric("Rata-rata Rating", f"{avg_review:.2f} / 5.0")
with col5:
    st.metric("Ketepatan Pengiriman", f"{on_time_rate:.1f}%")

st.markdown("---")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📦 Kinerja Kategori Produk",
    "🚚 Kepuasan & Ketepatan Pengiriman",
    "👥 Segmentasi Pelanggan (RFM)",
    "📍 Demografi Geografis"
])

# ----------------- TAB 1: KINERJA KATEGORI PRODUK -----------------
with tab1:
    st.subheader("Performa Kategori Produk: Pendapatan & Volume Terjual")
    st.write("Analisis ini menjawab pertanyaan mengenai kategori produk yang menghasilkan pendapatan tertinggi (Top Performing) dan terendah (Bottom Performing).")
    
    cat_summary = filtered_df.groupby('product_category_name_english').agg(
        total_revenue=('price', 'sum'),
        total_items=('order_item_id', 'count'),
        avg_price=('price', 'mean')
    ).reset_index()
    
    top5_rev = cat_summary.sort_values(by='total_revenue', ascending=False).head(5)
    bottom5_rev = cat_summary.sort_values(by='total_revenue', ascending=True).head(5)
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        st.markdown("#### 🏆 Top 5 Kategori Produk Berdasarkan Pendapatan")
        fig, ax = plt.subplots(figsize=(8, 5))
        # Highlight top 1 with deep blue, others with lighter shade
        colors = ['#1E3A8A' if i == 0 else '#60A5FA' for i in range(len(top5_rev))]
        bars = ax.barh(top5_rev['product_category_name_english'], top5_rev['total_revenue'], color=colors)
        ax.invert_yaxis()
        ax.set_xlabel("Total Pendapatan (BRL - R$)")
        ax.set_title("5 Kategori Produk dengan Pendapatan Tertinggi", fontsize=12, fontweight='bold', pad=10)
        
        # Add labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width + (top5_rev['total_revenue'].max() * 0.02), bar.get_y() + bar.get_height()/2,
                    f"R$ {width:,.0f}", ha='left', va='center', fontsize=9, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    with col_t2:
        st.markdown("#### ⚠️ Bottom 5 Kategori Produk Berdasarkan Pendapatan")
        fig, ax = plt.subplots(figsize=(8, 5))
        # Highlight lowest with dark red, others with muted red
        colors = ['#991B1B' if i == 0 else '#F87171' for i in range(len(bottom5_rev))]
        bars = ax.barh(bottom5_rev['product_category_name_english'], bottom5_rev['total_revenue'], color=colors)
        ax.invert_yaxis()
        ax.set_xlabel("Total Pendapatan (BRL - R$)")
        ax.set_title("5 Kategori Produk dengan Pendapatan Terendah", fontsize=12, fontweight='bold', pad=10)
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 20, bar.get_y() + bar.get_height()/2,
                    f"R$ {width:,.2f}", ha='left', va='center', fontsize=9, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)

    with st.expander("💡 Insight Bisnis Kategori Produk"):
        st.markdown("""
        - **Kategori Unggulan**: Kategori seperti `health_beauty`, `watches_gifts`, dan `bed_bath_table` secara konsisten menjadi motor penggerak pendapatan utama dengan kontribusi jutaan Real.
        - **Kategori Bawah**: Kategori `security_and_services`, `fashion_childrens_clothes`, dan `cds_dvds_musicals` membukukan penjualan yang sangat rendah, mengindikasikan rendahnya minat beli atau minimnya katalog/seller pada segmen tersebut.
        - **Action Item**: Optimalkan inventaris dan promo berbayar untuk 5 kategori teratas, serta lakukan evaluasi kurasi produk atau renegosiasi kemitraan merchant pada kategori bawah.
        """)

# ----------------- TAB 2: KEPUASAN & KETEPATAN PENGIRIMAN -----------------
with tab2:
    st.subheader("Dampak Ketepatan Waktu Pengiriman terhadap Kepuasan Pelanggan")
    st.write("Analisis ini mengkaji korelasi antara keterlambatan pengiriman (delivery delay) dengan skor kepuasan ulasan (review score).")
    
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        st.markdown("#### 📊 Distribusi Skor Ulasan Pelanggan")
        score_counts = filtered_df.drop_duplicates('order_id')['review_score'].value_counts().sort_index()
        
        fig, ax = plt.subplots(figsize=(7, 4.8))
        palette = ['#EF4444', '#F97316', '#FBBF24', '#34D399', '#059669']
        bars = ax.bar(score_counts.index.astype(str), score_counts.values, color=palette, edgecolor='black', linewidth=0.5)
        ax.set_xlabel("Skor Ulasan (Bintang)")
        ax.set_ylabel("Jumlah Pesanan")
        ax.set_title("Distribusi Rating Pelanggan (1 - 5)", fontsize=12, fontweight='bold', pad=10)
        
        total_rev_orders = score_counts.sum()
        for bar in bars:
            height = bar.get_height()
            pct = (height / total_rev_orders) * 100 if total_rev_orders > 0 else 0
            ax.text(bar.get_x() + bar.get_width()/2, height + (score_counts.max()*0.02),
                    f"{height:,}\n({pct:.1f}%)", ha='center', va='bottom', fontsize=8.5, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    with col_d2:
        st.markdown("#### ⏱️ Rata-rata Skor: Tepat Waktu vs Terlambat")
        delivery_score = filtered_df.drop_duplicates('order_id').groupby('delivery_status')['review_score'].agg(['mean', 'count']).reset_index()
        
        fig, ax = plt.subplots(figsize=(7, 4.8))
        colors_status = ['#EF4444' if status == 'Late' else '#10B981' for status in delivery_score['delivery_status']]
        bars = ax.bar(delivery_score['delivery_status'], delivery_score['mean'], color=colors_status, width=0.45, edgecolor='black', linewidth=0.5)
        ax.set_ylim(0, 5.5)
        ax.set_ylabel("Rata-rata Review Score (1 - 5)")
        ax.set_title("Perbandingan Skor Ulasan Berdasarkan Status Pengiriman", fontsize=12, fontweight='bold', pad=10)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.15,
                    f"{height:.2f} / 5.0", ha='center', va='bottom', fontsize=11, fontweight='bold')
                    
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    with st.expander("💡 Insight Bisnis Pengiriman & Kepuasan Pelanggan"):
        st.markdown("""
        - **Mayoritas Puas**: Secara umum, sekitar 75%+ pelanggan memberikan ulasan positif (bintang 4 dan 5).
        - **Dampak Keterlambatan Sangat Signifikan**: Pesanan yang tiba tepat waktu mendapatkan rata-rata rating **~4.29**, sementara pesanan yang terlambat anjlok menjadi **~2.57** (penurunan sebesar 1.72 poin atau lebih dari 40%).
        - **Action Item**: Mengaudit performa logistik mitra ekspedisi, memperbaiki algoritma estimasi waktu pengiriman (ETA) agar lebih realistis, dan mengimplementasikan sistem peringatan dini/kompensasi jika pesanan berpotensi terlambat.
        """)

# ----------------- TAB 3: RFM ANALYSIS -----------------
with tab3:
    st.subheader("Segmentasi Pelanggan Menggunakan Analisis RFM")
    st.write("Analisis Recency, Frequency, dan Monetary (RFM) mengidentifikasi karakteristik perilaku belanja pelanggan untuk perlakuan pemasaran yang terpersonalisasi.")
    
    # Calculate RFM for filtered dataset
    snapshot_date = filtered_df['order_purchase_timestamp'].max() + dt.timedelta(days=1)
    
    rfm_df = filtered_df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
        'order_id': 'nunique',
        'price': 'sum'
    }).reset_index()
    
    rfm_df.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']
    
    # Define simple segment based on Recency & Monetary
    r_labels = [4, 3, 2, 1]  # Lower recency = better
    m_labels = [1, 2, 3, 4]  # Higher monetary = better
    
    # Using quantiles with duplicate handling
    try:
        rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], q=4, labels=r_labels)
        rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], q=4, labels=m_labels)
    except Exception:
        rfm_df['R_Score'] = 2
        rfm_df['M_Score'] = 2
        
    def categorize_segment(row):
        score = int(row['R_Score']) + int(row['M_Score'])
        if score >= 7:
            return 'Champions'
        elif score >= 5:
            return 'Loyal / High Potential'
        elif score >= 3:
            return 'At Risk'
        else:
            return 'Hibernating / Lost'
            
    rfm_df['Customer_Segment'] = rfm_df.apply(categorize_segment, axis=1)
    
    rfm_col1, rfm_col2, rfm_col3 = st.columns(3)
    with rfm_col1:
        st.metric("Rata-rata Recency", f"{rfm_df['Recency'].mean():.0f} Hari")
    with rfm_col2:
        st.metric("Rata-rata Frekuensi", f"{rfm_df['Frequency'].mean():.2f} Order")
    with rfm_col3:
        st.metric("Rata-rata Pengeluaran (Monetary)", f"R$ {rfm_df['Monetary'].mean():.2f}")
        
    col_rfm1, col_rfm2 = st.columns(2)
    with col_rfm1:
        st.markdown("#### 👥 Distribusi Segmen Pelanggan")
        segment_counts = rfm_df['Customer_Segment'].value_counts()
        fig, ax = plt.subplots(figsize=(7, 4.5))
        seg_colors = ['#10B981', '#3B82F6', '#F59E0B', '#EF4444']
        bars = ax.bar(segment_counts.index, segment_counts.values, color=seg_colors[:len(segment_counts)], edgecolor='black', linewidth=0.5)
        ax.set_ylabel("Jumlah Pelanggan")
        ax.set_title("Proporsi Segmen Pelanggan Berdasarkan RFM Score", fontsize=11, fontweight='bold', pad=10)
        plt.xticks(rotation=15)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + (segment_counts.max()*0.02),
                    f"{height:,}", ha='center', va='bottom', fontsize=9, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    with col_rfm2:
        st.markdown("#### 💰 Kontribusi Pendapatan per Segmen")
        seg_monetary = rfm_df.groupby('Customer_Segment')['Monetary'].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(7, 4.5))
        wedges, texts, autotexts = ax.pie(
            seg_monetary.values, 
            labels=seg_monetary.index, 
            autopct='%1.1f%%',
            startangle=140,
            colors=['#10B981', '#3B82F6', '#F59E0B', '#EF4444'][:len(seg_monetary)],
            wedgeprops=dict(width=0.6, edgecolor='white', linewidth=2)
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(9)
            autotext.set_weight('bold')
        ax.set_title("Proporsi Total Belanja Menurut Segmen", fontsize=11, fontweight='bold', pad=10)
        plt.tight_layout()
        st.pyplot(fig)

    with st.expander("💡 Insight Strategi RFM"):
        st.markdown("""
        - **Karakteristik Transaksi**: Mayoritas pelanggan (>95%) melakukan transaksi sekali (one-time buyer).
        - **Champions & Loyal Customers**: Menghasilkan kontribusi nilai transaksi yang tinggi per kapita. Berikan program loyalitas eksklusif, early access produk baru, dan reward points.
        - **At Risk & Hibernating**: Pelanggan yang sudah lama tidak aktif bertransaksi. Terapkan strategi win-back campaign dengan email terpersonalisasi atau kupon diskon pembelian berikutnya.
        """)

# ----------------- TAB 4: DEMOGRAFI GEOGRAFIS -----------------
with tab4:
    st.subheader("Distribusi Geografis Transaksi & Pelanggan")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown("#### 🗺️ Top 10 Negara Bagian Berdasarkan Jumlah Pesanan")
        state_orders = filtered_df.groupby('customer_state')['order_id'].nunique().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(8, 4.5))
        bars = ax.bar(state_orders.index, state_orders.values, color='#3B82F6', edgecolor='black', linewidth=0.5)
        ax.set_ylabel("Jumlah Pesanan Unik")
        ax.set_title("10 Negara Bagian Teratas Berdasarkan Volume Order", fontsize=11, fontweight='bold', pad=10)
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + (state_orders.max()*0.02),
                    f"{height:,}", ha='center', va='bottom', fontsize=8, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    with col_g2:
        st.markdown("#### 💳 Preferensi Metode Pembayaran")
        payment_dist = filtered_df.drop_duplicates('order_id')['payment_type'].value_counts()
        fig, ax = plt.subplots(figsize=(8, 4.5))
        bars = ax.bar(payment_dist.index.str.replace('_', ' ').str.title(), payment_dist.values, color='#8B5CF6', edgecolor='black', linewidth=0.5)
        ax.set_ylabel("Jumlah Pesanan")
        ax.set_title("Distribusi Metode Pembayaran Utama", fontsize=11, fontweight='bold', pad=10)
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + (payment_dist.max()*0.02),
                    f"{height:,}", ha='center', va='bottom', fontsize=8, fontweight='semibold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig)
        
    st.info("📌 **Catatan Wilayah**: Wilayah São Paulo (SP), Rio de Janeiro (RJ), dan Minas Gerais (MG) merupakan pusat gravitasi e-commerce di Brazil dengan mencakup lebih dari 65% total transaksi.")

# Footer
st.markdown("---")
st.caption("Proyek Analisis Data - Belajar Fundamental Analisis Data | Dicoding Indonesia © 2026")
