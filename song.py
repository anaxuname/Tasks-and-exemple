"""
Создать класс Song с полями track_title , track_artist, track_duration

Создать на его основе класс детеныi DetailedSong с полями desctiption, url, genre
"""

class Song:

    def __init__(self, track_title , track_artist, track_duration):
        self.track_title = track_title
        self.track_artist = track_artist
        self.track_duration = track_duration

class DetailedSong(Song):

    def __init__(self, desctiption, url, genre):
        super.__init__(track_title , track_artist, track_duration)
        self.desctiption = desctiption
        self.url = url
        self.genre = genre