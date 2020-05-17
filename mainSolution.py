import sys
def get_max_product(n, array):

    index1 = 0
    for i in range (n):
         if array[i] > array[index1]:
             index1 = i
    if index1 == 0:
         index2 = 1
    else:
         index2 = 0
    for j in range(n):
         if j!=index1 and array[j] > array[index2]:
             index2 = j
    return array[index1] * array[index2]
if __name__ == "__main__":
    n = int(input())
    numbers = [ int(x) for x in input().split() ]
    product = get_max_product(n,numbers)
    
    print(product)
