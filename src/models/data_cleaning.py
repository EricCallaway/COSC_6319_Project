from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
import pickle


def get_file(file):
    data_clean(file)

def data_clean(data):
    file_data = open(data, 'rt')
    text = file_data.read()
    file_data.close()
    # Tokenize text into words
    tokens = sent_tokenize(text)
    
    sentences = []
    for sentence in tokens:
        temp = str(clean_sentence(sentence))
        sent = re.sub(r"[\([{})',\]]", "", temp)
        sentences.append(sent)
    print(sentences[:20])
    print("*"*50)
    for i in range(20):
        print(sentences[i])
    print("-"*100)
    # for sentence in sentences:
    #     vectorize_sentence(sentence)
    vectorize_sentence(sentences)
    # df = pd.DataFrame(list_of_sents.toarray(), columns= cv.get_feature_names)
    # print(df)




# Takes in sentence and cleans them one by one.
def clean_sentence(sentence):
    tokens = word_tokenize(sentence)
    tokens = [s.lower() for s in tokens]
    words = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return words

def vectorize_sentence(sentences):
    cv = CountVectorizer(stop_words='english')
    doc_term_mat = cv.fit(sentences)
    print(doc_term_mat.vocabulary_)
    print('-'*50)
    print(doc_term_mat.get_feature_names_out())
    print('-'*50)
    doc_term_mat = cv.transform(sentences)
    print(doc_term_mat.shape)
    print('-'*50)
    print(doc_term_mat.toarray())
    print('-'*50)
    df = pd.DataFrame(doc_term_mat.toarray(), columns = cv.get_feature_names_out())
    print(df.head(10))
    # Pickling the document term matrix data frame
    df.to_pickle('df.pkl')
    # Pickling the clean data
    # sentences.to_pickle('clean_data.pkl') # Not working, figure out how to pickle the list of clean data (not required)
    # Pickling the count vectorizer object
    pickle.dump(cv, open('cv.pkl', 'wb'))
    return doc_term_mat



    


