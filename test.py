import requests
from datetime import datetime

BASE = "http://127.0.0.1:5000/"

value = datetime.now()

song = {"name": "Alone"}
	   
#Insertion in Audiobook table
book = [{"name": "The Alchemist", "author": "Poulo caohle" , "narrator": "Smith Gold",  "duration": 5000, "uploaded_time" : value.strftime("%m/%d/%Y, %H:%M:%S")},
         {"name": "THE HOUSE OF MIRTH", "author": "EDITH WHARTON" , "narrator": "Andrew",  "duration": 90000, "uploaded_time" : value.strftime("%m/%d/%Y, %H:%M:%S")},
         {"name": "The Fault in Our Stars", "author": "John Green" , "narrator": "Frederic Lewis",  "duration": 80000, "uploaded_time" : value.strftime("%m/%d/%Y, %H:%M:%S")}
       ]

#Update in Audiobook table
book1 = { "narrator": "Garance"}

data1 = { "name": 101 }
#Participants list
s = ['Joe', 'Penny','Hulk']
s1 = ' '.join(map(str, s))
f = ['Ankita']
s2 = ' '.join(map(str, f))



#response = requests.put(BASE + "audiobook/"  + str(i) , book[i])
#Update in Podcast table
pod_cast =  {"host" : "Nelson"}
#Inserting values in podcast table
#for i in range(len(pod_cast)):
#response = requests.put(BASE + "audio/podcast/2", pod_cast)
#Delete entries in song table, audiobook, podcast
#response = requests.delete(BASE + "song/1")
#response = requests.delete(BASE + "audiobook/1")
#response = requests.delete(BASE + "podcast/1")
#Inserting values in AudioBook table
#for i in range(len(book)):
#	response = requests.put(BASE + "audiobook/"  + str(i) , book[i])
#	print(data[i])
#	print(data[i]) 
#Inserting values in Song table
#for i in range(len(data)):
#	response = requests.put(BASE + "audio/song/"  + str(i) , song[i])
#	print(data[i])
#Patch request in audiobook
response = requests.get(BASE + "audiobook/0")
#response = requests.patch(BASE + "audiobook/2" , book1)
print(response)
#response = requests.get(BASE + "audio/audiobook/1")
#print(response.json())
#response = requests.get(BASE + "audio/podcast/1")
#print(response.json())
#response = requests.get(BASE + "audio/song/1")
	