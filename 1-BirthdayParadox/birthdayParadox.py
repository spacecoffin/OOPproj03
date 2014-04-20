from birthdayGenerator import RandomBirthday

class BirthdayParadox:
    # The BirthdayParadox class is designed to illustrate the paradox.
    # The class BirthdayParadox uses RandomBirthday!
    def __init__(self):
        self.bday_list = []
        self.shares = 0
        self.bday = RandomBirthday()
    
    def make_bday_list(self, number_of_bdays):
        self.bday_list = []
        for i in range(number_of_bdays):
            self.bday.__next__()
            self.bday_list.append(self.bday.birthday_int)
        return self.bday_list
    
    def countShareBday(self, people, runs=10000):
        # performs number of runs as specified by the input. In each run
        # it "chooses people" (as many as specified in the input)
        # uniformly at random. It returns the number of runs in which
        # some pair of people share the same birthday.
        
        self.shares = 0
        for run in range(runs):
            self.bday_list = []
            for i in range(people):
                self.bday.__next__()
                current_bday = self.bday.birthday_int
                if current_bday in self.bday_list:
                    self.shares += 1
                    break
                else:
                    self.bday_list.append(current_bday)
                    continue
        return self.shares
  
    def distribution(self, number_of_bdays):
        # notes the different birthdays of randomly chosen people, as
        # many as specified by the input to the method.
        
        self.bday_list = []
        for i in range(number_of_bdays):
            self.bday.__next__()
            self.bday_list.append(self.bday.birthday)
        self.bday_list.sort()
        return self

    def display(self):
        # outputs the birth dates of the chosen people with the number
        # of people born on each date shown in parenthesis.
        
        bday_dict = {}
        month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                      'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        for month in month_list:
            bday_dict[month] = []
        
        for bday in self.bday_list:
            bday_dict[bday[0]].append(bday[1])
        
        for month in month_list:
            print("{}".format(month.capitalize()), end=' ')
            
            for day in range(1, 32):
                if day in bday_dict[month]:
                    print("{}({})".format(
                        day, bday_dict[month].count(day)), end=' ')                
            print()

    def tabulate(self, interval, runs=10000):
        # outputs a table with each row containing the number of people,
        # say n, that lies in the interval given by the input, and
        # fraction of runs (number of which is specified by the input)
        # in which some pair out of the n people (randomly chosen in
        # each run) shares the same birthday.
        
        # Check for appropriate arguments
        if not isinstance(interval, tuple) and not isinstance(interval, list):
            raise TypeError("interval must be a tuple or list.")
        if not isinstance(runs, int): 
            raise TypeError("runs must be an int")
        if runs > 99999:
            raise ValueError("maximum number of runs is 99999")
            
        # Print header, then calculate share ratios and print in loop
        print("Number of runs:  {}".format(runs))
        print('-'*23)
        print("{:<13} Pr[some two share the same birthday]".format(
            "#people"))
        for people in range(interval[0], interval[1]+1):
            self.countShareBday(people, runs)
            print(" {:^7}{}{:>4}/{} ={:.4f}".format(
                people, ' '*10, self.shares, runs, self.shares/runs))

if __name__ == '__main__':
    bday = RandomBirthday()
    for i,birthday in enumerate(bday):
        if i <= 5:
           print (birthday)
        else:
            break

    paradox = BirthdayParadox()
    paradox.distribution(50).display()
    print ('********************************')
    
    print ("In {0} out of 10000 runs some pair out of 15 people"
           "(randomly chosen in each run) shared the same birthday".format\
           (paradox.countShareBday(15)))
    print ('********************************')
    
    paradox.tabulate((10,15))
    print ('********************************')
    print()
    paradox.tabulate((33,36),2000)