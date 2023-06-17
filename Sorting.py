import sqlite3
class SortingClass:
  def __init__(self):
    self.db = sqlite3.connect("TarifDB.db")
    self.executor = self.db.cursor()
  def SortByPrice(self):
    self.executor.execute("SELECT * from TarifBase ORDER BY Price")
    return self.executor.fetchall()
  def SortByInternet(self):
    self.executor.execute("SELECT * from TarifBase ORDER BY InternetAm")
    return self.executor.fetchall()
  def SortByMinute(self):
    self.executor.execute("SELECT * from TarifBase ORDER BY MinuteAm")
    return self.executor.fetchall()
  def GetAll(self):
    self.executor.execute("SELECT* FROM TarifBase")
    return self.executor.fetchall()
  def SortByUser(self, price, Internet, Minute, MinuteForAll):
    self.executor.execute("select * from TarifBase WHERE Price >=:price AND InternetAm >=:internet AND MinuteAm >=:minute AND MinuteForOther >=:minAll", {"price": price, "internet":Internet, "minute":Minute , "minAll":MinuteForAll })
    return self.executor.fetchall()