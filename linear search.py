x=int(input("enter the  number of elements"))
arr=list(map(int,input("enter the numbers").split()))
n=int(input("enter the number u want to find"))

found=False

for i in range(x):
    if arr[i]==n:
        found=True
        break
if found:
        print("found")
else:
        print("notfound")    
    