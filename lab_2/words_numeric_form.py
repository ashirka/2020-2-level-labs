import re


def make_words_numeric(path_to_file):
    words_dict = {}
    word_number = 0
    with open(path_to_file, encoding='utf-8') as data_file:
        for line in data_file.readlines():
            tokenized_line = re.sub('[^a-z \n]', '', line.lower()).split()
            for token in tokenized_line:
                if token not in words_dict:
                    words_dict[token] = word_number
                    word_number += 1
    return words_dict


words_numeric_text = make_words_numeric('data.txt')
words_numeric_second_text = make_words_numeric('data_2.txt')
words_numeric_text.update(words_numeric_second_text)

with open('numeric_words.csv', 'w', encoding='utf-8') as file_dict:
    for key in words_numeric_text.keys():
        file_dict.write(f"{key},{words_numeric_text[key]}\n")



