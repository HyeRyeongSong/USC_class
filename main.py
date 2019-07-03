import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from collections import OrderedDict
import operator

# Preprocessing Combined
# Combine all 3 preprocessing steps and tokenizing steps
# Word Count Pre-processing

# make a dictionary called 'final_dictionary'
# A Python dictionary contains key:value pairs
# We will use this dictionary so that the actual word is the key and the count of the word is the value
final_dictionary = {}

with open('Data.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        if line_count == 1:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            txt = row[1]

            # 1. set the text to lowercase
            final_txt = txt.lower()
            stop_words = set(stopwords.words('English'))
            # 2. tokenize the word removing punctuations
            tokenizer = RegexpTokenizer('r\W+|\w+')
            word_tokens = tokenizer.tokenize(final_txt)
            # 3. filter the stop words in our tokens
            filtered_sentence = [w for w in word_tokens if not w in stop_words]

            # Then we will have our final list words that do not have punctuations or stop words
            # check whether a specific word is already in our dictionary or not
            # If it is in our dictionary we increment the count otherwise we add it to our dictionary giving it a count of 1
            # Now our dictionary has words and the count
            for w in filtered_sentence:
                if w not in final_dictionary:
                    final_dictionary[w] = 1
                else:
                    final_dictionary[w] = final_dictionary[w] + 1

# Since we want the most frequent words, we sort the dictionary with ‘reverse=True’ so that our dictionary is sorted in descending order
sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
# ‘sorted_d’ will now be a collection of tuples.
# Each tuple will have word for the first value and count for the second value.
print(sorted_d)

# Saving Word Count to a CSV File
# write our word count results to a csv file.
with open('wordCount.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')

    # write ‘Word’ and ‘Count’ as headers
    my_writer.writerow(['Word', 'Count'])

    # iterate over our collection of tuples and write each tuple in each row
    for key in sorted_d:
        current_Word = str(key[0])
        current_Count = int(key[1])

        my_writer.writerow([current_Word, current_Count])