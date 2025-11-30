#!/bin/bash

echo "=========================================="
echo "🛡️  TELKOMSEL AUTOMATION INSTALLER"
echo "=========================================="

# Update package
echo "📦 Update package Termux..."
pkg update -y && pkg upgrade -y

# Install dependencies
echo "📦 Install dependencies..."
pkg install -y python git openssl-tool

# Install Python packages
echo "📦 Install Python packages..."
pip install selenium requests beautifulsoup4

# Download Chrome Driver untuk Termux
echo "📦 Setup Chrome Driver..."
pkg install -y wget unzip

# Download chromedriver (versi stable)
echo "📦 Downloading Chrome Driver..."
wget https://storage.googleapis.com/chrome-for-testing-public/120.0.6099.109/linux64/chromedriver-linux64.zip

# Extract chromedriver
unzip chromedriver-linux64.zip
mv chrome-linux64/chromedriver /data/data/com.termux/files/usr/bin/
chmod +x /data/data/com.termux/files/usr/bin/chromedriver

# Clean up
rm -rf chromedriver-linux64.zip chrome-linux64

# Clone repository
echo "📦 Download script dari GitHub..."
git clone https://github.com/sukronwae85-design/tembakilpedtsel.git

# Masuk ke directory
cd tembakilpedtsel

# Beri permission
chmod +x main.py install_termux.sh

echo ""
echo "=========================================="
echo "🎉 INSTALASI SELESAI!"
echo "=========================================="
echo ""
echo "🚀 Cara menjalankan:"
echo "   cd tembakilpedtsel"
echo "   python main.py"
echo ""
echo "📝 Fitur:"
echo "   1. Login sekali (session 60 hari)"
echo "   2. Lihat nomor terdaftar"
echo "   3. Beli paket internet"
echo "   4. Bersihkan session expired"
echo ""
echo "⚠️  Pastikan:"
echo "   - Koneksi internet stabil"
echo "   - Storage permission diberikan"
echo "   - Nomor Telkomsel aktif"
echo "=========================================="