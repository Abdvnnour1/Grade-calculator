print( "    This is a grade calculator, welcome.    " )
sbjct_nmbr = int(input( "~ Enter number of subjects :" ))
while  int(sbjct_nmbr) <= 0 :
    print("invalid input")
    sbjct_nmbr = int(input("~ Enter number of subjects :"))
sbjct_max_name = ""
sbjct_min_name = ""
passed = 0
failed = 0
sbjct_name = []
sbjct_grade = []
total = 0
for i in range (sbjct_nmbr) :
  sbjct_name.append ( input ( f"\n~ Enter name of subject number {i+1} :" ))
  while type(sbjct_name[i]) != str :
      print("invalid input")
      sbjct_name.append(input(f"\n~ Enter name of subject number {i + 1} :"))
  grade = float(input(f"\n~ Enter grade of subject {i+1} :"))
  while grade < 0 or grade > 20 :
      print("invalid input")
      grade = float(input ( f"\n~ Enter grade of subject number {i+1} :" ))
  sbjct_grade.append(grade)
  total += grade
lowest_grade = sbjct_grade[0]
highest_grade = sbjct_grade[0]
sbjct_min_name = sbjct_name[0]
sbjct_max_name = sbjct_name[0]
for i in range (sbjct_nmbr) :
    if sbjct_grade [i] < lowest_grade :
        lowest_grade = sbjct_grade[i]
        sbjct_min_name = sbjct_name[i]
    if sbjct_grade [i] > highest_grade :
        highest_grade = sbjct_grade[i]
        sbjct_max_name = sbjct_name[i]
average = total / sbjct_nmbr
print(f"\n* AVERAGE GRADE *\n  Your average grade is {average}")
print(f"* HIGHEST GRADE *\n  Highest grade is {highest_grade} from the subject {sbjct_max_name} and lowest grade is {lowest_grade} from the subject {sbjct_min_name}")
for i in range (sbjct_nmbr) :
     if sbjct_grade[i] < 10 :
         failed += 1
         print(f"You failed {sbjct_name[i]}, the subject's grade is {sbjct_grade[i]}")
     else :
         passed += 1
         print(f"You passed {sbjct_name[i]}, the subject's grade is {sbjct_grade[i]}")
print(f"* FAILED {failed} SUBJECTS\n")
print(f"* PASSED {passed} SUBJECTS\n")
print("thank you for using this program")




