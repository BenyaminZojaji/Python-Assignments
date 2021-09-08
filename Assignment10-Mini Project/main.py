import film, series, documentary, clip
import csv
class Main:
    def __init__(self):
        print('Hello there! just a second for loading Data!')
        self.totalMedia = []
        with open('db.csv') as f:
            reader = csv.reader(f)
            for data in reader:
                if not data:
                    break
                if data[0]=='film':
                    self.totalMedia.append(film.Film(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
                elif data[0]=='series':
                    self.totalMedia.append(series.Series(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
                elif data[0]=='clip':
                    self.totalMedia.append(clip.Clip(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
                elif data[0]=='documentary':
                    self.totalMedia.append(documentary.Documentary(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
        print('Data loaded!')
        self.menu()
    def menu(self):
        choose = input('1- Add\n2- Edit\n3- Delete\n4- show all medias\n5- Download\n6- Search by name\n7- search by duration\n8- QrCode\n9- save changes and Exit\n')
        if choose=='1':
            self.add()
        elif choose=='2':
            self.edit()
        elif choose=='3':
            self.delete()
        elif choose=='4':
            self.showAllMedias()
        elif choose=='5':
            self.download()
        elif choose=='6':
            self.searchWithName()
        elif choose=='7':
            self.searchWithDuration()
        elif choose=='8':
            self.qrcode()
        elif choose=='9':
            self.saveExit()
    def add(self):
        data = []
        data.append(input('film/series/documentary/clip: '))
        data.append(input('Name: '))
        data.append(input('Director: '))
        data.append(input('Imdb: '))
        data.append(input('Url: '))
        data.append(input('Duration: '))
        data.append(input('Casts: '))
        if data[0]=='film':
            data.append(input('Genre: '))
            self.totalMedia.append(film.Film(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        elif data[0]=='series':
            data.append(input('Season: '))
            data.append(input('Episode: '))
            data.append(input('Genre: '))
            self.totalMedia.append(series.Series(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]))
        elif data[0]=='clip':
            data.append(input('Subject: '))
            self.totalMedia.append(clip.Clip(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        elif data[0]=='documentary':
            data.append(input('Time Spend: '))
            data.append(input('Subject: '))
            self.totalMedia.append(documentary.Documentary(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
        else:
            print('we don\'t support %s format'%data[0])
        self.menu()
    def edit(self):
        NAME = input('name: ')
        for data in self.totalMedia:
            if data.name == NAME:
                data.edit()
                print('Done.')
                self.menu()
        print('There is no media with that name.')
        self.menu()
    def delete(self):
        NAME = input('name: ')
        for data in self.totalMedia:
            if data.name == NAME:
                self.totalMedia.remove(data)
                print('Deleted.')
                self.menu()
        print('There is no media with that name.')
        self.menu()
    def showAllMedias(self):
        for piece in self.totalMedia:
            piece.showInfo()
        self.menu()
    def download(self):
        NAME = input('name: ')
        for data in self.totalMedia:
            if data.name == NAME:
                data.download()
                print('Downloaded.')
                self.menu()
        print('There is no media with that name.')
        self.menu()
    def searchWithName(self):
        NAME = input('name: ')
        for data in self.totalMedia:
            if data.name == NAME:
                print('FOUND.')
                self.menu()
        print('NOT FOUND.')
        self.menu()
    def searchWithDuration(self):
        time = list(map(int, input('give me 2 times i will found films between it. e.g. 70 90  ').split()))
        cnt = 0
        for data in self.totalMedia:
            if data.category=='film' and time[0]<=int(data.duration)<=time[1]:
                print('%i. %s'%(cnt, data.name))
                cnt+=1
        if cnt==0:
            print('sorry we don\'t have a film with your desire duration.')
        else:
            print('we only found %i film(s).'%cnt)
        self.menu()
    def qrcode(self):
        NAME = input('name: ')
        for data in self.totalMedia:
            if data.name == NAME:
                data.qrcode()
                print('QRcode created!')
                self.menu()
        print('There is no such a media with that name!')
        self.menu()
    def saveExit(self):
        with open('db.csv' , 'w' ,newline='') as f:
            writer = csv.writer(f)
            for data in self.totalMedia:
                if data.category=='film':
                    writer.writerow([data.category,data.name,data.director,data.imdbScore,data.url,data.duration,data.get_casts(),data.genre])
                elif data.category=='series':
                    writer.writerow([data.category,data.name,data.director,data.imdbScore,data.url,data.duration,data.get_casts(),data.season,data.episode,data.genre])
                elif data.category=='clip':
                    writer.writerow([data.category,data.name,data.director,data.imdbScore,data.url,data.duration,data.get_casts(),data.subject])
                elif data.category=='documentary':
                    writer.writerow([data.category,data.name,data.director,data.imdbScore,data.url,data.duration,data.get_casts(),data.timeSpend,data.subject])
        exit()
if __name__ == "__main__":
    Main()
