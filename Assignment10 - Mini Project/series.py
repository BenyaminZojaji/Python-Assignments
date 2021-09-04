import media
class Series(media.Media):
    def __init__(self, CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS, SEASON, EPISODE, GENRE):
        super().__init__(CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS)
        self.season = SEASON
        self.episode = EPISODE
        self.genre = GENRE
    def showInfo(self):
        super().showInfo()
        print('genre: %s\nseason: %s\nepisod per season: %s'%(self.genre, self.season, self.episode))
    def edit(self):
        super().edit()
        self.season = input('New Season: ')
        self.episode = input('New Episode: ')
        self.genre = input('New Genre: ')