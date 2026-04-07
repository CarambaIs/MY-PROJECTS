library = []

def add_song(list,album,title,creator):
 song= {"album":album, "title":title,"creator":creator}
 list.append(song)
 print("Song successfuly added to the library!") 

def remove_song(list,title):
 for song in list: 
  if song["title"]==title:
   list.remove(song)
   print("Song has been removed successfuly")
   return
 print("Song not found") 

def find_song(list,title):
  for song in list:
    if song["title"]==title: 
     print(f"Song found!\n{song['album']}, {song['title']}, {song["creator"]} ")
     return 
  print("Song not found")

def show_song(list):
 for song in list:
  print(f"Album: {song['album']}, Tytuł: {song['title']}, Twórca: {song['creator']}")

add_song(library,"MBDTF","AOTL","KANYE WEST")
show_song(library)