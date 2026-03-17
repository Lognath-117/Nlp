import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

s1="Please turn on the light because the room is dark."
s2="This bag is very light, so it is easy to carry."
word="light"
t1=word_tokenize(s1)
t2=word_tokenize(s2)
sense1=lesk(t1,word)
sense2=lesk(t2,word)
print("Word:",word)
print("Sentence1:",s1)
print("Definition of Sense1:",sense1.definition())
print("Sentence2:",s2)
print("Prediction Sense2:",sense2)
print("Definition of Sense2:",sense2.definition())
