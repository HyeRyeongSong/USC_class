## Sentence Preprocessing

# split our Tweet text into words
# use the NLTK(Natural Language Toolkit) library to split our text into words
# use the ‘word_tokenize()’ function provided by the nltk library

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Splitting a sentence into words
# We will have to preprocess our text before we count the words.
example_sentence = "This is a simple sentence."

word_tokens = word_tokenize(example_sentence)

for w in word_tokens:
    print(w)

# Preprocessing 1: Changing the case of charachters into a lower case
# “Happy” and “happy” will be counted as different words when they are the same words.
# We will have to change our text to lowercase because the Python script is case sensitive.
example_sentence = "This is a simple sentence."
final_sentence = example_sentence.lower()

print(final_sentence)

# Preprocessing 2: removing punctuations from a senetence
# remove punctuation from the sentence
# We have to ‘from nltk.tokenize import RegexpTokenizer’
# The ‘RegexpTokenizer()’ function removes the punctutation
example_sentence = "It's a simple sentence."

tokenizer = RegexpTokenizer('r\W+|\w+')
word_tokens = tokenizer.tokenize(example_sentence)

for w in word_tokens:
    print(w)

# Preprocessing 3: removing stopwords from a senetence
# remove stop words from our text
# Stop words usually refers to the most common words in a language that have no significant meaning
# We have to ‘from nltk.corpus import stopwords’

example_sentence = "It's a simple sentence."

stop_words = set(stopwords.words('English'))
tokenizer = RegexpTokenizer('r\W+|\w+')
word_tokens = tokenizer.tokenize(example_sentence)
# checks if any tokens are stop words and filters them
filtered_sentence = [w for w in word_tokens if not w in stop_words]


for w in filtered_sentence:
    print(w)
