class RailwayForm :
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is: {self.name}")
        print(f"train name is: {self.train}")

priteshApplication =RailwayForm()
priteshApplication.name = "pritesh"
priteshApplication.train ="Rajdhani Express"
priteshApplication.printData()
