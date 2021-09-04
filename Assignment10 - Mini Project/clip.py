import media
class Clip(media.Media):
    def __init__(self, CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS, SUBJECT):
        super().__init__(CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS)
        self.subject = SUBJECT
    def showInfo(self):
        super().showInfo()
        print('subject: %s'%(self.subject))
    def edit(self):
        super().edit()
        self.subject = input('New Subject: ')