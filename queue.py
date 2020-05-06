class FIFOqueue():

    def __init__(self):
        self.queue = [] 

    def Addtoqueue(self, x):
        self.queue.append(x)

    def Popfromqueue(self):
        
        if len(self.queue) != 0:
            x = self.queue[0] 
            del self.queue[0]  
            return x
        else:
            return None 

    def Sizeofqueue(self):
        return len(self.queue)