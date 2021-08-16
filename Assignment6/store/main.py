from colorama import Fore, Back, Style
from time import sleep
import cowsay
import pyqrcode
import png
#from pyqrcode import QRCode
def refreshData():
    myFile = open('database.txt', 'r')
    data = myFile.read()
    dataLine = data.split('\n')
    for piece in dataLine:
        productDict = {}
        if not piece:
            break
        piece = piece.split(',')
        productDict['code'] = piece[0]
        productDict['name'] = piece[1]
        productDict['price'] = int(piece[2])
        productDict['count'] = int(piece[3])
        PRODUCTs[piece[0]] = productDict
    myFile.close()
def showProducts():
    sleep(0.5)
    print('\ncode\tname\t\tprice\tcount\n')
    sleep(0.5)
    for key, value in PRODUCTs.items():
        print('%s\t%s\t\t%i\t%i' %(key, value['name'], int(value['price']), int(value['count'])))
    print()
def load():
    print(Fore.LIGHTYELLOW_EX, end='')
    cowsay.cow('Bni Store')
    print(Style.RESET_ALL, end='')
    refreshData()
def buy():
    cartDic = {}
    while True:
        print('\nHint:You can discard with type \'d\' \n')
        code = input('code: ')
        if code in PRODUCTs.keys():
            while True:
                vlu = input('How much: ')
                if vlu=='d':
                    break
                elif 0<int(vlu)<=int(PRODUCTs[code]['count']):
                    PRODUCTs[code]['count']-=int(vlu)
                    cartDic[code] = {code:code, 'name':PRODUCTs[code]['name'], 'price':int(PRODUCTs[code]['price']), 'count':int(vlu)}
                    if PRODUCTs[code]['count']==0:
                        del PRODUCTs[code]
                    print('Done!')
                    break
                else:
                    print('Thats too much. we have %i only.' %PRODUCTs[code]['count'])
        elif code=='d':
            break
        else:
            print('There is no product with this code.')
    if not cartDic:
        print('You didn\'t buy anything from us. how sad we are! :(')
    else:
        print('\n------------------------------\nThis is your bill:\ncode\tname\t\tprice\tcount\n')
        totalPrice = 0
        for key, value in cartDic.items():
            print('%s\t%s\t\t%i\t%i'%(key, value['name'], value['price'], value['count']))
            totalPrice = totalPrice + (value['price']*value['count'])
        print(Fore.RED + 'You have to pay %i.'%totalPrice)
        print(Style.RESET_ALL, end='')
        print('------------------------------')
    sleep(2)

def saveQrcode():
    while True:
        code = input('\nHint:You can discard by Enter \'d\'\ncode: ')
        if code in PRODUCTs.keys():
            tmp = PRODUCTs[code]['code']+ ','+ PRODUCTs[code]['name']+ ','+ str(PRODUCTs[code]['price'])+ ','+ str(PRODUCTs[code]['count'])
            url = pyqrcode.create(tmp)
            url.png('qrcode/'+ PRODUCTs[code]['name'] + 'QR' + '.png', scale = 6)
            print('\nDone!\n')
            break
        elif code=='d':
            break
        else:
            print('There is no product with this code.')
    
def saveDataInFile():
    myFile = open('database.txt', 'w')
    for key, value in PRODUCTs.items():
        myFile.write('%s,%s,%s,%s\n' %(key, value['name'], str(value['price']), str(value['count'])))
def search():
    while True:
        name = input('Hint:You can discard buy Enter \'d\'\ngive me a name: ')
        if name == 'd':
            break
        found = False
        for key, value in PRODUCTs.items():
            if value['name']==name:
                found = True
                break
        if found:
            print('We have %s in our store.\n'%name)
        else:
            print('sorry we don\'t have it.')
        sleep(1)
def deleteProduct():
    code = input('You can delete product by their code: ')
    try:
        del PRODUCTs[code]
        print('\nDone!')
    except:
        print('\nThere is no product with that code!')
def addNewProduct():
    code = input('\nAdding new product\ncode: ')
    name = input('name: ')
    price = input('price: ')
    count = input('count: ')
    productDict = {}
    productDict['code'] = code
    productDict['name'] = name
    productDict['price'] = int(price)
    productDict['count'] = int(count)
    PRODUCTs[code] = productDict
def editProduct():
    code = input('You can edit product by their code: ')
    try:
        PRODUCTs[code]
        name = input('\nYou can unchange by Enter \'d\'\nnew name: ')
        if name!='d':
            PRODUCTs[code]['name'] = name
        price = input('price: ')
        if price!='d':
            PRODUCTs[code]['price'] = price
        count = input('count: ')
        if count!='d':
            PRODUCTs[code]['count'] = count
        print('\nDone!\n')
    except:
        print('\nThere is no product with that code!')
def userChoose():
    while True:
        print('\n1- Add new product\n2- Edit product\n3- Delete product\n4- Search\n5- Show products\n6- Buy\n7- Save as QRcode\n8- Exit')
        choose=int(input())
        if choose==1:
            addNewProduct()
        elif choose==2:
            editProduct()
        elif choose==3:
            deleteProduct()
        elif choose==4:
            search()
        elif choose==5:
            showProducts()
        elif choose==6:
            buy()
        elif choose==7:
            saveQrcode()
        elif choose==8:
            saveDataInFile()
            exit()
while True:
    PRODUCTs = {}
    load()
    userChoose()