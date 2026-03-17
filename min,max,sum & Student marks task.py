#min,max,sum
'''print(max(3,5,6,7,8,9,10,20,30))
print(min(3,5,6,7,8,9,10,20,30))
#sum
a=3,5,6,7,8,9,10,20,30
print(sum(a))
print(sum([3,5,6,7,8,9,10,20,30]))'''

#student marks analysis
while True:
    a=int(input("enter no of stdents:"))
    marks=[]
    for i in range (a):
            b=int(input("enter the marks {i+1}:"))
        high=max(marks)
low=min(marks)
average=sum(marks)/n
print(" Results  ")
print("highest marks:",high)
print("lowest marks:",low)
print("average marks:",average)
        
    
    
