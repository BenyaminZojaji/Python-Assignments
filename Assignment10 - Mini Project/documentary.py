import media
class Documentary(media.Media):
    def __init__(self, CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS, TIME_SPEND, SUBJECT):
        super().__init__(CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS)
        self.timeSpend = TIME_SPEND
        self.subject = SUBJECT
    def showInfo(self):
        super().showInfo()
        print('subject: %s\ntime spend to make: %s'%(self.subject, self.timeSpend))
    def edit(self):
        super().edit()
        self.timeSpend = input('New Time spend: ')
        self.subject = input('New Subject: ')