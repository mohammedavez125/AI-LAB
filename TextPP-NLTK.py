# Import libraries
#import LIbraries
import nltk
nltk.download("stopwords")
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# input
text= """Natural Language Processing with Python provides a practical introduction to programming for
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more.
The online version of the book has been been updated for Python 3 and NLTK 3."""

# paragraph to sentence division
text_to_sentence = sent_tokenize(text)
print("Paragraph to Sentences")
print(text_to_sentence)
print("Number of sentences:",len(text_to_sentence))

# word division
tokenized_word = word_tokenize(text)
print("\nList of Words",tokenized_word)
print("Number of Words",len(tokenized_word))

# Stop word removal
sw_nltk = stopwords.words('english')
print("\nList of all stop words\n:",sw_nltk)
print("Number of stop words",len(sw_nltk))
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)
print("\nOld length: ", len(text))
print("\nNew length: ", len(new_text))
print("\nActual Text\n:",text)
print("\n Text after removing Stop words:\n",new_text)