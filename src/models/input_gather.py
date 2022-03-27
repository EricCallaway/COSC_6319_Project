from turtle import pd
import pdf_convert as pdf
import process_data as pd


def return_file(file_path):
    pdf.pdf_to_txt(file_path)

def return_url(url):
    return url

def return_folder(folder_path):
    pd.pickle_folder(folder_path)