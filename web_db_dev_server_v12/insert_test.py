from dao import Dao
from model import PowerPara


class InsertTest(object):
    def __init__(self):
        self.powerpara = PowerPara()
        self.dao = Dao()

    def test(self):
        self.powerpara.vol = "220v"
        self.dao.insertData(self.powerpara)