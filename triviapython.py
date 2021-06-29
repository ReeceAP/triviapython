import urllib, json, random, sys, html, string
url = "https://opentdb.com/api.php?amount=1"
response = urllib.request.urlopen(url)
data = json.load(response)
datastring = json.dumps(data)
datastringsorted = datastring.replace("&quot;", "")
datastringsorted = html.unescape(datastringsorted)
data = json.loads(datastringsorted)

q1topic = data['results'][0]['category']
print ("Question 1. Topic: " + q1topic)
print ("")
print (data['results'][0]['question'])
print ("")

if data['results'][0]['type'] == "boolean":
        print ("A. True")
        print ("B. False")
        usrBoolAns = input("Please enter your answer here: ")
        ansCorrect = data['results'][0]['correct_answer']
        if usrBoolAns == data['results'][0]['correct_answer']:
                print ("You got it right!")
                sys.exit(0)
        elif usrBoolAns == "A" or usrBoolAns == "a" or usrBoolAns == 1 or usrBoolAns == "true":
                usrBoolAns = "True"
                if usrBoolAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)
        elif usrBoolAns == "B" or usrBoolAns == "b" or usrBoolAns == 0 or usrBoolAns == "false":
                usrBoolAns = "False"
                if usrBoolAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)
        else:
                print ("Wrong :(")
                print ("Correct answer was: " + ansCorrect)
                sys.exit(0)


else:
        ansCorrect = data['results'][0]['correct_answer']
        ansIncorrect1 = data['results'][0]['incorrect_answers'][0]
        ansIncorrect2 = data['results'][0]['incorrect_answers'][1]
        ansIncorrect3 = data['results'][0]['incorrect_answers'][2]
        answers = [ansCorrect, ansIncorrect1, ansIncorrect2, ansIncorrect3]
        random.shuffle(answers)

        #for posAns in answers:
        #       print posAns

        print ("A. " + answers[0])
        print ("B. " + answers[1])
        print ("C. " + answers[2])
        print ("D. " + answers[3])

        usrAns = input("Please enter your answer here: ")
        if usrAns == data['results'][0]['correct_answer']:
                print ("You got it right!")
                sys.exit(0)
        elif usrAns == "a" or usrAns == "A" or usrAns == "1":
                usrAns = answers[0]
                print ("Your answer: " + answers[0])
                #print "[DEBUG]Could have also been: " + answers[0].lower
                if usrAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)


        elif usrAns == "b" or usrAns == "B" or usrAns == "2":
                usrAns = answers[1]
                print ("Your answer: " + answers[1])
                if usrAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)

        elif usrAns == "c" or usrAns == "C" or usrAns == "3":
                usrAns = answers[2]
                print ("Your answer: " + answers[2])
                if usrAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)

        elif usrAns == "d" or usrAns == "D" or usrAns == "4":
                usrAns = answers[3]
                print ("Your answer: " + answers[3])
                if usrAns == data['results'][0]['correct_answer']:
                        print ("You got it right!")
                        sys.exit(0)
                else:
                        print ("Wrong :(")
                        print ("Correct answer was: " + ansCorrect)
                        sys.exit(0)
        else:
                print ("Wrong :(")
                print ("Correct answer was: " + ansCorrect)
                sys.exit(0)
# TO DO:
# Fix bolean type questions, right now they just error - DONE
# Allow answering with 'A' 'B' 'C' 'D'
#       For the above I'm thinking we run an input check on responses such as abcd then run another check where it convers that into an array key which then converts into the associated string which then checks the string (like we have in place now) if it is equal to the correct answer

