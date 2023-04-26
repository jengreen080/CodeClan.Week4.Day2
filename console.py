from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Queen")
artist_repository.save(artist_1)
artist_2 = Artist("Green Day")
artist_repository.save(artist_2)

artist_repository.select_all()

