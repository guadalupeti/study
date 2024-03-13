class Rating:
    def __init__(self,client,rate):
        self.client = client
        self._rate = int(rate)
        if rate < 0 or rate > 5:
            print('\033[31mInvalid value!\033[m')
            exit()
        
    def __str__(self):
        return f'{self.client}: {self.rate}'
    
    @property
    def rate(self):
        return '⭐'*(self._rate)