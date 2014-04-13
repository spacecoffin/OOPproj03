from birthdayGenerator import RandomBirthday
from birthdayParadox import BirthdayParadox

def main():
    bday = RandomBirthday()
    for i,birthday in enumerate(bday):
        if i <= 5:
           print (birthday)
        else:
            break

    paradox = BirthdayParadox()
    paradox.distribution(28).display()
    print ('********************************')
    
    print ("""In {0} out of 10000 runs some pair out of 15 people
           (randomly chosen in each run) shared the same birthday""".format\
           (paradox.countShareBday(15)))
    print ('********************************')
    
    paradox.tabulate((10,15))
    print ('********************************')
    print()
    paradox.tabulate((33,36),2000)