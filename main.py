# read “csv” files using the “csv” package
import csv
# perform sentiment analysis using the “TextBlob” package
from textblob import TextBlob

# use the “open()” function to open a specific file
# include the “encoding=‘UTF-8’“ to read special characters
with open('Data.csv', encoding="UTF-8") as csv_file:
    # use the “csv.reader()” because we are reading a CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # use a Integer variable “line_count” to keep track of whether the data is a header or not
    line_count = 0
    # make a total_sentiment variable so that we can add on all the sentiment values obtained
    total_sentiment = 0
    # The “for row in csv_reader:” makes the code iterate over all data in the csv file
    for row in csv_reader:
        # Only the first row in the CSV file is the header information
        # so we exclude the first row and start printing from the second row
        if line_count == 0:
            line_count = line_count + 1

        # Only the text will be printed because we called “row[1]” and we do not need the ID information
        else:
            txt = row[1]
            ## Now we know how to get the specific Text data from each row of the CSV file

            # We will have to perform sentiment analysis on each of the Texts using “TextBlob(txt).polarity”
            # which will give you a float value between -1 and +1.
            sentiment = TextBlob(txt).polarity
            # add on the sentiment values so that we can later get the average sentiment of all 100 Texts
            total_sentiment = total_sentiment + sentiment
            line_count = line_count + 1

    print("FINAL!")
    # divide the “total_sentiment” by “line_count-1”
    # because that will be how many Text data we iterated through
    # (We have to minus 1 because we have to exclude the header count)
    print (total_sentiment / (line_count - 1))
