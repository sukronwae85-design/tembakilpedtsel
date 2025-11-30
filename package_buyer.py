import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from auth_manager import AuthManager
from config import CONFIG, PACKAGES

class PackageBuyer:
    def __init__(self):
        self.auth_manager = AuthManager()
        self.package_info = {
            '1gb_1day': {'name': '1 GB - 1 Hari', 'price': 'Rp 10,000'},
            '5gb_7days': {'name': '5 GB - 7 Hari', 'price': 'Rp 20,000'},
            '11gb_7days': {'name': '11 GB - 7 Hari', 'price': 'Rp 30,000'},
            '22gb_7days': {'name': '22 GB - 7 Hari', 'price': 'Rp 50,000'}
        }
    
    def get_package_name(self, package_key):
        """Dapatkan nama paket lengkap dengan harga"""
        info = self.package_info.get(package_key, {})
        return f"{info.get('name', 'Unknown')} - {info.get('price', 'Unknown')}"
    
    def show_available_packages(self):
        """Tampilkan daftar paket yang tersedia dengan harga"""
        print("\n📦 Daftar Paket Tersedia:")
        for i, (key, url) in enumerate(PACKAGES.items(), 1):
            info = self.package_info.get(key, {})
            print(f"{i}. {info.get('name', 'Unknown')} - {info.get('price', 'Unknown')}")
    
    def buy_package(self, phone_number, package_key):
        """Beli paket berdasarkan package key"""
        if not self.auth_manager.is_session_valid(phone_number):
            print("❌ Session expired, login ulang diperlukan")
            return False
        
        user_data = self.auth_manager.get_user(phone_number)
        package_url = PACKAGES.get(package_key)
        
        if not package_url:
            print("❌ Package tidak ditemukan")
            return False
        
        package_name = self.get_package_name(package_key)
        print(f"🛒 Memproses: {package_name}")
        print(f"📱 Untuk: {phone_number[:4]}****{phone_number[-3]}")
        
        # Setup browser dengan session yang disimpan
        options = webdriver.ChromeOptions()
        if CONFIG['headless']:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        
        try:
            # Load cookies session
            driver.get(CONFIG['base_url'])
            for cookie in user_data['session_data']['cookies']:
                driver.add_cookie(cookie)
            
            # Buka halaman paket
            print("🌐 Membuka halaman paket...")
            driver.get(package_url)
            wait = WebDriverWait(driver, CONFIG['timeout'])
            
            # Tunggu halaman load
            time.sleep(3)
            
            # Cari dan click beli button
            print("🔍 Mencari tombol beli...")
            buy_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Beli') or contains(text(),'BELI')]")
            
            if not buy_buttons:
                print("❌ Tombol beli tidak ditemukan")
                return False
            
            buy_buttons[0].click()
            print("✅ Tombol beli diklik")
            
            # Tunggu konfirmasi
            time.sleep(2)
            
            # Cari tombol konfirmasi
            confirm_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Ya') or contains(text(),'YA') or contains(text(),'Confirm')]")
            
            if confirm_buttons:
                confirm_buttons[0].click()
                print("✅ Konfirmasi pembelian")
            else:
                print("⚠️ Tombol konfirmasi tidak ditemukan, lanjut tanpa konfirmasi")
            
            # Tunggu proses selesai
            print("⏳ Menunggu proses pembelian...")
            time.sleep(5)
            
            print("🎉 Pembelian berhasil diproses!")
            print("💡 Silakan cek di aplikasi MyTelkomsel untuk konfirmasi")
            return True
            
        except Exception as e:
            print(f"❌ Gagal membeli paket: {str(e)}")
            return False
        finally:
            driver.quit()