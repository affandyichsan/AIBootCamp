def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_couns = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            
            print(f"Number of Lines : {line_couns}")
            print(f"Number of words : {word_count}")
    except FileNotFoundError:
        print(f"File{filename} not found!")
        
count_words_and_lines("sample.txt")
        