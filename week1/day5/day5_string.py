pertama = "affandy"
kedua = "ichsan"
gabung = pertama + '-' + kedua
# print(gabung)



text = "python programming"
# print(text[0:6])
# print(text[-11:])

split = text.split()
print(split)

new_sentence = "|".join(split)
print(new_sentence)

textP = "i love python"
update_text = textP.replace("python","php")
print(update_text)



habibi = "         hallo, word    "
cleaned_text = habibi.strip()

print(cleaned_text)