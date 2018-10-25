from model import PowerPara
from dao import Dao
class Insert(object):
    def __init__(self):
        self.power_para = PowerPara()
        self.dao = Dao()

    def test(self):
        self.power_para.vol = "220v"
        self.dao.insertData(self.power_para)