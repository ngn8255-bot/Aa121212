def _sex__(self):
    list = ['male', 'female']
    while True:
        self.sex=input('enter your sex: ')
        if self.sex not in list:
            continue
        else:
            self._year__()
            break
