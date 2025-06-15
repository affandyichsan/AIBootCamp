import re


text = "kontak aku at 08956-0517-3570"
digit = re.findall(r"\d+", text)


updated_text = re.sub(r"\d","x", text)

print(digit)
print(updated_text)