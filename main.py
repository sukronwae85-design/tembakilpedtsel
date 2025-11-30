from auth_manager import AuthManager
from package_buyer import PackageBuyer
from utils import show_registered_numbers, validate_phone_number, cleanup_expired_sessions
from config import PACKAGES
import os

def show_main_menu():
    print("\n" + "="*50)
    print("🛡️  TELKOMSEL AUTOMATION TOOL")
    print("="*50)
    print("1. 📱 Login Sekali (Session 60 hari)")
    print("2. 📋 Lihat Nomor Terdaftar")
    print("3. 🛒 Beli Paket")
    print("4. 🧹 Bersihkan Session Expired")
    print("5. 🚪 Keluar")
    print("="*50)

def show_package_menu():
    print("\n📦 PILIH PAKET INTERNET:")
    print("1. 22 GB - 7 Hari - Rp 50,000")
    print("2. 11 GB - 7 Hari - Rp 30,000") 
    print("3. 5 GB - 7 Hari - Rp 20,000")
    print("4. 1 GB - 1 Hari - Rp 10,000")
    print("5. Kembali ke Menu Utama")
    print("-" * 30)

def main():
    auth_manager = AuthManager()
    package_buyer = PackageBuyer()
    
    # Auto cleanup expired sessions saat start
    cleanup_expired_sessions()
    
    while True:
        show_main_menu()
        choice = input("Pilih menu (1-5): ").strip()
        
        if choice == '1':
            # Login dengan OTP
            print("\n🔐 LOGIN DENGAN OTP")
            print("Session akan valid selama 60 hari")
            phone = input("Masukkan nomor telepon: ").strip()
            validated_phone = validate_phone_number(phone)
            
            if not validated_phone:
                print("❌ Format nomor tidak valid. Gunakan format: 08123456789")
                continue
            
            if auth_manager.login_with_otp(validated_phone):
                print("✅ Login berhasil! Sekarang bisa langsung beli paket.")
        
        elif choice == '2':
            # Lihat nomor terdaftar
            print("\n📋 DAFTAR NOMOR TERDAFTAR")
            show_registered_numbers()
        
        elif choice == '3':
            # Beli Paket
            print("\n🛒 BELI PAKET INTERNET")
            
            # Tampilkan nomor terdaftar
            registered_numbers = list(auth_manager.users.keys())
            if not registered_numbers:
                print("❌ Belum ada nomor yang terdaftar.")
                print("   Silakan login dulu di menu 1")
                continue
            
            print("\nNomor yang tersedia:")
            for i, phone in enumerate(registered_numbers, 1):
                session_info = auth_manager.get_session_info(phone)
                status = "✅" if session_info and session_info['remaining_days'] > 0 else "❌"
                print(f"{i}. {phone[:4]}****{phone[-3:]} {status}")
            
            # Pilih nomor
            try:
                nomor_pilihan = int(input("\nPilih nomor (angka): ").strip())
                if 1 <= nomor_pilihan <= len(registered_numbers):
                    selected_phone = registered_numbers[nomor_pilihan - 1]
                    
                    # Cek session valid
                    if not auth_manager.is_session_valid(selected_phone):
                        print("❌ Session expired, silakan login ulang")
                        continue
                    
                    # Tampilkan menu paket
                    while True:
                        show_package_menu()
                        package_choice = input("Pilih paket (1-5): ").strip()
                        
                        package_mapping = {
                            '1': '22gb_7days',
                            '2': '11gb_7days', 
                            '3': '5gb_7days',
                            '4': '1gb_1day'
                        }
                        
                        if package_choice in package_mapping:
                            package_key = package_mapping[package_choice]
                            print(f"\n🎯 Memproses pembelian...")
                            print(f"📱 Nomor: {selected_phone[:4]}****{selected_phone[-3:]}")
                            print(f"📦 Paket: {package_buyer.get_package_name(package_key)}")
                            
                            confirm = input("Lanjutkan? (y/n): ").strip().lower()
                            if confirm == 'y':
                                success = package_buyer.buy_package(selected_phone, package_key)
                                if success:
                                    break
                            else:
                                print("❌ Pembelian dibatalkan")
                                break
                        elif package_choice == '5':
                            break
                        else:
                            print("❌ Pilihan tidak valid")
                
                else:
                    print("❌ Pilihan nomor tidak valid")
            
            except ValueError:
                print("❌ Masukkan angka yang valid")
            except Exception as e:
                print(f"❌ Error: {str(e)}")
        
        elif choice == '4':
            # Bersihkan session expired
            print("\n🧹 MEMBERSIHKAN SESSION EXPIRED...")
            cleanup_expired_sessions()
        
        elif choice == '5':
            print("\n👋 Terima kasih telah menggunakan tool ini!")
            break
        
        else:
            print("❌ Pilihan tidak valid")

if __name__ == "__main__":
    main()