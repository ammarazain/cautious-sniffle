def Area_Per(a,b):
    a=int(a)
    b=int(b)
    Area=a*b
    Perimeter=2*a+2*b
    print("the area of given rectangle is: ",Area)
    print("the perimeter of given rectangle is: ",Perimeter)
while True:
    h=input("enter length of side: ")
    w=input("enter breadth: ")
    Area_Per(h,w)

