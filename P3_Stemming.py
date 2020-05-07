#stemming is the processing of reducing it to their base form.

from nltk.stem import PorterStemmer #we can use many different stem techniques
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["Python","Pythoner","Pythoning","Pythoned"]
#Python - programming language
#Pythoner - Someone who pythons 
#Pythoninh - Someone who is doing python programming
#Pythoned - After completing the question is pythoned

for w in example_words:
    print(ps.stem(w))

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned prroly at least once."

words = word_tokenize(new_text)

for x in words:
    print(ps.stem(x))