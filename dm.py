arr=[]
size=int(input("size of arr = "))
for i in range(size):
	val=int(input("enter the value = "))
	arr.append(val)
print(arr)
n=len(arr)
count=0
for i in range(n-2):
	for j in range(i+1,n):
		for k in range(j+1,n):
			if arr[i]<arr[j]<arr[k]:
				count=count+1
print(count)
