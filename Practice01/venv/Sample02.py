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

# tokenize
tokens = nltk.word_tokenize(txt)
print(tokens)

# stopwords
wordsList = [w for w in tokens if not w in stop_words]
print(wordsList)

# tagging
tagged = nltk.pos_tag(wordsList)
print(tagged)