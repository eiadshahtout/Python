def make_album(artistName, albumTitle, numberOfSongs = None):
    album = {
		"Name": artistName,
		"Title" : albumTitle
	}
    if numberOfSongs:
        album["Number_Songs"] = numberOfSongs
    return album

album = make_album("Ed Sheeran", "Shape of YOU")
print(album)
album = make_album("Ed Sheeran", "Shape of YOU", numberOfSongs = 12)
print(album)
album = make_album("Polo G", "!!!")
print(album)