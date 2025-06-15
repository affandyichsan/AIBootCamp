import re


def clean_text(text):
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join(text.split())
    return text.lower()

input_text = "Hello apakah hari ini kamu akan belajar bahasa pemrograman python?"
cleanedtext = clean_text(input_text)

print(cleanedtext)
    