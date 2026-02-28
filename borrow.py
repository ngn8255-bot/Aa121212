class library:
    def __init__(self,name,sex,year):
        self.name = name
        self.time=year
        self.sex=sex
        self.account=[]
    def check_name(self):
        while True:
            if not self.name[0].isdigit() and self.name[1:].islower():
                self.account.append(self.name)
                break
            else:
                self.name=input('enter your name')
    def enroll_library(self):
        self.name=input('enter your name: ')
        while True:
            if self.name in self.account:
                print('you are already enrolled')
                self._sex__()
                break

            else:
                print('enter a valid name,name can be stored')
                self.check_name()
    def _sex__(self):
        list=['male','female']
        while True:
            if self.sex not in list:
                self.sex=input('enter your sex again')
            else:
                self._year__()
                break
    def _year__(self):
        while True:
            if 0<float(self.time)<=4:
                break
            else:
                self.time=int(input('enter your year'))

        print('it is successful')


d=library('fang','e','4')
d.check_name()
d.enroll_library()






