x = int(input("enter the number of elements: "))
arr = list(map(int, input("enter the numbers: ").split()))
n = int(input("enter the number u want to find: "))

low=0
high=len(arr)-1
while low <=high:
     mid=(low+high)//2
     
     if arr[mid]==n:
         print("found at first position",mid+1)
         break
     elif arr[mid]<n:
          low=mid+1
     else:
         high=mid-1
else:         
  print("not found")     
         
     
     
     