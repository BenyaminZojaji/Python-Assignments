import actor
import pytube
import qrcode
class Media:
    def __init__(self, CATEGORY, NAME, DIRECTOR, IMDBSCORE, URL, DURATION, CASTS):
        self.name = NAME
        self.category = CATEGORY
        self.director = DIRECTOR
        self.imdbScore = IMDBSCORE
        self.url = URL
        self.duration = DURATION
        self.casts = []
        for act in CASTS.split('-'):
            self.casts.append(actor.Actor(act))
    def showInfo(self):
        print('-------------------------------------')
        print('name: %s\ncategory: %s\ndirector: %s\nimdb: %s\nurl: %s\nduration: %s' %(self.name, self.category, self.director, self.imdbScore, self.url, self.duration))
        print('Actors list: ',end='')
        tmp = []
        for i in self.casts:
            tmp.append(i.name)
        print('-'.join(tmp))
    def download(self):
        link = self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='downloaded.mp4')
    def qrcode(self):
        img = qrcode.make(self.category+","+self.name+","+self.url)
        img.save('qrcode/'+self.name+'.png')
    def get_casts(self):
        tmp = []
        for act in self.casts:
            tmp.append(act.name)
        return '-'.join(tmp)
    def edit(self):
        self.name = input('New Name: ')
        self.director = input('New Director: ')
        self.imdbScore = input('New Imdb: ')
        self.url = input('New Url: ')
        self.duration = input('New Duration: ')
        CASTS = input('New Casts: ')
        self.casts = []
        for act in CASTS.split('-'):
            self.casts.append(actor.Actor(act))