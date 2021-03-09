# Write a program (function!) that takes a list and returns a new list that contains all the elements of the 
# first list minus all the duplicates.

# Using Set
def set_rem_dup(a):
    lst2 = set()
    for i in a:
        lst2.add(i)
    return lst2


# Using List
def lst_rem_dup(a):
    lst1 = []
    for i in a:
        if i not in lst1:
            lst1.append(i)
    return lst1


if __name__ == '__main__':
    lst = []
    num = int(input("Enter the number of item in a list: "))
    for i in range(0, num):
        ele = int(input())
        lst.append(ele)

    print(lst)
    print(lst_rem_dup(lst))
    print(list(set_rem_dup(lst)))
