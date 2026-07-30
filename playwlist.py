list=[2,5,6,4,8,9,3,1,4]
print(list)
count=0
for i in list:
    count+=i
avg=count/len(list)
print('sum=',count)
print('average=',avg)
list.sort()
print('the smallest element is',list[0])
print('the largest element is',list[-1])
