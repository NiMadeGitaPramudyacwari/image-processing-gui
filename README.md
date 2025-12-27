# image-processing-gui

# GUI berbasis Python menggunakan Streamlit

# Nama : Ni Made Gita Pramudyacwari
# NIM  : 250030730

Deskripsi:
- Point Operation yang dibuat : Brightness, Contrast 
- Filter Convolution yang dibuat : Blur, Sharpen, Edge Detection, Embossing Filters

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

# MATLAB GUI App - Image Processing

**Nama** : Ni Nyoman Januar Ari Setiawati
**NIM**  : 230030249

## Deskripsi
Ini adalah aplikasi GUI MATLAB untuk memproses citra.
Fitur aplikasi:
- **Browser Image** (pilih gambar dari komputer)
- **Kategori**: Greyscale, Binary & Negative (Inversion)
- Menampilkan **Original Image** dan **Complement Image**
- Tombol **Reset** untuk mengosongkan tampilan gambar

Aplikasi ini dibuat menggunakan **MATLAB App Designer** dan dapat digunakan untuk analisis citra atau pembelajaran pengolahan citra.

---

## Cara Menjalankan Aplikasi
1. Buka MATLAB.
2. Buka file `app1.mlapp` di MATLAB App Designer.
3. Klik tombol **Browser Image** untuk memilih gambar.
4. Pilih kategori **Greyscale**, **Binary**, atau **Negative (Inversion)**.
5. Lihat hasil di panel **Complement Image**.
6. Klik **Reset** untuk menghapus gambar dan mengembalikan aplikasi ke kondisi awal.

---

## Catatan Teknis
- **Greyscale**: mengubah citra RGB menjadi skala abu-abu.
- **Binary**: mengubah citra menjadi hitam-putih menggunakan threshold.
- **Negative / Inversion**: menggunakan rumus:
  ```matlab
  negative = 255 - img_gray
````
