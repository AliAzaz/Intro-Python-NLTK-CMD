import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# targeting english language stopwords
stop_words = set(stopwords.words('english'))

txt = "Sukanya, Rajib and Naba are my good friends. " \
      "Sukanya is getting married next year. " \
      "Marriage is a big step in one’s life." \
      "It is both exciting and frightening. " \
      "But friendship is a sacred bond between people." \
      "It is a special kind of love between us. " \
      "Many of you must have tried searching for a friend " \
      "but never found the right one."

# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module
# https://stackoverflow.com/a/35279885
tokenized = sent_tokenize(txt)

for i in tokenized:
    print("\nSentense", i, sep="---")
    # tokenize
    tokens = nltk.word_tokenize(i)
    print("tokens:", tokens)

    # stopwords
    wordsList = []
    for j in tokens:
        if j not in stop_words:
            wordsList.append(j)

    print("wordsLst:", wordsList)

    # tagging
    tagged = nltk.pos_tag(wordsList)
    print("tag:", tagged)
