def __init__(self):
    self.s = []
    self.m = []

def push(self,x):
   if self.s ==0:
     self.s.append(x)
   if self.m == 0:
     self.m.append(x)
   if self.m ==[-1]:
     self.m[-1].append(x)

def pop(self):
    if self.s !=0:
        return self.s.append(x)
    if self.s[-1] == self.m[-1]:
        return self.m.append(x)
    self.s.append(x)
