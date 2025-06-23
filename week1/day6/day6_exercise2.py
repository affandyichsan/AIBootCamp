def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
            
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("item in the files:")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!")

fruits = {"Apple", "Bananas", "Chery", "datwWWes"}
write_item_to_file("fruit.txt", fruits)
read_items_from_file("items.txt")
            