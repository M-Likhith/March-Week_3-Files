#range()
#start-stop-step
'''the range function returns the sequence of numbers, starting from 0, by default and increments by one by one and stops before
a specified number'''

'''for i in range(5):    #stop
    print(i)'''

'''for i in range(10,20):
    print(i,end=" ")'''

'''for i in range(0,20,2):
    print(i,end=" ")'''

'''for i in range(5,50,5):
    print(i,end=" ")'''

'''for i in range(3,30,3):
    print(i,end=" ")'''


#student grades
while True:
    marks=int(input("enter the marks:"))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,92):
        print("Grade B")
    elif marks in range(71,82):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")
