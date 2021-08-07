import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



#download nltk
nltk.download()

text_input = "Hello Mr. Smith! How are you doing? The weather seems to be really nice."

print(word_tokenize(text_input))

for i in word_tokenize(text_input):
    print (i)

example_sentence = "I have been riding a car lately since the beginning of last year and it has been traumatizing"

stop_words = set(stopwords.words("english"))

print(stop_words)

words = word_tokenize(example_sentence)
print(words)
filtered_text = []
for i in words:
    if i not in stop_words:
        filtered_text.append(i)
filtered_text

ps = PorterStemmer()

words = word_tokenize(example_sentence)


for i in words:
    print(ps.stem(i))