from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, Fro, To):
        print(f"Ticket is booked in train no: {self.trainNo} from {Fro} to {To}")
    
    def getStatus(self, ):
        print(f"Train no: {self.trainNo} is running on time")
    
    
    def getFare(self, Fro, To):
        print(f"Ticket fare in train no: {self.trainNo} from {Fro} to {To} is {randint(222,6666)}")
        
t = Train(124343)
t.book("Mumbai", "Chennai")
t.getStatus()
t.getFare("Mumbai", "Chennai")       
        
        