import PyPDF2
import sys
from data_cleaning import get_file


def pdf_to_txt(file_name):
    if file_name[-4:] == ".pdf":
        txt_file = file_name.replace('.pdf', '.txt')
        with open(file_name, 'rb') as pdf_file, open(txt_file, 'w') as text_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            num_pages = read_pdf.getNumPages()
            for page_num in range(num_pages):
                page = read_pdf.getPage(page_num)
                page_content = page.extractText()
                text_file.write(page_content)
            get_file(txt_file)
    else:
        sys.exit("Please select a PDF file for summarization.")