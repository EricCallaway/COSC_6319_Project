from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import os
import PyPDF2
import docx2txt
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer



ws = Tk()
ws.title('Text Summarization using deep learning')
ws.geometry('400x200') 

def text_lowercase(text):
    return text.lower()

def remove_numbers(text):
    output_text = re.sub(r'\d+', '', text)
    return output_text

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_whitespace(text):
    return  text.strip()

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text

def stem_words(word_tokens):
    stemmer = PorterStemmer()
    stems = [stemmer.stem(word) for word in word_tokens]
    return stems

def lemmatize_word(word_tokens):
    lemmatizer = WordNetLemmatizer()
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    return lemmas

def open_file():
    file_path = askopenfile(mode='r', filetypes=[("PDF Files", "*.pdf"), ("MS Word", "*.docx *.doc"), ("Text File", "*.txt")])
    filename_split = (file_path.name).split(".")
    print(filename_split)
    content = ""
    if file_path is not None:
        if(filename_split[1] == "pdf"):
           f = open(file_path.name, 'rb')
           pdfReader = PyPDF2.PdfFileReader(f)
           for page in range(pdfReader.numPages):
               pageObj = pdfReader.getPage(page)
               content = content + pageObj.extractText()
           f.close()
        elif(filename_split[1] == "doc" or filename_split[1] == "docx"):
            content = docx2txt.process(file_path.name)
        else:
            f = open(file_path.name, "r")
            content= f.read()
        # Lowercase text
        content = text_lowercase(content)

        # Remove numbers
        content = remove_numbers(content)

        # remove punctuation
        content = remove_punctuation(content)

        # remove whitespace from text
        content = remove_whitespace(content)

        # remove stopwords
        content = remove_stopwords(content)

        # stem words in the list of tokenized words
        content = stem_words(content)

        # lemmatize string
        lemmatize_word(content)
        print(content)


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    
input_document = Label(
    ws, 
    text='Upload Document for text summarization '
    )
input_document.grid(row=3, column=0, padx=10)

choose_btn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
choose_btn.grid(row=3, column=1)

upld = Button(
    ws, 
    text='Upload File', 
    command=uploadFiles
    )
upld.grid(row=5, columnspan=3, pady=10)

ws.mainloop()