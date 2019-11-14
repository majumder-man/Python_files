print("Exam Marks for Physics, Chemistry, Math and the eligibility of the candidate")
print("------------------------------------------------------------------------------")

#Physics Score
physics = float(input("Physics Score: "))
if physics > 200 or physics <0:
    print("Enter a valid score between 0 & 200")
    physics = float(input("Physics Score: "))

#Chemistry Score
chemistry = float(input("Chemistry Score: "))
if chemistry >200 or chemistry <0:
    print("Enter a valid score between 0 & 200")
    chemistry = float(input("Chemistry Score: "))

#Maths Score
maths = float(input("Maths Score: "))
if maths >200 or maths< 0:
    print("Enter a valid score between 0 & 200")
    maths = float(input("Maths Score: "))

#Cutoff Marks
cutoff= (physics/4) + (chemistry/4) + (maths/2)
if cutoff >= 195 and cutoff <=200:
    print ("Welcome to IISC Bangalore")
elif cutoff >= 190 and cutoff <195:
    print ("Welcome to IIT Bombay")
elif cutoff >= 180 and cutoff <190:
    print ("Welcome to IIIT Bangalore")
elif cutoff >= 150 and cutoff <180:
    print ("Welcome to IIT Kharagpur")
else:
    print("Better luck next time")
