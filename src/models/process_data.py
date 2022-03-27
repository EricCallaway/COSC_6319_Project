from data_cleaning import get_file, get_folder
import utilities as util
import pickle
import os
import shutil


def pickle_file(file):
    #Function will pickle individual files
    pass

def pickle_folder(folder_path):
    pkl_path = util.pickle_path(folder_path)
    dirs = os.listdir(folder_path)
    with open(f'{pkl_path}/data.pkl', 'wb') as f:
        for rec in dirs:
            file_dir = f"{folder_path}/{rec}"
            pickle.dump(file_dir, f)
    pkl_path = os.path.join(pkl_path, "data.pkl")
    get_folder(f, pkl_path)

def pickle_url(url):
    # Function will pickle the url of a website
    pass