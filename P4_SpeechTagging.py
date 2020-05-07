#labeling part of speech
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer #unsupervised [we can re train]

#train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")

train_text = "This is a training text, which consists of manya place name like: India, America and USA. Since Chinahas corona virus in the contry. Donald trump refuse to add them in the meeting."
sample_text = "This is a sample text which goes under the program and test  out that either it working or not. Contry : India , China, USA and Name : Donald Trump, Modi, Varun better etc."

custom_sent_tokenizer= PunktSentenceTokenizer(train_text) #training the text

tokenized  = custom_sent_tokenizer.tokenize(sample_text) #after training we use it to different data

#Give the result about who all are verbs, adjective and all the things.

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged  = nltk.pos_tag(words)
            print(tagged)
        
    except Exception as e:
            print(str(e))

process_content()