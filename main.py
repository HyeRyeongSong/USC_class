import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

from collections import OrderedDict
import operator

final_dictionary = {}

with open('GoodDoctorWeek1_clean.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        if line_count == 1:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            txt = row[1]

            final_txt = txt.lower()
            stop_words = ['hawaii', 'paris', 'new_york', 'beijing', 'los_angeles', 'seoul' ]
            tokenizer = RegexpTokenizer('r\W+|\w+')
            word_tokens = tokenizer.tokenize(final_txt)
            filtered_sentence = [w for w in word_tokens if w in stop_words]

            for w in filtered_sentence:
                if w not in final_dictionary:
                    final_dictionary[w] = 1
                else:
                    final_dictionary[w] = final_dictionary[w] + 1

sorted_d = sorted(final_dictionary.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)

with open('wordCount_GD.csv', mode='w', newline = '', encoding='UTF-8') as my_file:
    my_writer = csv.writer(my_file, delimiter=',')

    # write ‘Word’ and ‘Count’ as headers
    my_writer.writerow(['Word', 'Count'])

    # iterate over our collection of tuples and write each tuple in each row
    for key in sorted_d:
        current_Word = str(key[0])
        current_Count = int(key[1])

        my_writer.writerow([current_Word, current_Count])


with open('wordCount_GD.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        line_count = line_count + 1

        if line_count == 1:
            continue;

        word = str(row[0])
        count = int(row[1])

        final_dictionary[word] = count
        print(word + "\t" + str(count))

        if line_count == 21:
            break;

plt.figure(figsize=(20, 3))

plt.title('Frequency of some famous cities')
plt.xlabel('Cities')
plt.ylabel('Frequency')

plt.bar(final_dictionary.keys(), final_dictionary.values(), width=0.3, color='g')

plt.show()

f_dictionary = {}

f_dictionary['dawn'] = 0 # 0 ~ 5
f_dictionary['morning'] = 0 # 6 ~ 11
f_dictionary['afternoon'] = 0 # 12~17
f_dictionary['night'] = 0 # 18~23

with open('GoodDoctorWeek1_clean.csv', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        hour = row[7]

        if line_count == 0:
            line_count = line_count + 1
        else:
            line_count = line_count + 1
            # these lines are blank
            if line_count >= 7587 and line_count <= 7594:
                continue
            hour = int(row[7])
            if hour >= 0 and hour <= 5:
                f_dictionary['dawn'] = f_dictionary['dawn'] + 1
            if hour >= 6 and hour <= 11:
                f_dictionary['morning'] = f_dictionary['morning'] + 1
            if hour >= 12 and hour <= 17 :
                f_dictionary['afternoon'] = f_dictionary['afternoon'] + 1
            if hour >= 18 and hour <= 23:
                f_dictionary['night'] = f_dictionary['night'] + 1

print("# of tweets labeled as dawn: " + str(f_dictionary['dawn']))
print("# of tweets labeled as morning: " + str(f_dictionary['morning']))
print("# of tweets labeled as afternoon: " + str(f_dictionary['afternoon']))
print("# of tweets labeled as night: " + str(f_dictionary['night']))

plt.figure(figsize=(10, 4))
plt.title('Time Distribution of Tweets')
plt.xlabel('time')
plt.ylabel('# of Tweets per time')
plt.bar(f_dictionary.keys(),f_dictionary.values(), width=0.3, color='g')

plt.show()




