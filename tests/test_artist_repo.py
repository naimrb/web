from lib.artist_repository import ArtistRepository

def test_initalising(db_connection):
    repo = ArtistRepository(db_connection)
    assert isinstance(repo, ArtistRepository)
    assert repo._connection == db_connection

def test_all(db_connection):
    repo = ArtistRepository(db_connection)
    artists = repo.all()
    assert len(artists) == 5