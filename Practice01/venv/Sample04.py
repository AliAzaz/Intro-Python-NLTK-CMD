import nltk, io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# targeting english language stopwords
stop_words = set(stopwords.words('english'))

# opening file
root_file = open("../sample.txt")
# Use this to read file content as a stream:
line = root_file.read()

tokenized = sent_tokenize(line)
minetxt = []
for item in tokenized:
    tokens = nltk.word_tokenize(item)
    stopwordp_rm = [w for w in tokens if w not in stop_words]
    minetxt.append(stopwordp_rm)

print(minetxt)
