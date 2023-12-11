from lib.artist import Artist

class ArtistRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        artists = []

        for row in rows:
            artist = Artist(row['name'], row['genre'], row['id'])
            artists.append(artist)
        
        return artists

    def insert(self, name, genre):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)",
                                 (name, genre))
    
    def find(self, id):
        rows = self._connection.execute(f"SELECT * FROM artists WHERE id = {id}")
        artist = Artist(rows[0]['name'], rows[0]['genre'], rows[0]['id'])
        
        return artist