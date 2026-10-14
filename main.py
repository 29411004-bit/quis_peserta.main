from peserta import Peserta

jumlah = int(input("Masukkan jumlah peserta: "))

daftar_peserta = []

for i in range(jumlah):
    print(f"\nPeserta ke-{i + 1}")
    nama = input("Nama peserta        : ")
    tugas = float(input("Nilai tugas         : "))
    uts = float(input("Nilai UTS           : "))
    uas = float(input("Nilai UAS           : "))

    peserta = Peserta(nama, tugas, uts, uas)
    daftar_peserta.append(peserta)

print("\n===== HASIL PENILAIAN KURSUS =====")

for peserta in daftar_peserta:
    nilai_akhir = peserta.hitung_nilai_akhir()
    grade = peserta.hitung_grade()
    status = peserta.cek_kelulusan()

    print(f"\nNama        : {peserta.nama}")
    print(f"Nilai Akhir : {nilai_akhir:.2f}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")