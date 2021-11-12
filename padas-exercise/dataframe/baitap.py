
import pandas as pd 
import json as js

#read file Json
data_artist = pd.read_json('artist_.json',lines=True)
data_artist_credit_name = pd.read_json('artist_credit_name_.json',lines=True)
data_recording = pd.read_json('recording_10000.json',lines=True)

# Join 3 bảng
data1 = pd.merge(data_artist, data_artist_credit_name, left_on='id', right_on='artist')
data2 = pd.merge(data1[['artist', 'artist_credit']],data_recording, on='artist_credit')

# group by artist and count id of recording
final1 = data2.groupby("artist")['id'].count()

print(final1)