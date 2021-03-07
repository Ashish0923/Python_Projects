# Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

def list_overlap(list_a,list_b):
    ls = []
    size_a = len(list_a)
    size_b = len(list_b)
    if (size_a > size_b):
        for element in list_a:
            if element in list_b:
                ls.append(element)
    else:
        for element in list_b:
            if element in list_a:
                ls.append(element)
    return ls


if __name__ == '__main__':
    list_a = []
    list_b = []
    n1 = int(input("Enter the number of elements for first list: "))
    for i in range(0, n1):
        ele = int(input())
        list_a.append(ele)
    n2 = int(input("Enter the number of elements for first list: "))
    for i in range(0, n2):
        ele = int(input())
        list_b.append(ele)
    print(f'Entered Lists are {list_a} , {list_b}')
    print(f'Overlap elements in both list is {list_overlap(list_a,list_b)}')
