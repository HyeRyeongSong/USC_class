# read “csv” files using the “csv” package
import csv
# perform sentiment analysis using the “TextBlob” package
from textblob import TextBlob

# use the “open()” function to open a specific file
# include the “encoding=‘UTF-8’ “ to read special characters
with open('Data.csv', encoding="UTF-8") as csv_file:
    # use the “csv.reader()” because we are reading a CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # The “for row in csv_reader:” makes the code iterate over all data in the csv file
    # Each row has a Data Type “List”
    # Each list will have 2 elements since we have 2 values(ID and Text) in the CSV file
    # Row[0] will give the ID and Row[1] will give the Text.
    for row in csv_reader:
        print (row[0])
        print (row[1])


