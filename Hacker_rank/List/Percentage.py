#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

from functools import reduce
if __name__ == '__main__':
    n = int(raw_input()) # No of students
    student_marks = {}  # Empty dictionary
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]  
        scores = map(float, scores) # Float types scores re-mapped.
        student_marks[name] = scores # Now the dictionary contains keys & values.
    query_name = raw_input()
    
    Marks = student_marks[query_name] 
    sum = reduce(lambda x, y, : x + y, Marks) #takes x, y and adds
    average = sum/len(Marks)
    average1 = "{:.2f}".format(average) # printing two decimal values
    print(average1)
    
