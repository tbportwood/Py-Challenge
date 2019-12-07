txtpath = 'test.txt'
import re
with open(txtpath, "r") as text:
    
    #convert paragraph to string
    paragraph = text.read()
    paragraph = re.split("(?<=[.!?]) +", paragraph)
    
    print(sentences)
    sentence_count = 0
    word_count = 0
    average_letter_count = 0
    average_sentence_length = 0
    letters = 0
    
    for sentence in paragraph:
        sentence_count = sentence_count + 1
        temp_sentence = re.split("(?<=[,\- ])", sentence)
        final_sentence = []
        for word in temp_sentence:
            temp_word = str(word)
            temp_word = temp_word.replace(",", "")
            temp_word = temp_word.replace(".", "")
            temp_word = temp_word.replace("'", "")
            temp_word = temp_word.replace(" ", "")
            temp_word = temp_word.replace('“', '')
            temp_word = temp_word.replace('”', '')
            temp_word = temp_word.replace("-", "")
            if temp_word != '': 
                print(temp_word)
                final_sentence.append(temp_word)
                word_count = word_count + 1
                letters = letters + len(temp_word)

    average_letter_count = letters / word_count
    average_sentence_length = word_count / sentence_count
    
    print(round(average_letter_count, 2))
    print(average_sentence_length)
    print(word_count)
    print(sentence_count)