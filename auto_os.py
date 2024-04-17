import os

def current_directory():
    print(os.getcwd())

current_directory()

def file_path(filename):
    path = os.path.abspath(filename)
    print(path)

file_path('auto.py')
