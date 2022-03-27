from importlib.resources import path
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import os
from click import command
from pyparsing import col
from input_gather import return_file, return_url, return_folder

class CreateWindow:
    def __init__(self, root):
        # Labels
        self.greeting = Label(
            root, 
            text="Welcome to the Text Summarizer\nEither select a file from your local directory or enter a url."
            )
        self.url_label = Label(
            root, 
            text="Enter URL"
            )
        self.file_sel_label = Label(
            root, 
            text="File you have selected"
            )
        self.folder_sel_label = Label(
            root, 
            text="Folder you have selected"
            )

        # Entries
        self.file_selected = Entry(root)
        self.url_input = Entry(root)
        self.url_selected = Entry(root)
        self.folder_selected = Entry(root)

        # Buttons
        self.fe_button = Button(
            root, 
            text="Browse Local Files", 
            command=self.file_explorer, 
            padx=20
            )
        self.sbmt_btn = Button(
            root, 
            text="Submit", 
            command=self.submit_url, 
            padx=20
            )
        self.fol_ex_button = Button(
            root, 
            text="Browse Local Folders", 
            command=self.folder_explorer, 
            padx=20
            )

        # Placements
        self.fe_button.grid(
            column=0, 
            row=1
        )
        self.file_sel_label.grid(
            column=0, 
            row=2
        )
        self.file_selected.grid(
            column=0, 
            row=3
        )
        self.fol_ex_button.grid(
            column=0, 
            row=4
            )
        self.folder_sel_label.grid(
            column=0, 
            row=5
            )
        self.folder_selected.grid(
            column=0, 
            row=6
            )
        self.greeting.grid(
            column=1, 
            row=0, 
            columnspan=9
            )
        self.url_label.grid(
            column=2, 
            row=1
            )
        self.url_input.grid(
            column=2, 
            row=2
            )
        self.sbmt_btn.grid(
            column=2, 
            row=3
            )
        self.url_selected.grid(
            column=2, 
            row=4
            )
    
    def file_explorer(self):
        word_exts = r"*.docx *.doc"
        path = askopenfilename(title="Browse Local Files", filetypes=[("PDF Files", "*.pdf"), ("MS Word", word_exts), ("Google Docs", "*.gdoc"), ("Text File", "*.txt")])
        file_name = os.path.basename(path)
        self.file_selected.insert(0, file_name)
        return_file(path)
        return file_name
    
    def folder_explorer(self):
        path = askdirectory(title="Select Folder")
        folder_name = os.path.basename(path)
        self.folder_selected.insert(0, folder_name)
        return_folder(path)
        return folder_name

    def submit_url(self):
        url = self.url_input.get()
        self.url_selected.insert(0, url)
        return_url(url)
        return url


root = Tk(className="Text Summarizer")
my_root = CreateWindow(root)
root.geometry("800x500")