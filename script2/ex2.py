import pandas as pd
import os
import json


def read_filejson(file):
    try:
        data = pd.read_json(file, lines=True)
        print("Read success")
        return data
    except ValueError:
        print("Có lỗi khi đọc file")


def checkexistfile(file):
    i = 0
    while i == 0:
        path_file = "../data/" + file
        if os.path.exists(path_file) is True:
            i += 1
        else:
            print("File không tòn tại")
            file = input("input file agin:")
    print("file tồn tại")
    return path_file


# Read file json artist
file = input("input file artist:")
path_file_artist = checkexistfile(file)
data_artist = read_filejson(path_file_artist)

print(data_artist)
