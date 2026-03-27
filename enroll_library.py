def enroll_library(self):
    while True:
        self.name = input('enter your name: ')
        if not self.name:
            print('name cannot be empty, please re-enter')
            continue
        # check whether name is valid
        if not self.name[0].isdigit() and self.name[1:].islower():
            print('name is valid, registration can proceed')
            break
        else:
            print('invalid name! first character cannot be a number, and rest must be lowercase')

