# Tests for your routes go here

def test_route_artist_get(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_route_artist_post(web_client):
    response = web_client.post('/artists', data = {'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"