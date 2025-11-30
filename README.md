# Telkomsel Automation Tool

Tool untuk automasi pembelian paket Telkomsel dengan OTP.

## ⚠️ Disclaimer
- Hanya untuk edukasi dan penggunaan pribadi
- Patuhi Terms of Service Telkomsel
- Gunakan dengan bijak

## 🚀 Instalasi di Termux

### Cara 1: Otomatis (Recommended)
``bash
Download installer
wget https://raw.githubusercontent.com/sukronwae85-design/tembakilpedtsel/main/install_termux.sh

# Beri permission
chmod +x install_termux.sh

# Jalankan installer
./install_termux.sh
ara 2: Manual
bash

# Update package
pkg update && pkg upgrade

# Install dependencies
pkg install python git openssl-tool

# Install Python packages
pip install selenium requests beautifulsoup4

# Download Chrome Driver
pkg install wget unzip
wget https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.109/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
mv chrome-linux64/chromedriver $PREFIX/bin/
chmod +x $PREFIX/bin/chromedriver

# Clone repository
git clone https://github.com/sukronwae85-design/tembakilpedtsel.git
cd tembakilpedtsel

# Jalankan script
python main.py

📱 Cara Penggunaan

    Jalankan script:

bash

cd tembakilpedtsel
python main.py

    Menu Utama:

        1 Login Sekali (Session 60 hari)

        2 Lihat Nomor Terdaftar

        3 Beli Paket

        4 Bersihkan Session Expired

        5 Keluar

    Beli Paket:

        Pilih nomor dari daftar (contoh: 1. 0812****789)

        Pilih paket:

                22 GB - 7 Hari - Rp 50,000

                11 GB - 7 Hari - Rp 30,000

                5 GB - 7 Hari - Rp 20,000

                1 GB - 1 Hari - Rp 10,000

💾 Session Management

    Login sekali, session bertahan 60 hari

    Data disimpan di data/users.json

    Tidak perlu login ulang setiap kali

🛠️ Troubleshooting

Error Chrome Driver:
bash

pkg reinstall openssl-tool
cd $PREFIX/bin && ./chromedriver --version

Error Permission:
bash

termux-setup-storage
chmod +x $PREFIX/bin/chromedriver

Update Script:
bash

cd tembakilpedtsel
git pull

📞 Support

Jika ada masalah, buka issue di GitHub repository.

Note: Tool ini untuk edukasi, gunakan dengan tanggung jawab.
text


## 🎯 **Cara Upload ke GitHub:**

### 1. **File yang perlu diupload:**

tembakilpedtsel/
├── main.py
├── auth_manager.py
├── package_buyer.py
├── utils.py
├── config.py
├── requirements.txt
├── install_termux.sh
└── README.md
text


### 2. **Command untuk upload:**
``bash
# Di local computer/laptop
git add .
git commit -m "Add complete Telkomsel automation tool with Termux support"
git push origin main

📱 Cara Pakai di Termux:
Setelah diupload ke GitHub, pengguna bisa install dengan:
bash

# Di Termux - Cara simpel
wget -O install.sh https://raw.githubusercontent.com/sukronwae85-design/tembakilpedtsel/main/install_termux.sh
chmod +x install.sh
./install.sh

Atau manual:
bash

git clone https://github.com/sukronwae85-design/tembakilpedtsel.git
cd tembakilpedtsel
python main.py
 Fitur Terbaru:

  ✅ Tampilan nomor: 0812****789 (disensor untuk privacy)

   ✅ Daftar paket dengan harga lengkap

  ✅ Menu yang user-friendly

  ✅ Script instalasi otomatis untuk Termux

   ✅ Session 60 hari

  ✅ Auto cleanup session expired

Sekarang script sudah siap untuk diupload ke GitHub dan mudah diinstall di Termux! 🚀
