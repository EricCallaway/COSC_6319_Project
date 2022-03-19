import pdf_convert as pdf


def return_file(file_path):
    pdf.pdf_to_txt(file_path)

def return_url(url):
    return url