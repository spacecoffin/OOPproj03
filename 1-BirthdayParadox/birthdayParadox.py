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
        return sorted(self.bday_list)
    
        """
        # NOTE TO SELF: Should this method not operate on the shared
        # bday_list?
        self.bday_list = []
        for i in range(number_of_bdays):
            self.bday.__next__()
            self.bday_list.append(self.bday.birthday)
        return self.bday_list
        """

    def display(self):
        # outputs the birth dates of the chosen people with the number
        # of people born on each date shown in parenthesis.
        
        #G = [[randrange(2) for i in range(n)] for i in range(n)]
        
        #for birthday in self.bday_list
        """
        # NOTE TO SELF: This should probably be done as a dict shouldn't it?
        if isinstance(list_to_format, list):
            jan_list = []
            feb_list = []
            mar_list = []
            apr_list = []
            may_list = []
            jun_list = []
            jul_list = []
            aug_list = []
            sep_list = []
            oct_list = []
            nov_list = []
            dec_list = []
            bday_matrix = []
            for birthday_tuple in list_to_format:
                if birthday_tuple[0] is 'jan':
                    jan_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'feb':
                    feb_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'mar':
                    mar_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'apr':
                    apr_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'may':
                    may_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'jun':
                    jun_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'jul':
                    jul_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'aug':
                    aug_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'sep':
                    sep_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'oct':
                    oct_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'nov':
                    nov_list.append(birthday_tuple[1])
                    continue
                elif birthday_tuple[0] is 'dec':
                    dec_list.append(birthday_tuple[1])
                    continue
            bday_matrix.append(sorted(jan_list))
            bday_matrix.append(sorted(feb_list))
            bday_matrix.append(sorted(mar_list))
            bday_matrix.append(sorted(apr_list))
            bday_matrix.append(sorted(may_list))
            bday_matrix.append(sorted(jun_list))
            bday_matrix.append(sorted(jul_list))
            bday_matrix.append(sorted(aug_list))
            bday_matrix.append(sorted(sep_list))
            bday_matrix.append(sorted(oct_list))
            bday_matrix.append(sorted(nov_list))
            bday_matrix.append(sorted(dec_list))
        """    
        pass

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
    paradox = BirthdayParadox()
    # print(paradox.distribution(15))
    paradox.tabulate((30, 35), 2000)
    print ('********************************')
    print()
    paradox.tabulate(13)    