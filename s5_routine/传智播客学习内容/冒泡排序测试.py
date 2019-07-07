# bubble sort
def bubble_sort(alist):
	for j in range(len(alist)-1,0,-1):
		#j表示每次遍历需要比较的次数，是逐渐减少的
		for i in range(j):
			if alist[i] >alist[i+1]:
				alist[i],alist[i+1]=alist[i+1],alist[i]
li=[23,34,56,56,77,88,54,26]
bubble_sort(li)
print(li)
