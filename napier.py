a={1:3,2:9,3:27,4:81,5:247,6:741,7:2223,
   8:6669,9:20007,10:60021,11:180063,
   12:540189}
user1=int(input("Enter 1st number: "))
user2=int(input("Enter 2nd number: "))
s=user1+user2
print(s)
if s in a:
 print("ANSWER: ",a[s])
