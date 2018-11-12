import os

def rename_files():
    #1. Get file names from a folder
    list = os.listdir(r"/Users/Manuel/Desktop/MOOC/Programming Foundations With Python/prank")
    print(list)
    path = os.getcwd()
    print("The current working directory is " + path)
    os.chdir(r"/Users/Manuel/Desktop/MOOC/Programming Foundations With Python/prank")
    #2. Rename each file
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file in list:
        os.rename(file, file.translate(table))
    os.chdir(path)
rename_files()
