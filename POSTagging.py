import nltk
nltk.download('averaged_perceptron_tagger')
text= """Natural Language Processing with Python provides a practical introduction to programming for
language processing. Written by the creators of NLTK, it guides the reader through the fundamentals of
writing Python programs, working with corpora, categorizing text, analyzing linguistic structure, and more.
The online version of the book has been been updated for Python 3 and NLTK 3."""
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
