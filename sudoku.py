import numpy

file_name = "/example/task.txt"

def reader(file):
    f = open (file)
    ver = verif(f)
    if ver:
        data = f
    else:
        print ("File is not correct")
        exit()
    return data

def main():
    data = reader(file_name)
    


