sentence = input("Enter a sentence: ")


words = sentence.split()

words_count  = {}
 
for word in words:
    word = word.lower()
    if word in words_count:
        words_count[word]  +=1
    else:
        words_count[word] = 1
        
print(words_count)