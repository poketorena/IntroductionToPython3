from myclass.datalog import Datalog


class MyData(Datalog):
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)


obj = MyData()
obj.log("あいう")
obj.log("abc")
obj.log(123)
obj.printlog()
