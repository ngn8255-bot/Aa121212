def _year__(self):
    while True:
        self.year=int(input('enter year: '))
        if 0 < float(self.year) <= 4:
            break
        else:
            continue
