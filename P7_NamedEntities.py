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
            
            namedEnt = nltk.ne_chunk(tagged, binary=True) #As we put the binary=TRUE It will consider the Multiple 
            namedEnt = nltk.ne_chunk(tagged)              # named entities as in groups, not each one seperate.

            namedEnt.draw()
            #print(namedEnt)


            """
            NE Type Examples
            ORGANIZATION      Georgia-Pacific Corp., WHO
            PERSON     Eddy Bonte, President Obama
            LOCATION    Murray River, Mount Everest
            DATE    June, 2008-06-29
            TIME     two fifty a m,  1:30 p.m.
            MONEY    175 million Canadian Dollars,   GBP 10.40
            PERCENT      twenty pct,  18.75%
            GPE    South East Asia,   Midlothian
            """



        
    except Exception as e:
            print(str(e))

process_content()