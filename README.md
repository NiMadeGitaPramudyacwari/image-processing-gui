# Image Processing GUI

# GUI berbasis Python menggunakan Streamlit

# Nama Kelompok: 
1. Ni Made Gita Pramudyacwari (250030730)
2. Ni Nyoman Januar Ari Setiawati (230030249)
   
Deskripsi:
- Point Operation yang dibuat : Brightness, Contrast, Gamma Value (γ), Grayscale, Binary, Negative/Inversion
- Point Operation Thresholding   : Konversi Grayscale dan Binary Thresholding (T = 128 dan T = 255)
- Filter Convolution yang dibuat : Blur, Sharpen, Edge Detection, Embossing, Custom Convolution

# Menjalankan Program
- Buka repository GitHub di browser
- Klik tombol Code
- Pilih Download ZIP
- Extract ZIP ke folder (misal: Documents)
- Struktur folder setelah extract untuk mejalankan aplikasi GUI Python menggunakan Streamlit:
```bash
image-processing-gui-python/
├── app.py
├── requirements.txt
└── README.md
```
# Setelah itu bisa langsung lanjut ke:
```bash
pip install -r requirements.txt
streamlit run app.py
```

# Menjalankan Hasil Output Program Image Negative/Inversion GUI
- Setelah aplikasi berjalan, halaman GUI Streamlit akan ditampilkan pada browser.
- Unggah file gambar dengan format JPG, JPEG, atau PNG.
- Citra input akan ditampilkan pada sisi kiri layar (Image Before).
- Pilih jenis Point Operation dan Filter (Convolution) melalui menu sidebar :
  - Point Operation:
    - Brightness
    - Contrast
    - Gamma Value (γ)
      
  - Choose Operation :
    - None
    - Grayscale
    - Binary
    - Negative/Inversion
  - Choose Threshold Value
    - 128
    - 255
      
  - Filter (Convolution)
    - Blur
    - Sharpen
    - Edge Detection
    - Embbosing
    - Custom Convolution
    
- Hasil pengolahan citra akan langsung ditampilkan pada sisi kanan layar sebagai output image (Image After).
- Pengguna dapat mengganti jenis operasi untuk melihat perbedaan hasil gambar.

