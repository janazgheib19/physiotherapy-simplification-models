# CNN Model
# Install if needed
! pip install tensorflow
import numpy as np
from tensorflow . keras . preprocessing . text import Tokenizer
from tensorflow . keras . preprocessing . sequence import pad_sequences
from tensorflow . keras . models import Sequential
from tensorflow . keras . layers import Embedding , Conv1D ,
GlobalMaxPooling1D , Dense
# Sample dataset ( you can expand it )
complex_sentences = [
" Perform ␣ cervical ␣ rotation ␣ to ␣ the ␣ right ␣ and ␣ left " ,
" Engage ␣ core ␣ musculature ␣ throughout ␣ the ␣ movement " ,
" Perform ␣ shoulder ␣ abduction ␣ up ␣ to ␣ 90 ␣ degrees "
]
4
simple_sentences = [
" turn ␣ your ␣ head ␣ to ␣ both ␣ sides " ,
" tighten ␣ your ␣ stomach " ,
" lift ␣ your ␣ arm ␣ to ␣ shoulder ␣ level "
]
# Tokenization
tokenizer = Tokenizer ()
tokenizer . fit_on_texts ( complex_sentences + simple_sentences )
X = tokenizer . texts_to_sequences ( complex_sentences )
y = tokenizer . texts_to_sequences ( simple_sentences )
max_len = 10
X = pad_sequences (X , maxlen = max_len , padding = ’ post ’)
y = pad_sequences (y , maxlen = max_len , padding = ’ post ’)
vocab_size = len( tokenizer . word_index ) + 1
