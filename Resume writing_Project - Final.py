#Welcome Note and Opening the file
print("Welcome to the Resume Writing".center(70,'*'))
f=open("My_Resume.txt","w")
print("\nResume Sections Available: ")
list1=['1.Contact Details','2.Educational Qualifications-College','3.Educational Qualifications-School','4.Professional Experiences','5.Professional Projetcs','6.Educational Projects','7.Skiils/Area of Expertise','8.Extra Curricular Activities']
for i in list1:
    print(i)

#Selection of Sections
print("\n")
print("Kindly Select The Sections For Your Resume Below".center(70,'*'))
cd=input("Do you want to include your contact details?(yes/no): ")
eqc=input("Do you want to include your Educational Qualifications-College?(yes/no): ")
eqs=input("Do you want to include your Educational Qualifications-School?(yes/no): ")
pe=input("Do you want to include your Professional Experiences?(yes/no): ")
pp=input("Do you want to include your Professional projects?(yes/no): ")
ep=input("Do you want to include your educational projects?(yes/no): ")
sa=input("Do you want to include your Skillsets and area of expertise?(yes/no): ")
eca=input("Do you want to include your extra-curricular activities?(yes/no): ")
#Writing the sections

#Contact Details
if cd=="yes":
    f.write("Contact Details :")
    print("\n")
    print("Please Enter your Contact Details Below".center(70,'*'))
    name=input("Name: ")
    f.write("\nName:")
    f.write(name)
    mob=input("Contact Number: ")
    f.write("\nContact Number:")
    f.write(mob)
    email=input("Email ID: ")
    f.write("\nEmail ID:")
    f.write(email)
    current_location=input("Current Location: ")
    f.write("\nCurrent Location:")
    f.write(current_location)
    native_location=input("Native Place: ")
    f.write("\nNative Place:")
    f.write(native_location)
    f.write("\n*")
    f.write('*'*70)
    print("End of Contact Details Section".center(70,'*'))
elif cd=="no":
    print("\n")
    print("You have opted out from Contact Detail Section".center(70,'*'))
else:
    print("")

#Educational qualifications - College
if eqc=="yes":
    print("\n")
    print("Please Enter your College Educational Qualifications Below".center(70,'*'))
    f.write("\nEducational Qualifications - College :")
    n_deg=int(input("Number of College Degrees: "))
    for i in range(n_deg):
        j=input("College/Institute Name: ")
        o=input("Degree: ")
        s=input("Specialization: ")
        q=input("Score/Marks/Percentage/CGPA: ")
        k=int(input("Start Year: "))
        l=int(input("End Year: "))
        if l<k:
            print("Finish Year cannot be after Start year")
        else:
            m=l-k
            p=str(k)+"-"+str(l)
        f.write("\nInstitute: ")
        f.write(j)
        f.write("\nDegree: ")
        f.write(o)
        f.write("\nSpecialization: ")
        f.write(s)
        f.write("\nScore/Marks/Percentage/CGPA: ")
        f.write(q)
        f.write("\nTeure: ")
        f.write(p)
        f.write(" Duration(In Years): ")
        f.write(str(m))
    f.write("\n*")
    f.write('*'*70)
    print("End of Educational Qualification - College Section".center(70,'*'))
elif eqc=="no":
    print("\n")
    print("You have opted out from Educational Qualifications- College Section".center(70,'*'))
else:
    print("")

#Educational Qualifications - School
if eqs=="yes":
    print("\n")
    print("Please Enter your School Educational Qualifications Below".center(70,'*'))
    f.write("\nEducational Qualifications - School :")
    twelvth=input("12th Score/Marks/Percentages: ")
    twelvth_board=input("Board: ")
    twelvth_year=input("Year: ")
    f.write("\12th Score/Marks/Percentages: ")
    f.write(twelvth)
    f.write("\Board: ")
    f.write(twelvth_board)
    f.write("\nYear: ")
    f.write(twelvth_year)

    tenth=input("10th Score/Marks/Percentages: ")
    tenth_board=input("Board: ")
    tenth_year=input("Year: ")
    f.write("\10th Score/Marks/Percentages: ")
    f.write(tenth)
    f.write("\Board: ")
    f.write(tenth_board)
    f.write("\nYear: ")
    f.write(tenth_year)
    print("End of Educational Qualification - School Section".center(70,'*'))
