import time
#this program will ask 10 questions and give either freddie, mike, jess, or inez the result = 
top = ["two", 2]
three = ["three", 3]
one = ["one", 1]
#lists have to look like this:
#xx = "mommy"
#alist = [1, 2, 1.2, "apples" "pork", xx]

print "Hello. I am ooglaOS back again with a new game"
print "This game is called 10 questions"
print "I will guess your favorite musician in 10 questions or less."
time.sleep(3)
membersingroup = raw_input ("How many members are in the group?")
if membersingroup.lower() in top:
	numberofalbums = raw_input ("How many albums do they have")
	if numberofalbums.lower() in three:

		print "according to my calculations..."
		print "..................."
		time.sleep(4)
		print "twenty one pilots"
	elif numberofalbums.lower() in one:
		print "you really like"
		time.sleep(4)
		print "Macklemore."
elif membersingroup.lower()in one:
	letterofname = raw_input ("What is the first letter of your name?")
	#fullname = raw_input("enter your name")
	#firstlet = fullname[0]
		if letterofname.lower() == "f":
			print "according to my calculations"
			time.sleep(3)
			print ("Weezy F Baby. And the F is for phenonmenal")
elif letterofname.lower() == "j"
	



##this is to remind you about flow control


#if name in list:
    #do this
    #do this
#elif name in otherlist:
    #do this
    #do this
#else:
    #do this
