"""
Latihan 2: Validasi Daftar Nilai
Program untuk menghitung rata-rata nilai mahasiswa dengan validasi data
Menggunakan try-except dalam loop untuk melewati data tidak valid
"""

def percobaan():
    """
    Fungsi untuk validasi dan menghitung rata-rata dari list nilai
    """
    print("\n" + "="*50)
    print("VALIDASI DAFTAR NILAI MAHASISWA")
    print("="*50)
    
    # Data nilai mahasiswa yang berisi angka dan string
    nilai = [80, 90, 'A', 70, 100, 'B']
    
    print(f"\nData nilai mentah: {nilai}")
    print("\nProses validasi:")
    print("-"*50)
    
    # Inisialisasi variable
    total_nilai = 0
    jumlah_data_valid = 0
    data_tidak_valid = []
    
    # Iterasi dengan try-except untuk menangani data tidak valid
    for idx, data in enumerate(nilai):
        try:
            # Coba konversi ke float (untuk validasi angka)
            nilai_numerik = float(data)
            total_nilai += nilai_numerik
            jumlah_data_valid += 1
            print(f"✓ Index {idx}: {data} -> Valid (ditambahkan)")
        
        except ValueError:
            # Data bukan angka, catat sebagai tidak valid dan lanjut
            data_tidak_valid.append(data)
            print(f"✗ Index {idx}: '{data}' -> Tidak valid (dilewati)")
    
    # Hitung rata-rata
    print("\n" + "-"*50)
    print(f"\nJumlah data valid: {jumlah_data_valid}")
    print(f"Data tidak valid (dilewati): {data_tidak_valid}")
    
    if jumlah_data_valid > 0:
        rata_rata = total_nilai / jumlah_data_valid
        print(f"\nTotal nilai (data valid): {total_nilai}")
        print(f"Rata-rata nilai: {rata_rata:.2f}")
    else:
        print("\nTidak ada data valid untuk dihitung rata-ratanya!")
    
    print("="*50)


def main():
    """
    Fungsi utama untuk menjalankan program
    """
    percobaan()
    
    # Opsi untuk menjalankan lagi
    while True:
        ulang = input("\nIngin menjalankan program lagi? (ya/tidak): ").lower().strip()
        if ulang in ['ya', 'yes', 'y']:
            percobaan()
        else:
            print("\nTerima kasih telah menggunakan program validasi nilai!\n")
            break


if __name__ == '__main__':
    main()
