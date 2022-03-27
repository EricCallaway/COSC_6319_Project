#Utility functions
from importlib.resources import path
import os
import shutil


# Creates a Folder for all pickle objs based on the location of the input obj
def pickle_path(path):
    directory = 'Pickle_Files'
    location = os.path.basename(path)
    pkl_path = path.replace(location, directory)
    if os.path.exists(pkl_path):
        shutil.rmtree(pkl_path)
    os.mkdir(pkl_path)
    return pkl_path
