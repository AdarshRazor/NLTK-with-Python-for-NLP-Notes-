#Wordnet is a group of English words into set of synonyms called "synsets"

#I learned the NAtural language processing by resources found on internet.
#I learned the NAtural language processing by resources found on net.

#Both sentence are same just the last word is different but that wont change the meaning.

from nltk.corpus import wordnet as wn

print(wn.synsets("internet"))    #gives the synonyms of internet

print(wn.synset("internet.n.01").lemma_names())    #here internet.n.01 explain the things that n=noun and 01 is refered to first synset
                                                   #lemma names means the synonyms of the words

print(wn.synset("internet.n.01").definition())     #this would gives a normal definition of the word

print(wn.synset("internet.n.01").examples())      #this would gives the examples like of sentences

#there many not be any exmples of the words in the database
#lets check out the words who actually have the examples

print(wn.synsets("car"))

print(wn.synset("car.n.01").lemma_names())    #gives the synonames of the words

print(wn.synset("car.n.01").examples())       #gives the examples of the word

#for a certain lemma we can also obtain the synset

print(wn.lemma("internet.n.01.net").synset())  #by this we can obtain the word

#------------------------------------------------------------------------------------

#hyponyms = more specific meaning than of general word.
#spoon general word - cutlery is more specific word

print(wn.synsets("cat"))

#for more specific in terms of cats

print(wn.synsets("cat"))

cat=wn.synset("cat.n.01")
types_cats=cat.hyponyms

print(types_cats)

