# Ask the user for a number and determine whether the number is prime or not.

def prime_check(a):
    check = True
    for i in range(2, a):
        if a % i == 0:
            check = False
            break
    return check


if __name__ == '__main__':
    num = int(input('Enter the number: '))
    check1 = prime_check(num)
    if check1 is True:
        print('Number is Prime')
    else:
        print('Number is not Prime')
