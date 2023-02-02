def replace(word,cut):
    return word.replace(cut,"")

#run -> func -> word_input   -------------  cut_input
print(replace(input("Enter the word: "), input("Enter the cutter: ")))


