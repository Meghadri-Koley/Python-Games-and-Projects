import random
from celluloid import Camera
import matplotlib.pyplot as plt

def bubbleSort(arr,x):
	fig=plt.figure()
	camera=Camera(fig)
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				bars=plt.bar(x,arr, color='blue')
				bars[j].set_color('red')
				bars[j+1].set_color('red')
				plt.xlabel('x - axis')
				plt.ylabel('y - axis')
				camera.snap()
	bars=plt.bar(x,arr, color='blue')
	camera.snap()
	animation = camera.animate(interval = 100, repeat = False)
	plt.title('Bubble Sort')
	plt.show()
	plt.close()

def selectionSort(arr, x):
	fig=plt.figure()
	camera=Camera(fig)
	size=len(arr)
	for step in range(size):
		min_idx=step
		for i in range(step+1,size):
			if arr[i]<arr[min_idx]:
				min_idx=i
		arr[step],arr[min_idx]=arr[min_idx],arr[step]
		bars=plt.bar(x,arr,color='blue')
		bars[step].set_color('red')
		bars[min_idx].set_color('red')
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		camera.snap()
	bars=plt.bar(x,arr, color='blue')
	camera.snap()
	animation=camera.animate(interval=100, repeat=False)
	plt.title('Selection Sort')
	plt.show()
	plt.close()

def insertionSort(arr,x):
	fig=plt.figure()
	camera=Camera(fig)
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			bars=plt.bar(x,arr, color='blue')
			bars[j].set_color('red')
			bars[j+1].set_color('red')
			bars[i].set_color('green')
			plt.xlabel('x - axis')
			plt.ylabel('y - axis')
			camera.snap()
			j -= 1
		arr[j+1] = key

	bars=plt.bar(x,arr, color='blue')
	camera.snap()
	animation = camera.animate(interval = 100, repeat = False)
	plt.title('Insertion Sort')
	plt.show()
	plt.close()

#MAIN
arr = []
x= []

print('\nEnter your choice between bubble sort , selection sort and insertion sort visualiser')
print('1 for bubble sort')
print('2 for selection sort')
print('3 for insertion sort')
ch=input('\nEnter your choice : ')

if(int(ch)==1):
    n=int(input('Enter number of elements in array (around 20-30 elements would be ideal to visualise) : '))
    for i in range(n):
        x.append(i)
        arr.append(random.randint(100,999))
    bubbleSort(arr,x)

elif(int(ch)==2):
    n=int(input('Enter number of elements in array (around 80-100 elements would be ideal to visualise) : '))
    for i in range(n):
        x.append(i)
        arr.append(random.randint(100,999))
    selectionSort(arr,x)

elif(int(ch)==3):
    n=int(input('Enter number of elements in array (around 40-50 elements would be ideal to visualise) : '))
    for i in range(n):
        x.append(i)
        arr.append(random.randint(100,999))
    insertionSort(arr,x)
        
else:
    print('Wrong Input')