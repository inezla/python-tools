import sys
sys.path.append('~/Dropbox/python-tools')
import texter
import sched
import time

def gradeGetter():
#this calls adminIlluminate, getGrades, and textMe to get my grades
	gp = texter.adminIlluminate()
	grades = texter.getGrades(gp)
	message = texter.textMe(grades)
	print ("all done")

scheduler = sched.scheduler(time.time, time.sleep)
print 'START:', time.time()
scheduler.enter(5, 1, gradeGetter, ())
scheduler.enter(60, 1, gradeGetter, ())

scheduler.run()