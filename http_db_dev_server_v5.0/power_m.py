import insert

class PowerMain(object):
    def __init__(self):
        self.inst = insert.Insert()
    def test1(self):
        self.inst.test()

if __name__ == "__main__":
    obj_test = PowerMain()
    obj_test.test1()