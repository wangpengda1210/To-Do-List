def tracklist(**kwargs):
    for artist, albums in kwargs.items():
        print(artist)
        for album, song in albums.items():
            print(f"ALBUM: {album} TRACK: {song}")
