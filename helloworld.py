import time
import sys


goodnames = ["inez", "nezzie", "mike", "dad"]

for xx in range(10):
	print("\n")
#print("\n\n\n\n\n") # this makes new lines
print "Hello."
time.sleep(2)
print "My name is ooglaOS."
time.sleep(1)
print "I am a mind reader. Many people do not believe me, but I am the highest quality reader available in 2015"
print "If you are questioning my skill, please take the test below"
time.sleep(4)
print("\n\n") # this makes new lines
sys.stdout.flush()
susboy = raw_input("Please enter your name: ")


print "Thanks {}".format(susboy)	

print "I will now analyze your personality. Please stand by"
time.sleep(1)
print "......................"
time.sleep(3)

if susboy.lower() in goodnames:
	print "According to my calculations you are a"
	for xx in range(5):
		print "swagmaster :)"
		print '\a'
	time.sleep (2)
	print "I predict you will major in awesome.	"

elif susboy.lower() == "freddie":
	print "you are a super susser"

else:
	print "According to my calculations you are a "
	for ii in range(5):
	#print ii
		print "susser!"
		print '\a'
	time.sleep(2)	
	print "I predict you will major in tumpology"





time.sleep(2)
print "Thank you."
