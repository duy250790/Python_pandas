import pandas as pd
import os


# Function read file json, ađd try catch 
def read_filejson(file):
    try:
        data = pd.read_json(file, lines=True)
        print("Read file success")
        return data
    except ValueError:
        print("Have error when read file")


# Functuion check exsit file
def checkexistfile(file):
    i = 0
    while i == 0:
        path_file = "../data/" + file
        if os.path.exists(path_file) is True:
            i += 1
            print("File is existed")
            return path_file
        else:
            print("File is not exist")
            file = input("Input file again:")


# Input file artist, check exist and read file
file_arist = input("Input file artist:")
path_file_artist = checkexistfile(file_arist)
data_artist = read_filejson(path_file_artist)

# Input file artist_credit, check exist and read file
file_artist_credit = input("Input file artist credit:")
path_file_artist_credit = checkexistfile(file_artist_credit)
data_artist_credit = read_filejson(path_file_artist_credit)

# Merge 2 data của file artist and artist name
data_merge_artist_credit = pd.merge(
    data_artist, data_artist_credit, left_on='id', right_on='artist')

# Input file recording, check exist and read file
file_recording = input("Input file recording:")
path_file_recording = checkexistfile(file_recording)
data_recording = read_filejson(path_file_recording)

# Merge with data recoding
data_merge_final = pd.merge(
    data_merge_artist_credit[['artist', 'artist_credit']],
    data_recording, on='artist_credit')

# Group by artist and count id of table recording
result = data_merge_final.groupby("artist")['id'].count()
print(result)
