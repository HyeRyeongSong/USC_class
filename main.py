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
    # The “for row in csv_reader:” makes the code iterate over all data in the csv file
    for row in csv_reader:
        # Only the first row in the CSV file is the header information
        # so we exclude the first row and start printing from the second row
        if line_count == 0:
            line_count = line_count + 1

        # Only the text will be printed because we called “row[1]” and we do not need the ID information
        else:
            txt = row[1]
            print (txt)


