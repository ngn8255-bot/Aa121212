def enroll_library(self):
    self.name = input('enter your name: ')
    while True:
        if self.name in self.account:
            print('you are already enrolled')
            self._sex__()
            break

        else:
            print('enter a valid name,name can be stored')
            self.check_name()
