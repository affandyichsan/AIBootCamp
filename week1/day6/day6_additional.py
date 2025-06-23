
# # Buat program yang menghitung jumlah kemunculan sebuah kata dalam teks.
# # Ini seperti mesin pencari. Buat file berisi banyak teks, lalu cari kata tertentu dan lihat berapa kali kata itu muncul.

# def write_item_to_file(filename, fileitems):
#     with open(fileitems, "r") as files:
#         items = files.readlines()
#     with open(filename, "w") as file:
#         for item in items:
#             file.write(item)
        
# write_item_to_file("additional.txt","sample.txt")


# Tulis program untuk mencatat pesan log dengan timestamp (cap waktu) ke dalam file.
# Ini sedikit berbeda karena kita belum belajar cara menulis cap waktu. Tapi kamu bisa menggunakan fungsi bawaan Python untuk mendapatkan waktu saat ini.
# Jadi, kamu akan meminta masukan dari pengguna, lalu ketika pengguna mengetik sesuatu di command prompt, simpan itu sebagai pesan log di sebuah file, sertakan juga waktu saat pesan itu diketik. Jalankan perulangan while untuk terus-menerus mencatat pesan ini.

from datetime import datetime

# Nama file log
log_file = "log_pesan.txt"

print("Ketik pesan untuk dicatat (ketik 'keluar' untuk berhenti):")

while True:
    pesan = input("Pesan: ")
    if pesan.lower() == 'keluar':
        print("Program selesai. Semua pesan telah dicatat di file.")
        break

    # Ambil waktu saat ini
    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format pesan log
    log = f"[{waktu_sekarang}] {pesan}\n"

    # Tulis ke file
    with open(log_file, "a") as file:
        file.write(log)
