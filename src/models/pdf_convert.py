import PyPDF2
import sys
from data_cleaning import get_file


def pdf_to_txt(file_path):
    if file_path[-4:] == ".pdf":
        txt_file = file_path.replace('.pdf', '.txt')
        with open(file_path, 'rb') as pdf_file, open(txt_file, 'w') as text_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            num_pages = read_pdf.getNumPages()
            for page_num in range(num_pages):
                page = read_pdf.getPage(page_num)
                page_content = page.extractText()
                text_file.write(page_content)
            get_file(txt_file, file_path)
    else:
        sys.exit("Please select a PDF file for summarization.")