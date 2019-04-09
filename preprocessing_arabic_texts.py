#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nltk
from nltk.stem.isri import ISRIStemmer
import re

# loading stemmer for arabic
st = ISRIStemmer()
# asking an arabic text from user
try:
    while True:
        print("Enter an arabic text: ")
        # getting the text entered by user
        text=input()
        # message if user dose not enter a text
        if text=="":
            print("You did not enter your text !")           
        else:
            #tokenising arabic text
            tokens = nltk.word_tokenize(text)
            # stemming arabic text
            tok_stem=[st.stem(t) for t in tokens]
            text_tok_stem=' '.join(tok_stem)
            print("your text is preprocessed: ")
            print(text_tok_stem)
except KeyboardInterrupt:
    print ("  End of the program")
