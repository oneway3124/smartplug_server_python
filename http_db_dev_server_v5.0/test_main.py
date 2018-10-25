import insert_test

class PowerMan(object):
    def __init__(self):
        self.insert_test = insert_test.InsertTest()

def test_db():
    obj_test = PowerMan()
    obj_test.test()


if __name__ == '__main__':
	test_db()
	