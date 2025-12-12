"""
Latihan 1: Kalkulator Aman
Program kalkulator sederhana dengan penanganan eksepsi
"""

def percobaan():
    """
    Fungsi utama untuk menjalankan kalkulator aman
    """
    print("=" * 50)
    print("KALKULATOR AMAN - Latihan Penanganan Eksepsi")
    print("=" * 50)
    
    try:
        # Input angka pertama
        try:
            angka1 = float(input("\nMasukkan angka pertama: "))
        except ValueError:
            raise ValueError("Error: Input harus berupa angka!")
        
        # Input angka kedua
        try:
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            raise ValueError("Error: Input harus berupa angka!")
        
        # Input operator
        operator = input("Masukkan operator (+, -, *, /): ").strip()
        
        # Validasi operator
        if operator not in ['+', '-', '*', '/']:
            raise Exception(f"Error: Operator '{operator}' tidak valid! Gunakan +, -, *, atau /")
        
        # Hitung hasil berdasarkan operator
        if operator == '+':
            hasil = angka1 + angka2
            operasi = f"{angka1} + {angka2}"
        
        elif operator == '-':
            hasil = angka1 - angka2
            operasi = f"{angka1} - {angka2}"
        
        elif operator == '*':
            hasil = angka1 * angka2
            operasi = f"{angka1} * {angka2}"
        
        elif operator == '/':
            # Penanganan pembagian dengan nol
            try:
                hasil = angka1 / angka2
                operasi = f"{angka1} / {angka2}"
            except ZeroDivisionError:
                raise ZeroDivisionError("Error: Tidak bisa membagi dengan nol!")
        
        # Tampilkan hasil
        print("\n" + "=" * 50)
        print(f"Operasi: {operasi}")
        print(f"Hasil: {hasil}")
        print("=" * 50)
    
    except ValueError as e:
        print(f"\n{e}")
        print("Silakan masukkan angka dengan benar.")
    
    except ZeroDivisionError as e:
        print(f"\n{e}")
        print("Pembagi tidak boleh nol.")
    
    except Exception as e:
        print(f"\n{e}")
    
    finally:
        print("\nTerima kasih telah menggunakan Kalkulator Aman!\n")


def main():
    """
    Fungsi untuk menjalankan program dengan loop
    """
    while True:
        percobaan()
        
        # Tanya apakah pengguna ingin mengulangi
        ulang = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").lower().strip()
        if ulang not in ['ya', 'yes', 'y']:
            print("\nProgram selesai. Sampai jumpa!")
            break


if __name__ == '__main__':
    main()
