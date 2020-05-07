#process of grouping the broken down informatio to get the meaning what it is saying.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer #unsupervised [we can re train]

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer= PunktSentenceTokenizer(train_text) #training the text

tokenized  = custom_sent_tokenizer.tokenize(sample_text) #after training we use it to different data

#Give the result about who all are verbs, adjective and all the things.

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged  = nltk.pos_tag(words)
            #print(tagged)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{""" 
            
            #chinking is to excluding the things we don't required instead of selecting all by excepting few.

            chunkParser = nltk.RegexpParser(chunkGram)
            chucked = chunkParser.parse(tagged)

            #chucked.draw()
            print(chucked)





        
    except Exception as e:
            print(str(e))

process_content()