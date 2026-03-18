#min,max,sum
'''print(max(3,5,6,7,8,9,10,20,30))
print(min(3,5,6,7,8,9,10,20,30))
#sum
a=3,5,6,7,8,9,10,20,30
print(sum(a))
print(sum([3,5,6,7,8,9,10,20,30]))'''

#student marks analysis
stud=int(input("enter no of stdents:"))
marks=[]
for i in range (stud):
    a=int(input("enter the marks :"))
    marks.append(a)
for j in marks:
    print(j)
high=max(marks)    
low=min(marks)
total=sum(marks)
average=total//stud
print(" Results  ")
print("highest marks:",high)
print("lowest marks:",low)
print("total marks:",total)
print("average marks:",average)
