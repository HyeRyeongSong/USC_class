import csv
import matplotlib.pyplot as plt

final_dictionary = {}

with open('wordCount.csv', mode='r', encoding='UTF-8') as my_file:
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