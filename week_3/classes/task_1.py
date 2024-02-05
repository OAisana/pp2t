class Task_1:
    def __init__(self):
        self.st = ""
    def getString(self):
        self.st = input()
    def printString(self):
        print(self.st.upper())

st = Task_1()
st.getString()
st.printString()
