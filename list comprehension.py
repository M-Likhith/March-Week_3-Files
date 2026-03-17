#list comprehension
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expr for var in collection/range]
'''b=[i.upper() for i in a]
print(b)'''


#tasks:
#first letter capital (title)
'''a=["vja","hyd","vzg"]
b=[i.title() for i in a]
print(b)'''

#squares of numbers
'''a=[2,4,5,6,8,12,13]
b=[i*i for i in a]
print(b)
c=[i**2 for i in a]
d=[pow(i,2) for i in a]
print(c)
print(d)'''

#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i for i in range(16) if i%2!=0]
print(a)'''

'''a=[i*i for i in range(16) if i%2==0]
print(a)'''


#print "a" letter in fruit names
'''a=["apple","mango","banana","kiwi","berry","grapes"]
b=[i for i in a if "a" in i]
print(b)'''

#no-elif usage in list comprehension
#if-else usage in list comprehesnion
'''a=[i*i if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
d=c=[a[i]+b[i] for i in range(5)]
print(c)
print(d)'''



