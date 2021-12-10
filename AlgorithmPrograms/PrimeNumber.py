class PrimeNumber:
    first = 0
    second = 0
    
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def calculate(self):
        for num in range(self.first,self.second + 1):  
          if num > 1:  
              for i in range(2,num):  
                   if (num % i) == 0:  
                    break  
              else:  
                   print(num)
 
primeNumberRange = PrimeNumber(0, 1000)
 
primeNumberRange.calculate()
 