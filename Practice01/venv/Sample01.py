import nltk

sentence = "At eight o'clock on Thursday morning... Arthur didn't feel very good."

# doing tokenization
tokens = nltk.word_tokenize(sentence)
print(tokens)

# taging sentense (for tags visit: https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/)
tagged = nltk.pos_tag(tokens)
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)
print(entities)

# from nltk.corpus import treebank
# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()