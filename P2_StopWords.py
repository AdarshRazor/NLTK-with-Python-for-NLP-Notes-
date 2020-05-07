from nltk.corpus import stopwords #helps seperating the stop words
from nltk.tokenize import word_tokenize, sent_tokenize #help in tokenizing the the words 

example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english")) #making a set which import the english language.

words=word_tokenize(example_sentence) #tokenized by words

filtered_sentence=[]

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

#Same thing but in one line
#filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)

