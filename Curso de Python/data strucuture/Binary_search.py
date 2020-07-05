# -*- coding: utf-8 -*- 

def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False
    
    mid = int(low + high)//2

    if numbers[mid] ==  number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid-1)
    
    else:
        return binary_search(numbers, number_to_find, mid+1,high)


if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    number_to_find = int(input('Type a number to find:  '))

    result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

    if result == True:
        print('El numero si está en la lista')
    else:
        print('El número no está en la lista')