# 📚 Jadwal Kuliah - Class Schedule App

Aplikasi web untuk mengelola jadwal kuliah dan tracking tugas mahasiswa dengan UI yang responsif dan user-friendly.

## ✨ Fitur Utama

- 📅 **Jadwal Kuliah**: Tampilan tabel lengkap semua mata kuliah
- 📖 **Detail Mata Kuliah**: Halaman detail lengkap setiap course dengan informasi komprehensif
- ✅ **Task Management**: Tambah dan hapus tugas per mata kuliah
- 💬 **Modal Quick View**: Lihat detail cepat dengan modal dialog
- 📱 **Fully Responsive**: Mendukung semua device (mobile, tablet, desktop)
- 🎨 **Modern UI**: Design dengan gradient, animasi, dan glassmorphism

## 🚀 Deploy ke Replit

### Cara 1: Import dari GitHub (Recommended)

1. Buka [https://replit.com](https://replit.com)
2. Klik **"Create"** atau **"+ Create Repl"**
3. Pilih **"Import from GitHub"**
4. Paste repository URL: `https://github.com/AryaKharr/jadwal_kuliah_arya`
5. Tunggu proses import selesai
6. Klik **"Run"** atau tekan **Ctrl + Enter**
7. Aplikasi akan launching otomatis di tab browser baru

### Cara 2: Manual Upload

1. Clone atau download repository ini
2. Buka [https://replit.com](https://replit.com)
3. Buat Repl baru dengan Python
4. Upload semua file ke Repl
5. Di terminal Replit, jalankan:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

### Cara 3: Gunakan Replit CLI

```bash
# Install Replit CLI
npm install -g @replit/cli

# Login ke Replit
replit auth login

# Deploy
replit create --name jadwal-kuliah --language python
cd jadwal-kuliah
git clone https://github.com/AryaKharr/jadwal_kuliah_arya .
replit secrets set
replit run
```

## 🏃 Run Lokal

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone repository
git clone https://github.com/AryaKharr/jadwal_kuliah_arya.git
cd jadwal_kuliah_arya

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run aplikasi
python app.py
```

Akses di: `http://localhost:5000`

## 📁 Struktur Folder

```
jadwal_kuliah_arya/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku deployment config
├── .replit                     # Replit configuration
├── .replitignore               # Files to ignore on Replit
├── static/
│   └── style.css              # Styling & responsive design
└── templates/
    ├── index.html             # Jadwal & modal view
    └── matkul_detail.html     # Course detail page
```

## 🎯 Fitur Detail

### Halaman Utama (/)
- Tabel jadwal kuliah lengkap
- Quick view modal saat klik row
- Responsive design untuk semua device
- Task management integrasi

### Halaman Detail (/matkul/{id})
- Informasi lengkap mata kuliah
- Deskripsi detail course
- Manajemen tugas lengkap
- Desain modern dengan card layout

### API Routes

```
GET  /                    - Halaman jadwal utama
GET  /matkul/<id>        - Detail page mata kuliah
POST /tambah_tugas       - Tambah tugas
POST /hapus_tugas        - Hapus tugas
```

## 🎨 Design Highlights

- **Gradient Background**: Smooth purple-pink gradient
- **Responsive Typography**: Font scaling dengan CSS clamp()
- **Touch-Friendly**: Min 44px buttons untuk mobile
- **Smooth Animations**: Modal slide-up, hover effects
- **Glassmorphism**: Modern backdrop blur effect
- **Color Scheme**: Purple (#667eea) to Pink (#f093fb)

## 📱 Device Support

- ✅ Mobile phones (320px+)
- ✅ Android devices
- ✅ Tablets (600px+)
- ✅ Laptops (768px+)
- ✅ Desktop (1200px+)
- ✅ Ultra-wide screens (1400px+)

## 🔧 Configuration

Environment variables:
```
PORT=5000              # Default port
FLASK_ENV=production   # Environment mode
```

## 📝 Dependencies

- Flask==3.1.2
- Werkzeug==3.1.5
- Jinja2==3.1.6

## 🤝 Contributing

Feel free untuk contribute atau suggest improvements!

## 📄 License

© 2025 Jadwal Kuliah App. All rights reserved.

---

**Happy Learning! 📚✨**
