import media
class Film(media.Media):
    def __init__(self, CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS, GENRE):
        super().__init__(CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS)
        self.genre = GENRE
    def showInfo(self):
        super().showInfo()
        print('genre: %s'%self.genre)
    def edit(self):
        super().edit()
        self.genre = input('New Genre: ')