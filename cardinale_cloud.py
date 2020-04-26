from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
from datetime import date, datetime
import time
import uuid

class SheetsRegister:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cardinale-cd9020f252e8.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('cardinale test user').sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    def storeTempInfo(self, user, password):
        uniqueId = str(uuid.uuid4())
        self.newUser = [user, password, uniqueId, date.today().strftime("%m/%d/%y")]
    def uploadInfo(self):
        try:
            self.newUser[0]
        except IndexError:
            print('Empty list')
        else:
            if self.df.last_valid_index() == None:
                self.sheet.insert_row(self.newUser,2)
            else:
                self.sheet.insert_row(self.newUser,self.df.last_valid_index()+3)
    def print(self):
        print(self.newUser)

class SheetsLogin:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cardinale-cd9020f252e8.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('cardinale test user').sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    def storeTempInfo(self, user, passw):
        self.userw = user
        self.passw = passw

    def matchUser(self):
        return self.userw in self.df['email'].values

    def matchPass(self):
        return self.passw in self.df['password'].values

    def getUid(self):
        if self.MatchAcc() == True:
            return self.df.iloc[self.getUserIndex(), 2]

    def getUser(self):
        if self.MatchAcc() == True:
            return self.df.iloc[self.getUserIndex(), 0]

    def getPass(self):
        if self.MatchAcc() == True:
            return self.df.iloc[self.getUserIndex(), 1]

    def getUserIndex(self):
        return int(str(self.df.index[self.df['email'] == self.userw].tolist())[1:-1])

    def getPassIndex(self):
        return int(str(self.df.index[self.df['password'] == self.passw].tolist())[1:-1])

    def checkMatch(self):
        if (self.matchUser() and self.matchPass() == True):
            if self.getUserIndex() == self.getPassIndex():
                return True
            else:
                return False
        else:
            return False

    def MatchAcc(self):
        return self.checkMatch()

    def print(self):
        print(self.getUid())
        print(self.MatchAcc())

class SheetsCurrentUser:
    def __init__(self, user, passw, uid):
        self.email = user
        self.passw = passw
        self.uid = uid

class SheetsProduct:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cardinale-cd9020f252e8.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('Products').sheet1
    data = sheet.get_all_records()
    temp_df = pd.DataFrame(data)
    def __init__(self, uid):
        self.uid = uid
        self.df = self.temp_df.loc[self.temp_df['uid'] == uid]

    def storeTempInfo(self, product, stock, price):
        Date = date.today().strftime("%m/%d/%y")
        Time = time.strftime("%H:%M:%S", time.localtime())
        self.newInfo = [self.uid, product, stock, float(price), Date, Time, Date, Time]
    def uploadInfo(self):
        try:
            self.newInfo[0]
        except IndexError:
            print('Empty list')
        else:
            self.sheet.insert_row(self.newInfo,2)
    def modifyAddStock(self, product, stock):
        if product in self.df['product'].values:
            Date = date.today().strftime("%m/%d/%y")
            Time = time.strftime("%H:%M:%S", time.localtime())
            add = self.getItemStock(product) + stock
            print(add)
            self.sheet.update_cell(self.getItemIndex(product)+2,3, str(add))
            self.sheet.update_cell(self.getItemIndex(product)+2,7, Date)
            self.sheet.update_cell(self.getItemIndex(product)+2,8, Time)
    def modifySubtractStock(self, product, stock):
        if product in self.df['product'].values:
            Date = date.today().strftime("%m/%d/%y")
            Time = time.strftime("%H:%M:%S", time.localtime())
            add = self.getItemStock(product) - stock
            print(add)
            self.sheet.update_cell(self.getItemIndex(product)+2,3, str(add))
            self.sheet.update_cell(self.getItemIndex(product)+2,7, Date)
            self.sheet.update_cell(self.getItemIndex(product)+2,8, Time)
    def modifyPrice(self, product, price):
        if product in self.df['product'].values:
            Date = date.today().strftime("%m/%d/%y")
            Time = time.strftime("%H:%M:%S", time.localtime())
            self.sheet.update_cell(self.getItemIndex(product)+2,4, price)
            self.sheet.update_cell(self.getItemIndex(product)+2,7, Date)
            self.sheet.update_cell(self.getItemIndex(product)+2,8, Time)
    def getTotalProducts(self):
        return self.df['stock'].sum()
    def getItemIndex(self, product):
        if product in self.df['product'].values:
            return int(str(self.df.index[self.df['product'] == product].tolist())[1:-1])
    def getOGDate(self, product):
        return self.df.iloc[self.getItemIndex(product)-1, 4]
    def getOGTime(self, product):
        return self.df.iloc[self.getItemIndex(product)-1, 5]
    def getItem(self, product):
        return product in self.df['product'].values
    def getItemStock(self, product):
        return self.df.iloc[self.getItemIndex(product)-1, 2]
    def getItemPrice(self, product):
        return self.df.iloc[self.getItemIndex(product)-1, 3]
    def sortProductAscending(self):
        self.df = self.df.sort_values('product')
    def sortProductDescending(self):
        self.df = self.df.sort_values('product', ascending=False)
    def sortStockAscending(self):
        self.df = self.df.sort_values('stock')
    def sortStockDescending(self):
        self.df = self.df.sort_values('stock', ascending=False)
    def sortPriceAscending(self):
        self.df = self.df.sort_values('price')
    def sortPriceDescending(self):
        self.df = self.df.sort_values('price', ascending=False)
    def print(self):
        print(self.df)
        print(self.getItemStock('sprite'))

class SheetsSell:
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cardinale-cd9020f252e8.json', scope)
    client = gspread.authorize(credentials)
    sheet = client.open('cardinale sold').sheet1
    data = sheet.get_all_records()
    temp_df = pd.DataFrame(data)
    def __init__(self, uid):
        self.uid = uid
        self.df = self.temp_df.loc[self.temp_df['uid'] == uid]
    def sellProduct(self, product, price):
        Date = date.today().strftime("%m/%d/%y")
        Time = time.strftime("%H:%M:%S", time.localtime())
        newInfo = [self.uid, product, price, Date, Time]
        self.sheet.insert_row(newInfo,2)
    def getNETSalesToday(self):
        Date = date.today().strftime("%m/%d/%y")
        df = self.df.loc[self.df['date sold'] == Date]
        return df['price'].sum()
    def print(self):
        print(self.getNETSalesToday())
if __name__ == "__main__":
    check = SheetsLogin()
    check.storeTempInfo('samsam@gmail.com','sam')
    chek = SheetsProduct(check.getUid())
    chek.modifyPrice('coke mismo',15)
    #chek.print()

'''
CODE GRAVEYARD
        if self.df.iloc[int(str(self.df.index[self.df['product'] == product].tolist())[1:-1]),0] == uid:
            return int(str(self.df.index[self.df['product'] == product].tolist())[1:-1])
'''