elif eqs=="no":
    print("\n")
    print("You have opted out from Educational Qualifications- Schools Section".center(70,'*'))
else:
    print("")

#Professional Experiences
if pe=="yes":
    print("\n")
    print("Please Enter your Professional Experiences Below".center(70,'*'))
    f.write("\nProfessional Experiences :")
    n_org=int(input("Number of Organizations you worked and Working:"))
    for i in range(n_org):
        j=input("Organization Name:")
        k=input("Designation:")
        l=input("Tenure[Start Month - End Month](Number of years & Months) :")
        f.write("\nOrganization Name:")
        f.write(j)
        f.write("\Designation:")
        f.write(k)
        f.write("\nExperience:")
        f.write(l)
    f.write("\n*")
    f.write('*'*70)
    print("End of Professional Experiences Section".center(70,'*'))
elif pe=="no":
    print("\n")
    print("You have opted out from Professional Experiences Section".center(70,'*'))
else:
    print("")

#Professional Projects
if pp=="yes":
    print("\n")
    print("Please Enter your Professional Projects Below".center(70,'*'))
    f.write("\nProfessional Projects :")
    n_proj=int(input("Number of Projects:"))
    for i in range(n_proj):
        j=input("Projct Title:")
        k=input("Project Tenure[Start Month - End Month](Number of years & Months): ")
        l=input("Project Summary:")
        f.write("\nProject Title:")
        f.write(j)
        f.write("\nProject Tenure:")
        f.write(k)
        f.write("\nProject Summary:")
        f.write(l)
    f.write("\n*")
    f.write('*'*70)
    print("End of Professional Projects Section".center(70,'*'))
elif pp=="no":
    print("\n")
    print("You have opted out from Professional Projects Section".center(70,'*'))
else:
    print("")

#Educational Projects
if ep=="yes":
    print("\n")
    print("Please Enter your Educational Projects Below".center(70,'*'))
    f.write("\nEducational Projects :")
    n_eproj=int(input("Number of Projects:"))
    for i in range(n_eproj):
        j=input("Projct Title:")
        k=input("Project Tenure[Start Month - End Month](Number of years & Months): ")
        l=input("Project Summary:")
        f.write("\nProject Title:")
        f.write(j)
        f.write("\nProject Tenure:")
        f.write(k)
        f.write("\nProject Summary:")
        f.write(l) 
    f.write("\n*")
    f.write('*'*70)
    print("End of Educational Projects Section".center(70,'*'))
elif ep=="no":
    print("\n")
    print("You have opted out from Educational Projects Section".center(70,'*'))
else:
    print("")

#Skills & Area of Expertise
if sa=="yes":
    print("\n")
    print("Please Enter your Skills and Area of Expertise Below".center(70,'*'))
    f.write("\nSkills And Area of Expertise :")
    skills=input("Jot down your skills please: ")
    interests=input("Write down your Areas of interets please: ")
    f.write("\nSkill Sets: ")
    f.write(skills)
    f.write("\nAreas of Interests: ")
    f.write(interests)
    f.write("\n*")
    f.write('*'*70)
    print("End of Skills & Area of Expertise Section".center(70,'*'))
elif sa=="no":
    print("\n")
    print("You have opted out from Skills & Area of Expertise Section".center(70,'*'))
else:
    print("")

#Extra Curricular Activities
if eca=="yes":
    print("\n")
    print("Please Enter your Extra Curricular Activities Below".center(70,'*'))
    f.write("\nExtracurricular Activities :")
    ec_activities=int(input("Number of Extra-curricular Activities:"))
    for i in range(ec_activities):
        j=input("Activity Summary: ")
        f.write("\nActivity Summary: ")
        f.write(j)
        f.write("\n*")
    f.write('*'*70)
    print("End of Extracurricular Activities Section".center(70,'*'))
elif eca=="no":
    print("\n")
    print("You have opted out from Extra Curricular Section".center(70,'*'))
else:
    print("")

print("\n")
print("Thank You".center(70,'*'))
print("\n")
print("End Of Resume Writing".center(70,'*'))
f.close()
