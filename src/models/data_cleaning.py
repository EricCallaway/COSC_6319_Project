from pydoc import doc
from traceback import print_exc
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import re
import pickle
import os


def get_file(file, pkl_path):
    single_data_clean(file, pkl_path)

def get_folder(folder_path, pkl_path):
    data = []
    with open(pkl_path, 'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
            except EOFError:
                break
    data_clean(data, pkl_path)

def single_data_clean(data, pkl_path):
    file_data = open(data, 'rt')
    text = file_data.read()
    file_data.close()
    # Tokenize text into words
    tokens = sent_tokenize(text)
    sentences = []
    print('-'*25 +'RAW TEXT' + '-'*25)
    print('')
    print(tokens)
    for sentence in tokens:
        temp = str(clean_sentence(sentence))
        sent = re.sub(r"[\([{})',\]]", "", temp)
        sentences.append(sent)
    print()
    print('-'*100)
    print('AFTER CLEANING')
    print('-'*100)
    print(sentences[:20])
    print('-'*100)
    for i in range(20):
        print(sentences[i])
    print('-'*100)
    print('VECTORIZATION PROCESS')
    print('-'*100)
    data_frame = vectorize_sentence(sentences, pkl_path)
    
    
    return data_frame

def data_clean(data, pkl_path):
    data_frames = []
    sentences = []
    base = os.path.basename(pkl_path)
    clean_data_path = pkl_path.replace(base, 'clean_data.pkl')
    for rec in data:
        rec = os.path.normpath(rec)
        file_data = open(rec, 'rt', encoding='utf8')
        text = file_data.read()
        file_data.close()
        # Tokenize text into words
        tokens = sent_tokenize(text)
        
        for sentence in tokens:
            temp = str(clean_sentence(sentence))
            sent = re.sub(r"[\([{})',\]]", "", temp)
            sentences.append(sent)
            pickle.dump(sent, open(clean_data_path, 'wb'))
        data_frames.append(vectorize_sentence(sentences, pkl_path))
    

    # Splits data into a training set and a testing set for the model.
    x_train, x_test = train_test_split(data_frames, train_size=0.80, random_state=1)
    return data_frames

# Takes in sentence and cleans them one by one.
def clean_sentence(sentence):
    tokens = word_tokenize(sentence)
    tokens = [s.lower() for s in tokens]
    words = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return words

def vectorize_sentence(sentences, pkl_path):
    cv = CountVectorizer(stop_words='english')
    doc_term_mat = cv.fit(sentences)
    print(doc_term_mat.vocabulary_)
    print('-'*100)
    print(doc_term_mat.get_feature_names_out())
    print('-'*100)
    doc_term_mat = cv.transform(sentences)
    print('(SENTENCE #, FEATURE)')
    print(doc_term_mat.shape)
    print('-'*100)
    print('DOCUMENT TERM MATRIX')
    print(doc_term_mat.toarray())
    print('-'*100)
    print('DATA FRAMES')
    print('')
    df = pd.DataFrame(doc_term_mat.toarray(), columns = cv.get_feature_names_out())
    print(df.head(10))
    # Pickling the document term matrix data frame
    base = os.path.basename(pkl_path)
    df_path = pkl_path.replace(base, 'df.pkl')
    df.to_pickle(df_path)
    # Pickling the count vectorizer object
    cv_path = pkl_path.replace(base, 'cv.pkl')
    pickle.dump(cv, open(cv_path, 'wb'))
    return df



    


