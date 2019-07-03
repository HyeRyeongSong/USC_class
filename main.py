import csv
import matplotlib.pyplot as plt

## Visualize Word Count

# Reading CSV File into a dictionary
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

# Plot Word Count
plt.figure(figsize=(15, 3))

plt.title('Frequency of Most Frequent Words')
plt.xlabel('Most Frequent Words')
plt.ylabel('Frequency')

plt.bar(final_dictionary.keys(), final_dictionary.values(), width=0.3, color='g')

plt.show()