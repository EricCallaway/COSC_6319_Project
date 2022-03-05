from importlib.resources import path
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from pyparsing import col

class input_gather:
    def __init__(self, root):
        # Labels
        self.greeting = Label(root, text="Welcome to the Text Summarizer\nEither select a file from your local directory or enter a url.")
        self.url_label = Label(root, text="Enter URL")
        self.file_sel_label = Label(root, text="File you have selected")

        # Entries
        self.file_selected = Entry(root)
        self.url_input = Entry(root)
        self.url_selected = Entry(root)

        # Buttons
        self.fe_button = Button(root, text="Browse Local Files", command=self.file_explorer, padx=20)
        self.sbmt_btn = Button(root, text="Submit", command=self.submit_url, padx=20)

        # Placements
        self.fe_button.grid(column=0, row=1)
        self.file_sel_label.grid(column=0, row=2)
        self.file_selected.grid(column=0, row=3)
        self.greeting.grid(column=1, row=0, columnspan=9)
        self.url_label.grid(column=2, row=1)
        self.url_input.grid(column=2, row=2)
        self.sbmt_btn.grid(column=2, row=3)
        self.url_selected.grid(column=2, row=4)
        
    def file_explorer(self):
        word_exts = r"*.docx *.doc"
        path = askopenfilename(title="Browse Local Files", filetypes=[("PDF Files", "*.pdf"), ("MS Word", word_exts), ("Google Docs", "*.gdoc"), ("Text File", "*.txt")])
        file_name = os.path.basename(path)
        self.file_selected.insert(0, file_name)
        return file_name

    def submit_url(self):
        url = self.url_input.get()
        self.url_selected.insert(0, url)
        return url


root = Tk(className="Text Summarizer")
my_root = input_gather(root)
root.geometry("800x500")
root.mainloop()
