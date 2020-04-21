import re


name = raw_input("Enter your name: ")
yesPhone = False
number = 0
while yesPhone == False:
    phone = raw_input("Please enter your phone number in ***-***-**** format. ")
    if (len(phone) != 12):
        print ("The phone number is not in correct length")
        continue
    else:
        print ("You have put in the correct length")
        number = phone[0:3] + phone[4:7] + phone[8:12]
        try:
            int(number)
            print ("You have input the correct format. ")
            yesPhone = True
        except ValueError:
            print("ERROR! Please input in the correct format")
            continue
        if (phone[3] == "-" and phone[7] == "-"):
            print ("Everything is OK")
            yesPhone = True
        else:
            print("Please use a hyphen (-) to separate numbers")
            continue


gpaGood = False
gpa = 0

while gpaGood == False:


    try:
        gpa = raw_input("Please enter your GPA. \n")
        if  (float(gpa)>=0.0 and float(gpa)<= 4.0):
            print "GPA is valid"
            gpaGood = True
    except ValueError:
        print "GPA input is invalid"
        gpaGood = False




validEmail = False
while validEmail == False:
    email = raw_input("Please enter a valid email address \n")
    if not re.match(r"^[a-zA-Z0-9]+@[a-zA-z0-9]+(\.[a-zA-Z0-9]+)*\.[a-zA-Z0-9]{3}$", email):
        print "That email is not correct"
    else:
        print "Email is valid"
        validEmail = True



