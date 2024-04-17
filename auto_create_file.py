from os import path


def create_file(filename):
    if not path.exists(filename):
        try:
            with open(filename, 'w') as file:
                file.write('Welcome to Python!')
            print('File created successfully!')
        except FileNotFoundError:
            print('There was an error creating the file!')
    else:
        print('File already exists!')

create_file('./data/my_file.txt')