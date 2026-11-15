import streamlit as st

st.title("Belajar Ilmu pengetahuan Data Engineer")
st.write(
    "Pengertian dasar mengenai OLTP & OLAP serta perbedaan diantaranya adalah sebagai berikut :" \
    "OLTP adalah singkatang dari Online Transaction Processing yaitu suatu system yang meproses banyak transaksi dan di proses secara realtime/live streaming. contohnya seperti transfer melalui mobile banking sistem perlu mengurangi saldo rekening pengirim sekaligus memperbarui informasi transaksi." \
    "OLAP adalah singkatan dari Online Analytical Processing dimana suatu process data multidimensi yang diproses secara batch/dilakukan secara berkala sesuai dengan waktu yang sudah ditentukan terlebih dahulu.contohnya seperti laporan penjualan bulanan,olap digunakan untuk menganailis data yang sudah ada dan untuk mengambil keputusan." \
    
    "perbedaan antara OLTP dan OLAP " \
    "Tujuan" \
    "OLAP membantu Anda menganalisis data dalam volume besar untuk mendukung pengambilan keputusan." \
    "OLTP membantu Anda mengelola dan memproses transaksi waktu nyata " \
    "Sumber data." \
    "OLAP menggunakan data historis dan agregat dari beberapa sumber." \
    "OLTP menggunakan data waktu nyata dan transaksional dari satu sumber." \
    "Struktur data" \
    "OLAP menggunakan basis data multidimensional (kubus) atau relasional." \
    "OLTP menggunakan basis data relasional." \
    "Model data" \
    "OLAP menggunakan skema bintang, skema kepingan salju, atau model analitik lainnya." \
    "OLTP menggunakan model yang dinormalisasi atau didenormalisasi." \
    "Volume data" \
    "OLAP memiliki persyaratan penyimpanan yang besar. Misalnya, terabita (TB) dan petabita (PB)." \
    "OLTP memiliki persyaratan penyimpanan yang relatif lebih kecil. Misalnya, gigabita (GB)." \
    "Waktu respons" \
    "OLAP memiliki waktu respons yang lebih lama, biasanya dalam detik atau menit." \
    "OLTP memiliki waktu respons yang lebih pendek, biasanya dalam milidetik" \
    "Contoh penerapan" \
    "OLAP baik digunakan untuk menganalisis tren, memprediksi perilaku pelanggan, dan mengidentifikasi profitabilitas." \
    "OLTP baik digunakan untuk memproses pembayaran, manajemen data pelanggan, dan pemrosesan pesanan."
)
