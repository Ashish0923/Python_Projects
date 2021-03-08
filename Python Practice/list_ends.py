# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only 
# the first and last elements of the given list. 


def list_ends(a):
    lst1 = [a[0], a[-1]]
    return lst1


if __name__ == '__main__':
    lst = []
    n = int(input("Enter the number of elements for the list: "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)

    print(f'List end items are {list_ends(lst)}')
