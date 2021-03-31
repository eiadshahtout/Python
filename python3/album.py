def make_album(artistName, albumTitle, numberOfSongs = None):
    album = {
		"Name": artistName,
		"Title" : albumTitle
	}
    if numberOfSongs:
        album["Number_Songs"] = numberOfSongs
    return album

while True:
    print("--------------------------------------------")
    artist_n = input("What is the name of the artist? ")
    print("--------------------------------------------")
    album_n = input("What is the title of the album? ")
    print("--------------------------------------------")
    print("This is optional! ")
    numberofsongs = input("What are the number of the songs in the album? ")
    print("--------------------------------------------")
    break

message = make_album(artistName = artist_n, albumTitle = album_n, numberOfSongs = numberofsongs)
print(message)