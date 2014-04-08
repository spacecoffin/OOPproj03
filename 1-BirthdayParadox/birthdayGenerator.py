from random import choice

class RandomBirthday:
    # RandomBirthday generates birthdays uniformly at random for
    # non-leap years.
    def __init__(self):
        self.month = ''
        self.day = 1
    
    def generate(self):
        random_int = choice(range(1, 365))
        if random_int < 32:
            self.month = 'jan'
            self.day = random_int
        elif random_int < 60:
            self.month = 'feb'
            self.day = random_int - 31
        elif random_int < 91:
            self.month = 'mar'
            self.day = random_int - 59
        elif random_int < 121:
            self.month = 'apr'
            self.day = random_int - 90
        elif random_int < 152:
            self.month = 'may'
            self.day = random_int - 120
        elif random_int < 182:
            self.month = 'jun'
            self.day = random_int - 151
        elif random_int < 213:
            self.month = 'jul'
            self.day = random_int - 181
        elif random_int < 244:
            self.month = 'aug'
            self.day = random_int - 212
        elif random_int < 274:
            self.month = 'sep'
            self.day = random_int - 243
        elif random_int < 305:
            self.month = 'oct'
            self.day = random_int - 273
        elif random_int < 335:
            self.month = 'nov'
            self.day = random_int - 304
        else:
            self.month = 'dec'
            self.day = random_int - 334
        self.birthday = (self.month, self.day)
        return self.birthday
    
    def __next__(self, number=2):
        if isinstance(number, int):
            print("Met condition with number {}".format(number))
            self.birthday_list = []
            for i in range(number):
                self.birthday_list.append(self.generate())
                return self.birthday_list
        else:
            self.birthday = self.generate()
            print(random_int)
            return self.birthday
    
    def __iter__(self):
        return self

if __name__ == '__main__':
    bday = RandomBirthday()
    for i,birthday in enumerate(bday):
        if i <= 5:
           print (birthday)
        else:
            break
    print ('********************************')
    print ('Three random birthdays:  ', next(bday,3))
    print ('********************************')