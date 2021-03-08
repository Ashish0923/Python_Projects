# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.


def seq(a):
    first_number = 1
    second_number = 0
    print(first_number)
    for i in range(1, a):
        print(first_number+second_number)
        temp = second_number
        second_number = first_number
        first_number = first_number + temp


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    seq(num)
