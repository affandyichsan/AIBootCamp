# # read
# with open("sample.txt", "r") as file:
#     content = file.readline()
#     print(content)


# write
with open("sample.txt", "w") as file:
    file.write("test ini uji coba")
    file.writelines("testing write")