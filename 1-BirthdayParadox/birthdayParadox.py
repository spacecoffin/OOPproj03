from birthdayGenerator import RandomBirthday

class BirthdayParadox:
    # The BirthdayParadox class is designed to illustrate the paradox.
    # The class BirthdayParadox uses RandomBirthday!
    def __init__(self):
        self.runList = []
        self.shares = 0
    
    def make_bday_list(self, number_of_bdays):
        bday_list = []
        bday = RandomBirthday()
        for i in range(number_of_bdays):
            bday.__next__()
            bday_list.append(bday.birthday_int)
        return bday_list
    
    def countShareBday(self, people, runs=10000):
        # performs number of runs as specified by the input. In each run
        # it "chooses people" (as many as specified in the input)
        # uniformly at random. It returns the number of runs in which
        # some pair of people share the same birthday.
        
        self.shares = 0
        bday = RandomBirthday()
        for run in range(runs):
            bday_list = []
            for i in range(people):
                last_bday = bday.birthday_int
                bday.__next__()
                current_bday = bday.birthday_int
                if current_bday in bday_list:
                    self.shares += 1
                    break
                else:
                    bday_list.append(current_bday)
                    continue
        return self.shares
  
    def distribution(self, number):
        # notes the different birthdays of randomly chosen people, as
        # many as specified by the input to the method.
        
        pass

    def display(self):
        # outputs the birth dates of the chosen people with the number
        # of people born on each date shown in parenthesis.
        pass

    def tabulate(self):
        # outputs a table with each row containing the number of people,
        # say n, that lies in the interval given by the input, and
        # fraction of runs (number of which is specified by the input)
        # in which some pair out of the n people (randomly chosen in
        # each run) shares the same birthday.
        pass

if __name__ == '__main__':
    paradox = BirthdayParadox()
    #print(paradox.make_bday_list(3))
    print ("""In {0} out of 10000 runs some pair out of 15 people
       (randomly chosen in each run) shared the same birthday""".format\
       (paradox.countShareBday(15)))
    print ('********************************')