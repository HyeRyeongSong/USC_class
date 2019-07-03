import csv
import matplotlib.pyplot as plt

final_dictionary = {}

final_dictionary['positive'] = 0
final_dictionary['neutral'] = 0
final_dictionary['negative'] = 0

with open('nltk_output.txt', mode='r', encoding='UTF-8') as my_file:
    csv_reader = csv.reader(my_file, delimiter='\t')

    for row in csv_reader:
        txt = row[0]
        sentiment = float(row[1])

        if sentiment == 0:
            final_dictionary['neutral'] = final_dictionary['neutral'] + 1

        if sentiment < 0:
            final_dictionary['negative'] = final_dictionary['negative'] + 1

        if sentiment > 0:
            final_dictionary['positive'] = final_dictionary['positive'] + 1

    # we have to convert final_dictionary which is a numeric value to string
    print("# of tweets labeled as positive: " + str(final_dictionary['positive']))
    print("# of tweets labeled as neutral: " + str(final_dictionary['neutral']))
    print("# of tweets labeled as negative: " + str(final_dictionary['negative']))

    plt.figure(figsize=(10, 3))
    plt.title('Sentiment Distribution of Tweets -- NLTK')
    plt.xlabel('Sentiment')
    plt.ylabel('# of Tweets per sentiment')
    plt.bar(final_dictionary.keys(), final_dictionary.values(), width=0.3, color='g')

    plt.show()

    