"""
Structured-english
The program will analyse the grades on a final exam
The program will point to file (Final.txt) and create a list from the text and then close the file
We will write 3 functions and print the output to the user
The first will output the number of grades, 
The second will output the average grade
The third will ouput the precentage of grades above average
"""

"""
Psuedo-Code

#Point to the file Final.txt
infile = open("Final.txt", 'r' )

#Strip the list of grades and create a list for the program to read
grades= [line.rstrip() for lin in file]
infile.close()
for i in range(len(grades)): 
    grades[i] = int(grades[i])
average = sum(grades)
num=0
for grade in grades:
    if grade > average:
        num += 1
 print("Number of grades:")
 print("Average grade:")
 print("Percentage of grades above average:")
"""

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%".format(
    100 * num / len(grades)))
