from random  import randint
from time import clock

class Array:
    def __init__(self, size, array_type):
        if array_type == 'ascending':
            self.size = size
            self.main_array = [i for i in range(size)]

        elif array_type == 'descending':
            self.size = size
            self.main_array = [size - i for i in range(size)]

        elif array_type == 'random':
            self.size = size
            self.main_array = [randint(0,size) for i in range(size)]
        #print('\n',self.main_array)

    def bubble_sort(self):
        start_time = clock()
        a = self.main_array
        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
        end_time = clock()
        #print(a)
        print('Size:',self.size, ', Time: ',end_time - start_time)


    def selection_sort(self):
        start_time = clock()
        a = self.main_array
        for i in range(len(a)):
            big = i
            for j in range(i, len(a)):
                if a[i] > a[big]:
                    big = i
            a[i], a[big] = a[big], a[i]
            
        end_time = clock()
        #print(a)
        print('Size:',self.size, ', Time: ', end_time - start_time)


    def insertion_sort(self):
        start_time = clock()
        a = self.main_array
        for i in range(1,len(a)):
            for j in range(0,i):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]

        end_time = clock()
        #print(a)
        print('Size:',self.size, ', Time: ', end_time - start_time)                

    def partition(self, a, lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], hi = hi, a[i]
        return i

    def quicksort(self, a, lo, hi):
        if lo < hi:
            p = self.partition(a, lo, hi)
            self.quicksort(a, lo, p-1)
            self.quicksort(a, p+1, hi)

    def call_quicksort(self):
        start_time = clock()
        a = self.main_array
        self.quicksort(a, 0,self.size-1)
        end_time = clock()
        print('Size:',self.size, ', Time: ', end_time - start_time)                

#------------------------------------------------------------
if __name__ == '__main__':
    
    for array_type in ['ascending', 'descending', 'random']:
        for size in [50, 500, 900]:
            A = Array(size, array_type)
            print('\nArray Type: ', array_type)

            print('Bubble: ', end = '\t')
            A.bubble_sort()
            print('Selection: ', end = '\t')
            A.selection_sort()
            print('Insertion: ', end = '\t')
            A.insertion_sort()
            print('Quick: ', end = '\t\t')
            A.call_quicksort()
        print()
