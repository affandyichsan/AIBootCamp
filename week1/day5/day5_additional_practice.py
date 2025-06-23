# write a program to count the number of vowels in a string
# create a program to find and replace all email address in a text using regex
# write a program to reverse the words in sentence (not the letters)

# # write a program to count the number of vowels in a string
# def hitung_vokal(text):
#     vokal = 'aiueoAIUEO'
#     jumlah = sum(1 for huruf in vokal if huruf in text)
#     return jumlah

# teks_input = input("Masukkan sebuah kalimat atau kata: ")
# jumlah_vokal = hitung_vokal(teks_input)

# # Tampilkan hasil
# print(f"Jumlah huruf vokal dalam teks tersebut adalah: {jumlah_vokal}")



# # create a program to find and replace all email address in a text using regex
# import re

# def ganti_email(teks):
#     pola_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
#     hasil = re.sub(pola_email, 'affandyichsan5@gmail.com', teks)
#     return hasil

# # Contoh penggunaan
# teks_input = """
# Halo, silakan hubungi saya di contoh.com atau admin123@domain.co.id untuk informasi lebih lanjut.
# """
# hasil_output = ganti_email(teks_input)
# print(hasil_output)



def balik_kata(kalimat):
    kata = kalimat.split()        # Memisahkan kata berdasarkan spasi
    kata_terbalik = kata[::-1]    # Membalik urutan kata
    return ' '.join(kata_terbalik)

# Input dari pengguna
kalimat_input = input("Masukkan sebuah kalimat: ")

# Proses dan hasil
hasil = balik_kata(kalimat_input)
print("Kalimat setelah dibalik urutan katanya:")
print(hasil)
