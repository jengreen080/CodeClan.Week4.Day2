from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist_to_save):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist_to_save.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist_to_save.id = id
    return artist_to_save

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['artist_name'], row['id'])
        artists.append(artist)
    return artists

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
