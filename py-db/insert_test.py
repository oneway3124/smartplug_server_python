from house_spider.dao import Dao
from house_spider.model import Person


class InsertTest(object):
    def __init__(self):
        self.person = Person()
        self.dao = Dao()

    def test(self):
        self.person.name = "陈按时"
        self.dao.insertData(self.person)