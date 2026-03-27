def _year__(self):
    while True:
        try:
            self.year = float(input('enter year (1-4): '))
            if 0 < self.year <= 4:
                print('year is valid')
                break
            else:
                print('year must be between 1 and 4, please re-enter')
        except ValueError:
            print('please enter a number for year')