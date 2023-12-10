# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

def test_get_names(web_client):
    response = web_client.get("/names?add=Eddie")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Julia, Alice, Karim, Eddie"
# === End Example Code ===
