def _sex__(self):
    valid_sex = ['male', 'female']
    while True:
        self.sex = input('enter your sex (male/female): ')
        if self.sex not in valid_sex:
            print('invalid sex! please enter "male" or "female"')
            continue
        else:
            print('sex is valid')
            # we can check year
            self._year__()
            break
