print "Let\'s get started..."
spy_name = raw_input("What is your name ? :")

if len(spy_name) > 0:
        # logic will be here if condition is true

        spy_salutation = raw_input("What should we call you ? : ")
        spy_name = spy_salutation + " " + spy_name
        print "Welcome %s  Glad to have you back with us.we would like to know more about you." %(spy_name)
else:
    print "invalid user....!!!"

spy_age=int(raw_input("Enter your age :"))

if spy_age > 12 and spy_age < 55:

    print("you are iligible")
    spy_rating = float(raw_input("What is your spy rating :"))
    if spy_rating > 4.7 and spy_rating < 10:
        print"You are a top class spy"

    elif spy_rating >= 3.5 and spy_rating <= 4.5:
        print "You have good face reading skills "

    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print "you are growing too fast"

    else:
        print "you have to improve your skills"

    spy_is_online = True
    print "Authentication complete Welcome %s %s age:  %d  has a rating of : %f." % (
    spy_salutation, spy_name, spy_age, spy_rating)

else:
    print("you are not iligible")








