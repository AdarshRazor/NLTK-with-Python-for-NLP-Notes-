'''
import nltk
nltk.downlaod()

Download all of the things as they are elements we need in the future
'''

from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing - word tokenizers [seperate by words] and sentence tokenizers [seperate by sentences]
#lexicon and xoproras
#corpora - body of text. ex: medical journals, presidemtial speeches, English Language
#lexicon - words and their meaning

#investor-speak and regular english-speak

#investor-speak 'bull' = someone who is positive about the market
#english-speak 'bull' = scary animal you don't want running @ you

example_text = "Hello Mr. Smith, how are you doing today? The weeather is great and python is awsome. The sky is blue and the people around are having fun and seems to be very happyy"

#print(sent_tokenize(example_text))

#print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)