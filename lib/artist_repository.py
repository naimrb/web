from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        artists = []

        for row in rows:
            artist = Artist(row['name'], row['genre'])
            artists.append(artist)
        
        return artists

    def insert(self, name, genre):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)",
                                 (name, genre))