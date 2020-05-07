#similar to stemming but end result will be actual word or some form of synonames of the original word. [ different word with same meaning ]

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))

print(lemmatizer.lemmatize("better"))

#sampletext="better"        #RBR
#sample=word_tokenize(sampletext)
#POS=nltk.pos_tag(sample)
#print(POS)

print(lemmatizer.lemmatize("better",pos="a"))