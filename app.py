import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/artists', methods=['GET', 'POST'])
def get_artists():
    if request.method == "GET":
        repo = ArtistRepository(get_flask_database_connection(app))
        artists = repo.all()
        names = []
        for i in artists:
            names.append(i.name)
        
        return render_template('artists.html', artists=artists)
    
    if request.method == "POST":
        name = request.form['name']
        genre = request.form['genre']

        repo = ArtistRepository(get_flask_database_connection(app))
        repo.insert(name, genre)
        
        return ""
        
@app.route('/artists/<id>', methods=['GET'])
def get_artists_id(id):
    repo = ArtistRepository(get_flask_database_connection(app))
    artist = repo.find(id)

    return render_template('id.html', id=id, artist=artist)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

