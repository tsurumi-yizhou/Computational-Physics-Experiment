class Helper:
    def __init__(self, data=""):
        self.data = data

    def getString(self):
        self.data = input()

    def printString(self):
        print(self.data.upper())


def test_get_str():
    helper = Helper()
    helper.getString()


def test_print_str():
    helper = Helper("test")
    helper.printString()
