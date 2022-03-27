import re
from spacy.lang.en.stop_words import STOP_WORDS

def clean_body(text):
    newText = text.lower()
    newText = re.sub('[^\w\s\d\.]','',newText)
    newText = ' '.join(newText.split())
    tokens = [w for w in newText.split() if not w in STOP_WORDS]
    long_words=[]
    for i in tokens:
        if len(i)>=3:
            long_words.append(i)   
    return (" ".join(long_words)).strip()

new_text = cleaned_body(input_text)

#-----------------------------------------------------------------------------------------------
#coverting text to string
new_text = new_text.progress_apply(lambda x: str(x))
#splitting data into train and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(new_text, new_text_summary,test_size=0.2,random_state=0,shuffle=True)
#-----------------------------------------------------------------------------------------------

# Tokenizing the text"
from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences
x_tok = Tokenizer()
x_tok.fit_on_texts(list(x_train))

# Converting text to number sequences
x_train = x_tok.texts_to_sequences(x_train) 
x_test = x_tok.texts_to_sequences(x_test)

# Padding zero upto maximum length
x_train = pad_sequences(x_train,  maxlen=max_len_body, padding='post') 
x_test = pad_sequences(x_test, maxlen=max_len_body, padding='post')

# Total number of words
x_vocab_size = len(x_tok.word_index) +1

