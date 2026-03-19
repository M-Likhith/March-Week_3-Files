#functions
#normal code
'''a=10
b=20
print("the sum is:",a+b)
print("the difference is:",a-b)
print("the product is:",a*b)

a=1000
b=2000
print("the sum is:",a+b)
print("the difference is:",a-b)
print("the product is:",a*b)'''

#using functions ,code
#calculation
'''def calculate(a,b):
    print("the sum is:",a+b)
    print("the difference is:",a-b)
    print("the product is:",a*b)
calculate(10,20)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the modulus is:",a%b)
    print("the integer division is:",a//b)
    print("the power is:",a**b)
calculate(10,20)
calculate(12,6)'''


'''def add(a,b):
    print(a+b)
add(6,8)'''

#run_time
'''def add():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
add()'''

'''while True:
        def fullname():
            fname=input("first name:")
            lname=input("last name:")
            print(fname+" "+lname)
        fullname()'''

#print vs return
'''def mul(a,b):
    print(a*b)
mul(4,5)'''

'''def mul(a,b):
    return a*b
print(mul(6,3))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(3,5))'''


#split bill
'''def bill():
    b=int(input("enter the bill:"))
    p=int(input("enter total persons:"))
    c=(f"amount per person {b//p}")
    print(c)
bill()'''

'''def bill():
    b=int(input("enter the bill:"))
    p=int(input("enter total persons:"))
    a=b//p
    c=("amount per person {}".format(a))
    print(c)
bill()'''

'''def bill():
    b=int(input("enter the bill:"))
    p=int(input("enter total persons:"))
    print("bill is {}".format(b//p))
    c=(f"amount per person",b//p)
bill()'''



#task
def run(a,b):
    c=int(input("enter the option:"))
    if c==1:
        print("the sum is:",a+b)
    elif c==2:
        print("the diff is:",a-b)
    elif c==3:
        print("the product is:",a*b)
    elif c==4:
        print("the ans is:",a//b)
    else:
        print("plz choose the correct option")
run(4,5)




    
